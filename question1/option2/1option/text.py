import os
def encrypt_file(shift1, shift2, raw_path, encrypted_path):
    with open(raw_path, "r") as file:
        content = file.read()

    encrypted = ""

    for char in content:
        if char.islower():
            pos = ord(char) - ord('a')

            if 'a' <= char <= 'm':
                new_pos = (pos + shift1 + shift2) % 26

            else:
                new_pos = (pos - (shift1 + shift2)) % 26

            encrypted += chr(ord('a') + new_pos)

        elif char.isupper():
            pos = ord(char) - ord('A')

            if 'A' <= char <= 'M':
                new_pos = (pos - shift1) % 26

            else:
                new_pos = (pos + (shift2 ** 2)) % 26

            encrypted += chr(ord('A') + new_pos)

        else:
            encrypted += char

    with open(encrypted_path, "w") as file:
        file.write(encrypted)

def decrypt_file(shift1, shift2, encrypted_path, decrypted_path):
    with open(encrypted_path, "r") as file:
        content = file.read()

    decrypted = ""

    for char in content:
        if char.islower():
            pos = ord(char) - ord('a')

            if 'a' <= char <= 'm':
                new_pos = (pos - (shift1 + shift2)) % 26

            else:
                new_pos = (pos + shift1 + shift2) % 26

            decrypted += chr(ord('a') + new_pos)

        elif char.isupper():
            pos = ord(char) - ord('A')

            if 'A' <= char <= 'M':
                new_pos = (pos + shift1) % 26

            else:
                new_pos = (pos - (shift2 ** 2)) % 26

            decrypted += chr(ord('A') + new_pos)

        else:
            decrypted += char

    with open(decrypted_path, "w") as file:
        file.write(decrypted)



def verify(raw_path, decrypted_path):
    with open(raw_path, "r") as file:
        original = file.read()

    with open(decrypted_path, "r") as file:
        decrypted = file.read()

    if original == decrypted:
        print("Decryption successful! The files match.")
    else:
        print("Decryption failed! The files do not match.")


def main():
    shift1 = int(input("Enter shift1 value: "))
    shift2 = int(input("Enter shift2 value: "))

    current_dir = os.path.dirname(os.path.abspath(__file__))

    raw_path = os.path.join(current_dir, "raw_text.txt")
    encrypted_path = os.path.join(current_dir, "encrypted_text.txt")
    decrypted_path = os.path.join(current_dir, "decrypted_text.txt")

    encrypt_file(shift1, shift2, raw_path, encrypted_path)
    decrypt_file(shift1, shift2, encrypted_path, decrypted_path)
    verify(raw_path, decrypted_path)



main()
