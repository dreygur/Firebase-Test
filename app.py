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
    "apiKey"        :   "AIzaSyCRJyJU8cXuApBmX9kFmrLCYnzJF3ztK64",
    "authDomain"    :   "transport-tracker-56d6b.firebaseapp.com",
    "databaseURL"   :   "https://transport-tracker-56d6b.firebaseio.com",
    "storageBucket" :   "transport-tracker-56d6b.appspot.com"
}
apiKey      = "AIzaSyCRJyJU8cXuApBmX9kFmrLCYnzJF3ztK64" # Your API key
projectID   = "transport-tracker-56d6b"                 # Your Project ID

# You know what it does :D
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def rnd_gen(i):
    """ Fills up a text control with a random string of length "length" """
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ?" # My Text :P
    text = "".join(random.sample(s, i))
    return text

def sign_up(n):
    """ Generating Random Users """
    email = rnd_gen(6)  + "@playlagom.com"
    password = rnd_gen(8)
    auth.create_user_with_email_and_password(email, password)
    user = "[{0}]\tUsername: {1}\n\tPassword: {2}\n"
    print(user.format(n, email, password))

def main(count):
    """ The main Function """
    n = 1
    while count > 0:
        try:
            sign_up(n)
            count -= 1
            n += 1
        except:
            break

if __name__ == "__main__":
    count = int(input("Enter Targeted Number: "))
    main(count)