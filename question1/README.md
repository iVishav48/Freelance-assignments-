# Question 1 - Text Encryption/Decryption

This question involves implementing a custom text encryption and decryption algorithm with multiple approaches.

## Problem Description
Create a program that encrypts and decrypts text files using a custom cipher algorithm with different shift values for different character ranges.

## Algorithm Details
The encryption follows these rules:
- **Lowercase letters a-m**: Apply forward shift by `(shift1 * shift2) % 26`
- **Lowercase letters n-z**: Apply backward shift by `26 - (shift1 + shift2) % 26`
- **Uppercase letters A-M**: Apply backward shift by `26 - shift1 % 26`
- **Uppercase letters N-Z**: Apply forward shift by `(shift2 * shift2) % 26`
- **Non-alphabetic characters**: Remain unchanged

## Directory Structure
- `option2/yo.py` - Original implementation with rule tracking
- `option2/1option/main.py` - Alternative implementation
- `option2/1option/text.py` - Another variant
- `option2/raw_text.txt` - Input text file for encryption

## Files Generated
- `encrypted_text.txt` - Result of encryption process
- `decrypted_text.txt` - Result of decryption (should match original)
- `rules.txt` - Track of which encryption rule was applied to each character

## Usage
1. Navigate to the desired implementation directory
2. Run the Python script
3. Enter shift1 and shift2 values when prompted
4. The program will encrypt, then decrypt, and verify the result

## Verification
The program includes a verification step that compares the original text with the decrypted text to ensure the encryption/decryption process is reversible.
