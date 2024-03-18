"""
This program is a command line based interactive story generator. 
The purpose of this program is to generate a story for the user that they make choices
for that have different outcomes based on the choices made.
It will utilize file recognition to take pre-written story content and based on conditional statements, will run them accordingly.
"""
import time
import random
import story_content_1
import story_content_2
import story_content_3
import story_content_4
import story_content_5
import functions

def intro():

    print("Welcome to this awesome program!")
    time.sleep(2)
    user_name = input("Please enter your name: ").capitalize()
    print("Hello " + user_name + "!")
    
    main()

def main():
    # These two lines are for reference
    #functions.time_sleep(3, "You stand in front of a tree.")
    #functions.time_sleep(4, "It's a very big tree.")
  

    generate = input("\nTo start, enter 'N' to generate a story: ").capitalize()

    if generate == "N":
        
        num_random = random.randint(1,5)

        if num_random == 1:
            print("function 1")
        elif num_random == 2:
            print("function 2")
        elif num_random == 3:
            print("function 3")
        elif num_random == 4:
            print("function 4")
        elif num_random == 5:
            print("function 5")
        else:
            print("INVALID")
            time.sleep(2)
            print("Try again...")
            time.sleep(1)
            main()
    else:
        functions.time_sleep(1, "INVALID")
        functions.time_sleep(2, "Try again...")
        main()


# This line below is for reference
#story_content_1.test()
intro()

