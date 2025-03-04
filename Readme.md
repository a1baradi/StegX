Here is the README.md content for you to paste directly into your GitHub repository:

# StegX - Steganography Tool

**StegX** is a powerful steganography tool for hiding and revealing secret messages inside images. It supports various functionalities like:

- Hiding text inside images (using LSB technique).
- Extracting hidden text from images.
- Metadata extraction and file hashing.

## Features
- Hide secret messages in PNG images.
- Extract hidden messages.
- Extract metadata from image files.
- Get file hashes (MD5, SHA256, SHA512).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/D3fu1t/StegX.git
   cd StegX

2. Install dependencies:

pip install Pillow stegano opencv-python numpy



Usage

Hide a Secret Message in an Image:

python3 stegfore.py hide cover.png "This is a secret" output.png

Extract Hidden Message from an Image:

python3 stegfore.py extract output.png

Extract Metadata from an Image:

python3 stegfore.py metadata image.jpg

Get File Hash:

python3 stegfore.py hash file.exe --algo sha256

License

This tool is licensed under the MIT License. See the LICENSE file for more information.

Contributing

Feel free to fork the repository and submit pull requests for improvements!

Made by D3fu1t

You can copy and paste this into your `README.md` file in your GitHub repository. Let me know if you need anything else!

