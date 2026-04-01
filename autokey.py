def clean_text(text):
    return ''.join(filter(str.isalpha, text)).upper()


def encrypt(plaintext, key):
    plaintext = clean_text(plaintext)
    key = clean_text(key)

    extended_key = key + plaintext
    extended_key = extended_key[:len(plaintext)]

    ciphertext = ""

    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - 65
        k = ord(extended_key[i]) - 65
        c = (p + k) % 26
        ciphertext += chr(c + 65)

    return ciphertext


def decrypt(ciphertext, key):
    ciphertext = clean_text(ciphertext)
    key = clean_text(key)

    plaintext = ""

    for i in range(len(ciphertext)):
        k = ord(key[i]) - 65
        c = ord(ciphertext[i]) - 65
        p = (c - k) % 26
        char = chr(p + 65)

        plaintext += char
        key += char  

    return plaintext
