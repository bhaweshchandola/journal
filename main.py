import numpy as np
import os
import json
import datetime
from cryptography.fernet import Fernet


print("hello")

journal_direc = "journals"
users_direc = "users"
key_dir = "key"


def gen_key():
    if not os.path.exists(key_dir):
        key = Fernet.generate_key()
        os.makedirs(key_dir)
        print("directory made")
        f = open(key_dir+"/key.txt", "a+")
        f.write(key.decode())
    return True


def encrypt(inp_str):
    key = open(key_dir+"/key.txt", 'r').readline()
    cipher_suite = Fernet(key)
    encoded_text = cipher_suite.encrypt(inp_str.encode())
    print(encoded_text)
    return encoded_text.decode()


def decrypt(enc_str):
    key = open(key_dir+"/key.txt", 'r').readline()
    cipher_suite = Fernet(key)
    decoded_text = cipher_suite.decrypt(enc_str.encode())
    print(decoded_text)
    return decoded_text.decode()


def signup():
    user_name = input("Plase Enter your Username")
    password = input("Please Enter your Password")

    if not os.path.exists(users_direc):
        os.makedirs(users_direc)
        print("directory made")
    filename = users_direc + "/users.txt"
    num_lines = sum(1 for line in open(filename))
    
    if num_lines > 15:
        print("Users limit reached")
    else:
        for line in open(filename, 'r').readlines():
            temp_info = line.split()
            if user_name == temp_info[0]:
                print("user already exists")
                return user_name

        f = open(filename, "a+")
        user_details = user_name+" "+encrypt(password) + '\n'
        f.write(user_details)
        f.close()


def login():
    user_name = input("Plase Enter your Username")
    password = input("Please Enter your Password")

    for line in open("users/users.txt", 'r').readlines():
        temp_info = line.split()
        if user_name == temp_info[0] and password == decrypt(temp_info[1]):
            print("user authenticated")
            return user_name

    print("Authentication Failed")
    return False


def check_entry(username):
    filename = journal_direc +"/"+username+".txt"
    num_lines = sum(1 for line in open(filename))
    print(num_lines)
    if num_lines > 50:
        with open(filename, 'r') as fin:
            data = fin.read().splitlines(True)
        with open(filename, 'w') as fout:
            fout.writelines(data[1:])
    return num_lines


def journal_entry(username):
    # directory_j = "journals"
    if not os.path.exists(journal_direc):
        os.makedirs(journal_direc)
        print("directory made")
    f = open(journal_direc+"/"+username+".txt", 'a+')
    temp_entry = input("Type your Journal Entry")
    check_entry(username)
    entry = datetime.datetime.now().strftime("%d %b %Y %I.%M%p").lower() + " " + temp_entry
    f.write(entry)
    f.write('\n')
    f.close()


def journal_show(username):
    filename = journal_direc + "/" + username + ".txt"
    f = open(filename)
    lines = f.read().splitlines()
    for i in lines:
        print(i)

# journal_entry(login())
# check_entry("bh")
# gen_key()
# print(encrypt("helllooooo"))
# print(decrypt(encrypt("helllooooo")))
# journal_show("bh")
# signup()
login()