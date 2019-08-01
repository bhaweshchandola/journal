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
    user_details = {"username":user_name, "password":password}
    f.write(json.dumps(user_details))
    f.close()

signup()