"""
Vigenere cipher module.
Provides functions to encrypt and decrypt text using the Vigenere cipher.
"""

ALPHABET_SIZE = 26  # number of letters in the English alphabet


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword.upper()
    j = 0
    for ch in plaintext:
        if ch.isalpha():
            shift = ord(keyword[j % len(keyword)]) - ord("A")
            base = ord("A") if ch.isupper() else ord("a")
            ciphertext += chr((ord(ch) - base + shift) % ALPHABET_SIZE + base)
        else:
            ciphertext += ch
        j += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword.upper()
    j = 0
    for ch in ciphertext:
        if ch.isalpha():
            shift = ord(keyword[j % len(keyword)]) - ord("A")
            base = ord("A") if ch.isupper() else ord("a")
            plaintext += chr((ord(ch) - base - shift) % ALPHABET_SIZE + base)
        else:
            plaintext += ch
        j += 1
    return plaintext
