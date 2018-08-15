#!usr/bin/env python3

import pyrebase
import random
import string


config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def rnd_gen(i):
    """ Fills up a text control with a random string of length "length" """
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    text = "".join(random.sample(s, i))
    return text

def sign_up():
    n = 1
    email = rnd_gen(6)
    password = rnd_gen(8)
    auth.sign_up_with_email_and_password(email, password)
    user = "[{0}]\tUsername: {1}\n\tPassword: {2}\n"
    print(user.format(n, email, password))

def main(count):
    while count > 0:
        sign_up()
        count -= 1

if __name__ == "__main__":
    count = int(input("Enter Targeted Number: "))
    main(count)