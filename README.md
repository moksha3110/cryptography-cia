# Auto Key Cipher with Hash Function

## 📌 Description
This project implements the Auto Key Cipher along with a Polynomial Rolling Hash function.

---

## 🔐 Auto Key Cipher

The Auto Key Cipher is a polyalphabetic substitution cipher.

### Encryption:
Ci = (Pi + Ki) mod 26

### Decryption:
Pi = (Ci - Ki) mod 26

The key is extended using the plaintext.

---

## 🔑 Hash Function

Polynomial Rolling Hash is used.

### Formula:
hash = (s[0]*p^0 + s[1]*p^1 + ...) mod m

Where:
- p = 31
- m = 1e9 + 7

---

📊 Example 1

Plaintext: HELLO
Key: KEY

Ciphertext: RIJSS
Decrypted: HELLO

📊 Example 2

Plaintext: WORLD
Key: ABC

Ciphertext: WPTOK
Decrypted: WORLD

## ▶️ How to Run

```bash
python main.py

