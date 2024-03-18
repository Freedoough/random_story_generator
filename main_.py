"""
This program is a command line based interactive story generator. 
The purpose of this program is to generate a story for the user that they make choices
for that have different outcomes based on the choices made.
It will utilize file recognition to take pre-written story content and based on conditional statements, will run them accordingly.
"""
import time
import random
import story_content_1
import functions

def intro():

    print("Welcome to this awesome program!")
    time.sleep(2)
    user_name = input("Please enter your name: ").capitalize()
    #figure out time and print functions and pass in data to them
    print("Hello " + user_name + "!")
    
    main()

def main():
    #os.read("story_content_1.py", 'r')
    #figure out syntax for file reading
    time.sleep(2)
    #make the if statements a random number from 1-5
  


    #test 

    choice = input("\nTo start, pick a number from 1 to 5: ")

    if choice == "1":
        print("function 1")
    elif choice == "2":
        print("function 2")
    elif choice == "3":
        print("function 3")
    elif choice == "4":
        print("function 4")
    elif choice == "5":
        print("function 5")
    else:
        print("INVALID")
        time.sleep(2)
        print("Try again...")
        time.sleep(1)
        main()




functions.time_sleep(3, "You stand in front of a tree.")
functions.time_sleep(4, "It's a very big tree.")
story_content_1.test()
intro()

