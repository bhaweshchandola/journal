import numpy as np
import os
import json
import datetime
from cryptography.fernet import Fernet


# print("hello")

journal_direc = "journals" # journals directory
users_direc = "users" #users directory
key_dir = "key" #encryption key directory


# function to generate key for encryption
def gen_key():
    if not os.path.exists(key_dir):
        key = Fernet.generate_key()
        os.makedirs(key_dir)
        print("directory made")
        f = open(key_dir+"/key.txt", "a+")
        f.write(key.decode())
    return True

''' 
function to encrypt a string
param = input string
returns encrypted string
'''
def encrypt(inp_str):
    key = open(key_dir+"/key.txt", 'r').readline()
    cipher_suite = Fernet(key)
    encoded_text = cipher_suite.encrypt(inp_str.encode())
    # print(encoded_text)
    return encoded_text.decode()


''' 
function to decrypt a string
param = encoded string
returns orignal string
'''
def decrypt(enc_str):
    key = open(key_dir+"/key.txt", 'r').readline()
    cipher_suite = Fernet(key)
    decoded_text = cipher_suite.decrypt(enc_str.encode())
    # print(decoded_text)
    return decoded_text.decode()


'''
function user signup
takes user input username and password
checks number of users whih already exists, limit of 10
create a user by storing username and password in the users.txt file
'''
def signup():
    user_name = input("Plase Enter your Username: ")
    password = input("Please Enter your Password: ")

    if not os.path.exists(users_direc):
        os.makedirs(users_direc)
        print("directory made")
    filename = users_direc + "/users.txt"
    num_lines = sum(1 for line in open(filename))
    
    if num_lines > 10:
        print("*********Users limit reached***********")
    else:
        for line in open(filename, 'r').readlines():
            temp_info = line.split()
            if user_name == temp_info[0]:
                print("*******User Already Exists*********")
                return False

        f = open(filename, "a+")
        user_details = user_name+" "+encrypt(password) + '\n'
        f.write(user_details)
        f.close()
        return user_name


'''
function for user login
takes user input username and password
checks if the username and password matches or not
'''
def login():
    user_name = input("Plase Enter your Username: ")
    password = input("Please Enter your Password: ")

    for line in open("users/users.txt", 'r').readlines():
        temp_info = line.split()
        if user_name == temp_info[0] and password == decrypt(temp_info[1]):
            print("**************User Authenticated*************")
            print("Welcome",user_name)
            print()
            return user_name

    print("********Authentication Failed************")
    print("Try Again")
    return False


'''
function to check number of entries in the journal
param = username
if greater than 50 delete the first entry
'''
def check_entry(username):
    filename = journal_direc +"/"+username+".txt"
    num_lines = sum(1 for line in open(filename))
    # print(num_lines)
    if num_lines > 50:
        print("******Journal Entry Limit Reached*********")
        print("Deleting Earliest Entry")
        with open(filename, 'r') as fin:
            data = fin.read().splitlines(True)
        with open(filename, 'w') as fout:
            fout.writelines(data[1:])
    return num_lines



'''
function to create a journal entry
param = username
creates a file with the username
takes user input for jounal entry
'''
def journal_entry(username):
    # directory_j = "journals"
    if not os.path.exists(journal_direc):
        os.makedirs(journal_direc)
        print("directory made")
    f = open(journal_direc+"/"+username+".txt", 'a+')
    temp_entry = input("Type your Journal Entry\n")
    check_entry(username)
    entry = datetime.datetime.now().strftime("%d %b %Y %I.%M%p").lower() + " - " + temp_entry
    f.write(encrypt(entry))
    f.write('\n')
    f.close()
    return True


'''
function to show journal log
param = username
read the user journal and dispay them in order
'''
def journal_show(username):
    filename = journal_direc + "/" + username + ".txt"
    if os.path.exists(filename):
        f = open(filename)
        lines = f.read().splitlines()
        print()
        for i in lines:
            print(decrypt(i))
        print()
    else:
        print("No Entries Found")



'''
main function
prompts user with option to login, signup or exit
then prompts user with option to view or create a new journal entry
'''
def main_fun():
    main_call = True
    user = False
    while main_call:
    
        if not user:
            try:
                inp = int(input("Press 1 to Login \nPress 2 to Signup \nPress 3 to Exit\n"))
            except:
                print("*******Invalid Input*********")
                continue
            
        if inp == 1 or user:
            if not user:
                user = login()
            if user:
                in_call = True
                while in_call:
                    print()
                    try:
                        inp1 = int(input("Press 1 to make a journal Entry\nPress 2 to view previous entries\nPress 3 to exit to previous menu\n"))
                    except:
                        print("*******Invalid Input*********")
                        continue
                    if inp1 == 1:
                        journal_entry(user)
                    elif inp1 == 2:
                        journal_show(user)
                    elif inp1 == 3:
                        user = False
                        in_call = False
        elif inp == 2:
            user = signup()
            
        elif inp == 3:
            main_call = False
        else:
            pass

    return True
