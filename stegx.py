import argparse
import cv2
import numpy as np
import hashlib
import os
from PIL import Image
from stegano import lsb
from datetime import datetime
from pathlib import Path

# Simple text banner function
def banner():
    print("""
    Steganography Tool
    ===================
    Made by Al Baradi Joy
    """)

# Footer for the script
def footer():
    print("\nMade by D3fu1t\n")

# Function to ensure image is in RGB mode
def convert_to_rgb(image_path):
    img = Image.open(image_path)
    
    if img.mode != "RGB":
        print(f"[!] {image_path} is in {img.mode} mode. Converting to RGB...")
        img = img.convert("RGB")
        rgb_path = image_path.replace(".png", "_RGB.png")  # Save a new RGB image
        img.save(rgb_path)
        return rgb_path  # Return new image path
    return image_path  # Return original if already RGB

# Function to hide data inside an image
def hide_text(image_path, secret_text, output_path):
    image_path = convert_to_rgb(image_path)  # Convert image if needed

    try:
        secret_img = lsb.hide(image_path, secret_text)
        secret_img.save(output_path)
        print(f"[+] Secret data hidden in {output_path}")
    except Exception as e:
        print(f"[-] Error hiding text: {e}")

# Function to extract hidden data from an image
def extract_text(image_path):
    try:
        secret_text = lsb.reveal(image_path)
        if secret_text:
            print(f"[+] Hidden Message: {secret_text}")
        else:
            print("[-] No hidden data found.")
    except Exception as e:
        print(f"[-] Error extracting data: {e}")

# Function to get file hash
def get_file_hash(file_path, hash_type="sha256"):
    hash_func = getattr(hashlib, hash_type)()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hash_func.update(chunk)
    return hash_func.hexdigest()

# Function to extract metadata
def extract_metadata(file_path):
    try:
        img = Image.open(file_path)
        exif_data = img._getexif()
        if not exif_data:
            print("[-] No EXIF metadata found.")
            return
        for tag, value in exif_data.items():
            print(f"{tag}: {value}")
    except Exception as e:
        print(f"[-] Error extracting metadata: {e}")

# Function to display usage examples
def show_examples():
    print("\n🔥 Examples of Usage:")
    print("🔹 Hide a secret message in an image:")
    print("  python3 stegfore.py hide cover.png \"This is a secret\" output.png")
    print("\n🔹 Extract a hidden message:")
    print("  python3 stegfore.py extract output.png")
    print("\n🔹 Extract metadata from an image:")
    print("  python3 stegfore.py metadata image.jpg")
    print("\n🔹 Get a file's hash (MD5, SHA256, SHA512):")
    print("  python3 stegfore.py hash file.exe --algo sha256")
    print("\n📌 Use '--help' to see all available options.\n")

# Argument parser setup
parser = argparse.ArgumentParser(description="Steganography & Forensics Tool", add_help=False)

subparsers = parser.add_subparsers(dest="command")

# Steganography - Hide
hide_parser = subparsers.add_parser("hide", help="Hide text inside an image")
hide_parser.add_argument("image", help="Path to the cover image")
hide_parser.add_argument("text", help="Secret message to hide")
hide_parser.add_argument("output", help="Output image path")

# Steganography - Extract
extract_parser = subparsers.add_parser("extract", help="Extract hidden text from an image")
extract_parser.add_argument("image", help="Path to the image with hidden data")

# File Hashing
hash_parser = subparsers.add_parser("hash", help="Get file hash")
hash_parser.add_argument("file", help="Path to the file")
hash_parser.add_argument("--algo", default="sha256", help="Hash algorithm (md5, sha256, sha512)")

# Metadata Extraction
meta_parser = subparsers.add_parser("metadata", help="Extract metadata from an image")
meta_parser.add_argument("file", help="Path to the image file")

# Show banner and usage examples if no arguments provided
if len(os.sys.argv) == 1:
    banner()
    parser.print_help()
    show_examples()
    footer()
    os.sys.exit()

# Show banner before processing any command
banner()

# Parse arguments
args = parser.parse_args()

if args.command == "hide":
    hide_text(args.image, args.text, args.output)
elif args.command == "extract":
    extract_text(args.image)
elif args.command == "hash":
    print(f"[+] {args.algo.upper()} Hash: {get_file_hash(args.file, args.algo)}")
elif args.command == "metadata":
    extract_metadata(args.file)
else:
    parser.print_help()
    show_examples()

# Show footer after command execution
footer()
