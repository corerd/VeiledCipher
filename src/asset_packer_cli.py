"""
Steganography in Python.
Hide data across images using encrypted Least Significant Bit (LSB) steganography encode/decode method.

Inspired by OpenPuff
https://embeddedsw.net/OpenPuff_Steganography_Home.html
"""
import argparse

from asset_packer import asset_pack, asset_unpack


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
        asset_pack(args.carrier, args.secret_file, args.password, args.output)
    elif args.command == 'decode':
        asset_unpack(args.stego, args.password, args.dest_file)


if __name__ == "__main__":
    main()
