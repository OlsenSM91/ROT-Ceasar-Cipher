import os

# Common English words list
common_words = set(["the", "be", "to", "of", "and", "me", "so", "in", "that", "have", "you"])

def rot_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def rot_decrypt(text, key):
    return rot_encrypt(text, -key % 26)

def load_text_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        print("File does not exist.")
        return None

def save_text_file(file_path, text):
    try:
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
    except OSError as e:
        print(f"Error: {e}")
        print("Failed to save the file.")

def count_common_words(text):
    words = text.split()
    return sum(word.lower() in common_words for word in words)

def decrypt_with_unknown_key(file_path):
    text = load_text_file(file_path)
    best_key = None
    max_count = 0
    best_decryption = ""

    for key in range(1, 26):
        decrypted_text = rot_decrypt(text, key)
        word_count = count_common_words(decrypted_text)
        if word_count > max_count:
            max_count = word_count
            best_key = key
            best_decryption = decrypted_text

    if best_key is not None:
        print(f"Most likely key: {best_key}\nDecrypted text: {best_decryption[:200]}...")  # Limiting preview for longer texts
    else:
        print("No valid decryption found.")

def main_menu():
    while True:
        print("\nROT Cipher Tool")
        print("1. Encrypt text file")
        print("2. Decrypt text file with known key")
        print("3. Decrypt text file with unknown key")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            file_path = input("Enter text file path: ")
            key = int(input("Enter key (1-25): "))
            text = load_text_file(file_path)
            encrypted_text = rot_encrypt(text, key)
            save_text_file(file_path + ".enc", encrypted_text)
            print("File encrypted successfully.")
        elif choice == "2":
            file_path = input("Enter encrypted file path: ")
            key = int(input("Enter key: "))
            text = load_text_file(file_path)
            print("Decrypted text:", rot_decrypt(text, key))
        elif choice == "3":
            file_path = input("Enter encrypted file path: ")
            decrypt_with_unknown_key(file_path)
        elif choice == "4":
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main_menu()
