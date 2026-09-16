"""
Steganography in Python.
Hide data across images using encrypted Least Significant Bit (LSB) steganography encode/decode method.

Inspired by OpenPuff
https://embeddedsw.net/OpenPuff_Steganography_Home.html
"""
from PIL import Image
import numpy as np
import os
import argparse
import sys

# --- Re-importing necessary cryptographic functions ---
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256


# --- Encryption/Decryption Helper Functions ---

def encrypt_message(message, password):
    # ... Encryption implementation
    if isinstance(message, str):
        # Fallback for text messages
        data = message.encode('utf-8')
    else:
        # If it's bytes (from the file read), no encoding is needed
        data = message

    pad_len = AES.block_size - (len(data) % AES.block_size)
    padded_data = data + bytes([pad_len]) * pad_len
    
    salt = os.urandom(16)
    key = PBKDF2(password.encode('utf-8'), salt, dkLen=32, count=1000000, hmac_hash_module=SHA256)
    iv = os.urandom(AES.block_size) 
    
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ciphertext = cipher.encrypt(padded_data)
    
    return salt + iv + ciphertext


def decrypt_message(encrypted_bytes, password):
    # ... Decryption implementation
    try:
        salt = encrypted_bytes[:16]
        iv = encrypted_bytes[16:32]
        ciphertext = encrypted_bytes[32:]
        
        key = PBKDF2(password.encode('utf-8'), salt, dkLen=32, count=1000000, hmac_hash_module=SHA256)
        
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        padded_data = cipher.decrypt(ciphertext)
        
        pad_len = padded_data[-1]
        decrypted_bytes = padded_data[:-pad_len]
        
        # Convert the decrypted bytes back into a readable string.
        # return decrypted_bytes.decode('utf-8')

        # Return the raw decrypted bytes object.
        # This allows binary files (like images, zip, pdf) to be saved correctly.
        return decrypted_bytes
    
    except Exception:
        raise ValueError("Decryption failed. The password might be incorrect.")


# --- CORE LSB ENCODE/DECODE FUNCTIONS  ---

def encode_cli(carrier_path, secret_file_path, password, output_path):
    """
    Handles the 'encode' command, hiding a complete file.
    """
    print(f"\n--- Starting Stego Encode: Hiding '{secret_file_path}' in '{carrier_path}' -> '{output_path}' ---")
    
    try:
        # 1. READ RAW BYTES FROM THE SECRET FILE
        with open(secret_file_path, 'rb') as f:
            secret_data_bytes = f.read()
            
        # 2. Encrypt the data
        encrypted_bytes = encrypt_message(secret_data_bytes, password)
        
        # 3. Prepare binary stream (Length Header + Encrypted Data)
        data_len = len(encrypted_bytes)
        length_header = format(data_len, '032b')
        encrypted_binary = ''.join(format(byte, '08b') for byte in encrypted_bytes)
        binary_stream = length_header + encrypted_binary
        total_bits_to_hide = len(binary_stream)
        
        # 4. Load image into NumPy array and Check capacity
        img = Image.open(carrier_path).convert('RGB')
        data = np.array(img, dtype=np.uint8)
        pixels_flat = data.flatten()
        
        if total_bits_to_hide > len(pixels_flat):
            print(f"ERROR: Secret file size ({total_bits_to_hide} bits) exceeds image capacity ({len(pixels_flat)} bits).")
            return
            
        # 5. Perform LSB Encoding
        bits_to_embed = np.array([int(b) for b in binary_stream], dtype=np.uint8)
        target_pixels = pixels_flat[:total_bits_to_hide]
        modified_pixels = (target_pixels & 0xFE) | bits_to_embed
        pixels_flat[:total_bits_to_hide] = modified_pixels
        
        # 6. Save the new image
        new_data = pixels_flat.reshape(data.shape)
        new_img = Image.fromarray(new_data, 'RGB')
        new_img.save(output_path)
        
        print(f"SUCCESS: File encrypted and hidden. Stego-image saved to: {output_path}")

    except FileNotFoundError:
        print(f"ERROR: One or both files not found.")
    except Exception as e:
        print(f"An unexpected error occurred during encoding: {e}")


def decode_cli(stego_path, password, dest_file_path):
    """
    Handles the 'decode' command, extracting the secret file.
    """
    print(f"\n--- Starting Stego Decode: {stego_path} -> {dest_file_path} ---")
    
    try:
        # 1. Load image into NumPy array and extract encrypted bytes
        img = Image.open(stego_path).convert('RGB')
        data = np.array(img, dtype=np.uint8)
        pixels_flat = data.flatten()
        
        # Extract header
        header_lsb = pixels_flat[:32] & 1
        length_binary = "".join(map(str, header_lsb))
        encrypted_data_len = int(length_binary, 2)
        
        total_bits_to_extract = 32 + (encrypted_data_len * 8)
        
        if total_bits_to_extract > len(pixels_flat) or encrypted_data_len == 0:
            print("ERROR: Could not read valid header data.")
            return

        # Extract all relevant LSBs and convert back to encrypted bytes
        data_lsb = (pixels_flat[:total_bits_to_extract] & 1)[32:]
        encrypted_bytes = bytearray()
        for i in range(0, len(data_lsb), 8):
            binary_string = "".join(map(str, data_lsb[i:i+8]))
            encrypted_bytes.append(int(binary_string, 2))
            
        # 2. Decrypt the message
        # decrypt_message returns the raw decrypted bytes of the secret file
        decrypted_file_bytes = decrypt_message(bytes(encrypted_bytes), password)
        
        # 3. WRITE RAW BYTES TO THE DESTINATION FILE
        with open(dest_file_path, 'wb') as f:
            f.write(decrypted_file_bytes)  # pyright: ignore[reportArgumentType]
        
        print(f"\nSUCCESS: File successfully extracted and saved to: {dest_file_path}")

    except FileNotFoundError:
        print(f"ERROR: Stego-image not found at {stego_path}")
    except ValueError as e:
        print(f"ERROR: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during decoding: {e}")


# --- ARGPARSE SETUP ---

def main():
    """Main function to handle command-line arguments."""
    parser = argparse.ArgumentParser(
        description="A secure LSB steganography tool (inspired by OpenPuff).",
        epilog="Usage examples: \n"
               "  - Encode: python stego_tool.py encode -c input.png -m 'secret' -p 'key' -o output.png\n"
               "  - Decode: python stego_tool.py decode -s output.png -p 'key'",
        formatter_class=argparse.RawTextHelpFormatter
    )

    # Use a subparser to handle multiple commands (encode/decode)
    subparsers = parser.add_subparsers(dest='command', required=True, help='Action to perform')

    # 1. ENCODE Subparser
    parser_encode = subparsers.add_parser('encode', help='Encode (hide) a secret file in a carrier image.')
    parser_encode.add_argument('-c', '--carrier', required=True, help='Path to the carrier image file (PNG/BMP).')
    parser_encode.add_argument('-f', '--secret-file', required=True, help='Path to the secret file to hide.') 
    parser_encode.add_argument('-p', '--password', required=True, help='The password for AES encryption.')
    parser_encode.add_argument('-o', '--output', required=True, help='Path to save the resulting stego-image.')
    
    # 2. DECODE Subparser
    parser_decode = subparsers.add_parser('decode', help='Decode (extract) a secret file from a stego-image.')
    parser_decode.add_argument('-s', '--stego', required=True, help='Path to the stego-image file.')
    parser_decode.add_argument('-p', '--password', required=True, help='The password for AES decryption.')
    parser_decode.add_argument('-d', '--dest-file', required=True, help='Path to save the recovered secret file.') 

    # Parse arguments
    args = parser.parse_args()

    # Dispatch command to the relevant function
    if args.command == 'encode':
        encode_cli(args.carrier, args.secret_file, args.password, args.output)
    elif args.command == 'decode':
        decode_cli(args.stego, args.password, args.dest_file)


if __name__ == "__main__":
    main()
