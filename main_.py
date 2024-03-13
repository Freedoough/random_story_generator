import time
import random

def main():
    
    print("Hello!")
    time_()
    #print_("Welcome to this program!\n")

    user_name = input("Please enter your name: ").capitalize()
    intro(user_name)

def intro(user_name):
    print("Hello" + user_name + " welcome!")

def time_():
    time.sleep(3)
def print_(text):
    print
main()