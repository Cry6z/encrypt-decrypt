from cryptography.fernet import Fernet
import os

def load_key():
   
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        print("[✔] Key baru dibuat: secret.key")
    return open("secret.key", "rb").read()

def encrypt_text(plain_text):
    key = load_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(plain_text.encode())
    return encrypted.decode()  

def decrypt_text(encrypted_text):
    key = load_key()
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted_text.encode()).decode()
    return decrypted

if __name__ == "__main__":
    print("=== ENCRYPTOR & DECRYPTOR ===")
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    choice = input("Pilih (1/2): ")

    if choice == "1":
        text = input("Masukkan teks yang mau dienkripsi: ")
        encrypted = encrypt_text(text)
        print("Teks terenkripsi:", encrypted)

    elif choice == "2":
        encrypted_text = input("Masukkan teks terenkripsi: ")
        try:
            decrypted = decrypt_text(encrypted_text)
            print("Teks asli:", decrypted)
        except Exception as e:
            print("[!] ERROR: Tidak bisa decrypt ->", str(e))
