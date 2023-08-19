# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 19:17:55 2023

@author: Pakhomav
"""

from cryptography.fernet import Fernet
import os
import hashlib
import time
import sys

def unic_un(file_path1):
    global file_path
    def text_to_unicode_binary(text):
        unicode_text = " ".join([format(ord(char), 'x') for char in text])
        binary_text = " ".join([format(ord(char), '08b') for char in text])
        return unicode_text, binary_text

    def main():
        try:
            with open(file_path1, 'r', encoding='utf-8') as file:
                text = file.read()
                unicode_text, binary_text = text_to_unicode_binary(text)
            with open(file_path1, 'w', encoding='utf-8') as file:
                file.write(binary_text)
        except:
            print('ERROR *_*')
            sys.exit(0)
    if __name__ == "__main__":
        main()

def bienc_un(file_path2, key):
    def h_encrypt_file(file_path2):
        with open(file_path2, 'rb') as file:
            file_data = file.read()
        hashed_data = hashlib.sha256(file_data).hexdigest()
        return hashed_data

    def f_encrypt_file(file_path2, key):
        if not os.path.exists(file_path2):
            raise FileNotFoundError('ERROR *_*')
        if not os.access(file_path2, os.W_OK):
            raise PermissionError('ERROR *_*')
        if not key:
            raise ValueError("Incorrect key.")
            sys.exit(0)
        fernet = Fernet(key)
        h_encrypt_file(file_path2)
        with open(file_path2, 'rb') as file:
            file_data = file.read()
        encrypted_data = fernet.encrypt(file_data)
        with open(file_path2, 'wb') as file:
            file.write(encrypted_data)
        
    f_encrypt_file(file_path2, key)

def casur_un(file_path3, numkey):
    def caesar_encrypt(text, shift):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text

    def encrypt_file(file_path3, shift):
        try:
            with open(file_path3, 'r') as file:
                original_text = file.read()
            encrypted_text = caesar_encrypt(original_text, shift)
            with open(file_path3, 'w') as file:
                file.write(encrypted_text)
            print('Encryption completed.')
        except:
            print('ERROR *_*')
            sys.exit(0)

    shift = numkey
    encrypt_file(file_path, shift)

file_path = input("Please enter the file name to encrypt: ")
key = Fernet.generate_key()
print("Key：{}".format(key.decode('utf-8')))
casur_un(file_path, 7)
bienc_un(file_path, key)
unic_un(file_path)
bienc_un(file_path, key)
casur_un(file_path, 9)
bienc_un(file_path, key)
unic_un(file_path)
time.sleep(9)
sys.exit(0)