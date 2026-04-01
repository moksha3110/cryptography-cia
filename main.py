from autokey_cipher import encrypt, decrypt
from hash_function import polynomial_hash


def main():
    print("=== Auto Key Cipher with Hash ===")

    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")

    cipher = encrypt(plaintext, key)
    hash_val = polynomial_hash(cipher)
    decrypted = decrypt(cipher, key)

    print("\n--- Results ---")
    print("Plaintext :", plaintext.upper())
    print("Key       :", key.upper())
    print("Ciphertext:", cipher)
    print("Hash      :", hash_val)
    print("Decrypted :", decrypted)


if __name__ == "__main__":
    main()
