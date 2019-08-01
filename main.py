import numpy as np
import os
import json

print("hello")


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
            return True

    print("Authentication Failed")
    return False


login()