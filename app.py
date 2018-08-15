#!usr/bin/env python3

# Preventing from writing Bytecodes
import sys
sys.dont_write_bytecode = True

# Importing The Modules
import pyrebase
import random
import string

# Firebase Configurations
config = {
    "apiKey"        :   "apiKey",
    "authDomain"    :   "projectId.firebaseapp.com",
    "databaseURL"   :   "https://databaseName.firebaseio.com",
    "storageBucket" :   "projectId.appspot.com"
}

# You know what it does :D
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def rnd_gen(i):
    """ Fills up a text control with a random string of length "length" """
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ?" # My Text :P
    text = "".join(random.sample(s, i))
    return text

def sign_up():
    """ Generating Random Users """
    n = 1
    email = rnd_gen(6)
    password = rnd_gen(8)
    auth.create_user_with_email_and_password(email, password)
    user = "[{0}]\tUsername: {1}\n\tPassword: {2}\n"
    print(user.format(n, email, password))

def main(count):
    """ The main Function """
    while count > 0:
        try:
            print("Working")
            sign_up()
            count -= 1
        except:
            break
            sys.exit(0)

if __name__ == "__main__":
    count = int(input("Enter Targeted Number: "))
    main(count)