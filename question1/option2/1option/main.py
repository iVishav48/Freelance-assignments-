import os

shift1 = int(input("Enter shift1 value: "))
shift2 = int(input("Enter shift2 value: "))

current_dir = os.path.dirname(os.path.abspath(__file__))
raw_path = os.path.join(current_dir, "raw_text.txt")
encryptedpath = os.path.join(current_dir, "encrypted_text.txt")
decryptedpath = os.path.join(current_dir, "decrypted_text.txt")

file = open(raw_path, "r")
content = file.read()
file.close()

encrypted = ""
for char in content:
    if char.islower():
        if char >= 'a' and char <= 'm':
            pos = ord(char) - ord('a')
            new_pos = (pos + shift1 * shift2) % 26
            encrypted += chr(ord('a') + new_pos)
        else:
            pos = ord(char) - ord('a')
            new_pos = (pos - shift1 - shift2) % 26
            encrypted += chr(ord('a') + new_pos)
    elif char.isupper():
        if char >= 'A' and char <= 'M':
            pos = ord(char) - ord('A')
            new_pos = (pos - shift1) % 26
            encrypted += chr(ord('A') + new_pos)
        else:
            pos = ord(char) - ord('A')
            new_pos = (pos + shift2 * shift2) % 26
            encrypted += chr(ord('A') + new_pos)
    else:
        encrypted += char

final_file = open(encryptedpath, "w")
final_file.write(encrypted)
final_file.close()

encrypted_file = open(encryptedpath, "r")
encrypted_content = encrypted_file.read()
encrypted_file.close()

decrypted = ""
for char in encrypted_content:
    if char.islower():
        if char >= 'a' and char <= 'm':
            pos = ord(char) - ord('a')
            new_pos = (pos - shift1 * shift2) % 26
            decrypted += chr(ord('a') + new_pos)
        else:
            pos = ord(char) - ord('a')
            new_pos = (pos + shift1 + shift2) % 26
            decrypted += chr(ord('a') + new_pos)
    elif char.isupper():
        if char >= 'A' and char <= 'M':
            pos = ord(char) - ord('A')
            new_pos = (pos + shift1) % 26
            decrypted += chr(ord('A') + new_pos)
        else:
            pos = ord(char) - ord('A')
            new_pos = (pos - shift2 * shift2) % 26
            decrypted += chr(ord('A') + new_pos)
    else:
        decrypted += char

dec_file = open(decryptedpath, "w")
dec_file.write(decrypted)
dec_file.close()

real_file = open(raw_path, "r")
realcontent = real_file.read()
real_file.close()

decrypted_file = open(decryptedpath, "r")
decryptedcontent = decrypted_file.read()
decrypted_file.close()

if realcontent == decryptedcontent:
    print("Decryption successful, The files match.")
else:
    print("Decryption failed, The files do not match.")
