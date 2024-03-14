"""
This program is a command line based interactive story generator. 
The purpose of this program is to generate a story for the user that they make choices
for that have different outcomes based on the choices made.
It will utilize file recognition to take pre-written story content and based on conditional statements, will run them accordingly.
"""
import time
import random
import math
import os

def intro():

    print("Welcome to this awesome program!")
    time.sleep(2)
    user_name = input("Please enter your name: ").capitalize()
    
    print("Hello " + user_name + "!")

    main()

def main():
    os.read("story_content_1.py", 'r')

intro()
