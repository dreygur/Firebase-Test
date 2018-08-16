#!usr/bin/env python3

"""
Copyleft
Author: Rakibul Yeasin Totul (fb.com/rytotul)
For Fun Purpose don't take seriously...
"""

# Preventing from writing Bytecodes
import sys
sys.dont_write_bytecode = True

# Importing The Modules
import pyrebase
import random
import string

# Firebase Configurations
apiKey      = "AIzaSyCRJyJU8cXuApBmX9kFmrLCYnzJF3ztK64" # Your API key
projectID   = "transport-tracker-56d6b"                 # Your Project ID

# Don't Edit Here...
authDomain      = "{0}.firebaseapp.com".format(projectID)
databaseURL     = "https://{0}.firebaseio.com".format(projectID)
storageBucket   = "{0}.appspot.com".format(projectID)

config = {
    "apiKey"        :   apiKey,
    "authDomain"    :   authDomain,
    "databaseURL"   :   databaseURL,
    "storageBucket" :   storageBucket
}

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
    return user.format(n, email, password)

def main(count):
    """ The main Function """
    n = 1
    with open('credentials.txt', "w") as f:
        while count > 0:
            try:
                f.write(sign_up(n))
                count -= 1
                n += 1
            except:
                break

if __name__ == "__main__":
    count = int(input("Enter Targeted Number: "))
    main(count)