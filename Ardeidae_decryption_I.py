# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 19:43:51 2023

@author: Pakhomav
"""

from cryptography.fernet import Fernet
import os
import hashlib
import time
import sys

def unic_un(file_path1):
    def binary_unicode_to_text(binary_unicode):
        binary_list = binary_unicode.split()
        text = "".join([chr(int(code, 2)) for code in binary_list])
        return text

    def main():
        try:
            with open(file_path1, 'r', encoding='utf-8') as file:
                binary_unicode = file.read()
                text = binary_unicode_to_text(binary_unicode)
            
            with open(file_path1, 'w', encoding='utf-8') as file:
                file.write(text)
            
        except:
            print('ERROR *_*')

    if __name__ == "__main__":
        main()

def bienc_un(file_path2, key):
    def h_decrypt_file(file_path2, encrypted_data):
        with open(file_path2, 'rb') as file:
            file_data = file.read()
        hashed_data = hashlib.sha256(file_data).hexdigest()
        if hashed_data != encrypted_data:
            print('Decryption failed, has been altered.')
        else:
            return file_data

    def f_decrypt_file(file_path2, key):
        # Check if the file exists.
        if not os.path.exists(file_path2):
            raise FileNotFoundError("ERROR *_*")
        # Check if the file is readable.
        if not os.access(file_path2, os.R_OK):
            raise PermissionError("ERROR *_*")
        # Check if the key is valid.
        if not key:
            raise ValueError("Incorrect key.")
        
        fernet = Fernet(key)
        with open(file_path2, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(file_path2, 'wb') as file:
            file.write(decrypted_data)
    
    f_decrypt_file(file_path2, key)

def casur_un(file_path3, numkey):
    def caesar_decrypt(text, shift):
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        return decrypted_text
    
    def decrypt_file(file_path3, shift):
        try:
            with open(file_path3, 'r') as file:
                encrypted_text = file.read()
            decrypted_text = caesar_decrypt(encrypted_text, shift)
            with open(file_path3, 'w') as file:
                file.write(decrypted_text)
            print('Decryption completed.')
        except:
            print('ERROR *_*')
    
    shift = numkey
    decrypt_file(file_path3, shift)


file_path = input("Please enter the file name to decrypt: ")
key = input("Please enter the key: ")
unic_un(file_path)
bienc_un(file_path, key)
casur_un(file_path,9)
bienc_un(file_path, key)
unic_un(file_path)
bienc_un(file_path, key)
casur_un(file_path, 7)
time.sleep(9)
sys.exit(0)