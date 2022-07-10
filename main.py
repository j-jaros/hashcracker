"""
HashCracker is educational bruteforce software to crack passwords.
To work properly you need to add passwords to passwords.txt.
\nEach password should be in separate lines.

HashCracker works by hashing passwords from passwords.txt one by one and comparing results with hash given by user.
\nHC automatically detects type of hash by measuring length of hash.

Compatible algorithms: SHA1, SHA224, SHA256, SHA384, SHA512, MD5

HashCracker is MIT licensed\n
Author: https://github.com/j-jaros
"""
# Importing hashing library
import time
from hashlib import *
import os


class Crack:
    def __init__(self):
        print("""\033[95m _  _   _   ___ _  _  ___ ___    _   ___ _  _____ ___ 
| || | /_\ / __| || |/ __| _ \  /_\ / __| |/ / __| _ \\
| __ |/ _ \\\\__ \ __ | (__|   / / _ \ (__| ' <| _||   /
|_||_/_/ \_\___/_||_|\___|_|_\/_/ \_\___|_|\_\___|_|_\\\033[0m""")  # Welcome ASCII art
        print("Version: \033[92m0.1\n\033[0mDeveloped by \033[96mJulian Jaros \033[0mhttps://github.com/j-jaros")  # Author information

        if os.path.exists("passwords.txt"):
            pass
        else:
            print("\033[91mCouldn't detect password file.\033[0m")
            input("Press enter to exit...")
            exit()

        # Basic variables
        self.password_list = []
        self.hash_type = None
        self.base_hash = str(input("\nInsert hash: "))
        self.detect_hash_type()

    def detect_hash_type(self):
        print("\n\033[93mDetecting algorithm...\033[0m")
        hash_length = len(self.base_hash)
        if hash_length == 32:  # MD5 detect
            print("\033[92mDetected algorithm is MD5\033[0m")
            self.hash_type = md5

        elif hash_length == 40:  # SHA-1 detect
            print("\033[92mDetected algorithm is SHA-1\033[0m")
            self.hash_type = sha1

        elif hash_length == 56:  # SHA-224 detect
            print("\033[92mDetected algorithm is SHA-224\033[0m")
            self.hash_type = sha224

        elif hash_length == 64:  # SHA-256 detect
            print("\033[92mDetected algorithm is SHA-256\033[0m")
            self.hash_type = sha256

        elif hash_length == 96:  # SHA-384 detect
            print("\033[92mDetected algorithm is SHA-384\033[0m")
            self.hash_type = sha384

        elif hash_length == 128:  # SHA-512 detect
            print("\033[92mDetected algorithm is SHA-512\033[0m")
            self.hash_type = sha512

        else:  # Not supported algorithm
            print("\033[91mThis algorithm is not supported.\033[0m")
            input("Press enter to exit")
            exit()
        self.start_bruteforce()

    def start_bruteforce(self):
        # Reading password file
        try:
            password_amount = 0
            with open("passwords.txt", "r") as f:
                self.password_list = f.read().splitlines()
                password_amount = len(self.password_list)
            print(f"\033[92mPassword file readed successfully.\nAmount of passwords: \033[94m{password_amount}\033[0m")

        except FileNotFoundError:
            print("\033[91mCouldn't find password file.\033[0m")
            input("Press enter to exit")
            exit()

        except Exception as ex:
            print(f"\033[91mException occurred during password file read: {ex}\033[0m")
            input("Press enter to exit")
            exit()

        try:
            count = 0
            founded = False
            start_time = time.time()
            print(f"\n\033[93mEstimate cracking time: \033[94m{round(password_amount*0.000006901, 3)} \033[93mseconds\033[0m")
            for password in self.password_list:
                count += 1
                print(f"\r\033[93mProgress: \033[94m{count}\033[93m/\033[94m{password_amount}\033[0m", end="")
                temp_password = password
                hashed_password = self.hash_type(bytes(password, 'utf-8')).hexdigest()
                if hashed_password == self.base_hash:
                    founded = True
                    break
            end_time = time.time()
            with open("timesPYCHARM.txt", "a+") as d:
                d.write(f"{end_time-start_time}\n")
            if founded:
                print(f"\n\033[92mPassword cracked! Result: \033[95m{temp_password}\033[0m")
                print(f"\n\033[93mCracking completed in \033[94m{round(end_time - start_time, 3)} \033[93mseconds\033[0m")
                input("\nPress enter to exit")
                exit()
            else:
                print(f"\n\033[91mPassword crack failed. Couldn't find match.\033[0m")
                input("Press enter to exit")
                exit()

        except Exception as ex:
            print(f"\033[91mException occurred during password crack: {ex}\033[0m")
            input("Press enter to exit")
            exit()

if __name__ == "__main__":
    crack = Crack()
