import numpy as np
import os
import json
import datetime

print("hello")

journal_direc = "journals"
users_direc = "users"

def signup():
    user_name = input("Plase Enter your Username")
    password = input("Please Enter your Password")

    directory = "users" 
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("directory made")
    f = open(directory+"/users.txt", "a+")
    user_details = user_name+" "+password + '\n'
    f.write(user_details)
    f.close()


def login():
    user_name = input("Plase Enter your Username")
    password = input("Please Enter your Password")

    for line in open("users/users.txt", 'r').readlines():
        temp_info = line.split()
        if user_name == temp_info[0] and password == temp_info[1]:
            print("user authenticated")
            return user_name

    print("Authentication Failed")
    return False

def check_entry(username):
    filename = journal_direc +"/"+username+".txt"
    num_lines = sum(1 for line in open("journals/bh.txt"))
    print(num_lines)

def journal_entry(username):
    # directory_j = "journals"
    if not os.path.exists(journal_direc):
        os.makedirs(journal_direc)
        print("directory made")
    f = open(journal_direc+"/"+username+".txt", 'a+')
    temp_entry = input("Type your Journal Entry")
    entry = datetime.datetime.now().strftime("%d %b %Y %I.%M%p").lower() + " - " + temp_entry
    f.write(entry)
    f.write('\n')
    f.close()

# journal_entry(login())
check_entry("bh")