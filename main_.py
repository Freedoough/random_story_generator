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
import intro


def main():
    # These two lines are for reference
    #functions.time_sleep(3, "You stand in front of a tree.")
    #functions.time_sleep(4, "It's a very big tree.")
    
    #Run the intro function and assign return value to user_name
    user_name = intro.intro()
    print ("User name - " + user_name + " - from intro file function in main")

    story_content_1.main(user_name)

    #Could alternatively skip variable assignment and put the intro call directly in the print statement
    #print ("User name - " + intro.intro() + " - from intro file function in main")

    generate = input("\nTo start, enter 'N' to generate a story: ").capitalize()

    if generate == "N":
        
        # number range set to 1-1 for debugging SC1 purposes
        num_random = random.randint(1, 1)

        if num_random == 1:
            story_content_1.main(user_name)
        elif num_random == 2:
            story_content_2.main()
        elif num_random == 3:
            story_content_3.main()
        elif num_random == 4:
            story_content_4.main()
        elif num_random == 5:
            story_content_5.main()
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


main()

# This line below is for reference
#story_content_1.test()

#Turn this file into "driver file"
#Perhaps make a new branch and try it that way
#finish first story before attempting this