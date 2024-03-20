#Story 1:
#A maze
import functions
import random
import time

def main():
    i = 0

    while i < 5:

        functions.time_sleep(.75, "LOADING...\n")

        i += 1

    time.sleep(2)
    functions.time_sleep(4, "You're walking in a tall grass field...\n")
    functions.time_sleep(4, "You can barely see above the grass.\n")
    functions.time_sleep(4, "You can make out a treeline in the distance.\n")
    functions.time_sleep(4, "You advance toward it.\n")
    functions.time_sleep(4, "As you enter the dense forest, you see a peculiar object sticking out of the ground.\n")
    functions.time_sleep(4, "You approach the object with uncertainty.\n")
    functions.time_sleep(4, "You can now make out what appears to be a large branch with a skull on top.\n")
    functions.time_sleep(4, "Your gut wrenches in disgust.\n")
    functions.time_sleep(4, "You turn around and take one step away from it.\n")
    functions.time_sleep(3, "Suddenly, the ground beneath you breaks.\n")
    functions.time_sleep(3, "It's as if you stepped on some sort of hole covered by leaves and branches.\n")
    functions.time_sleep(2, "You fall down the hole...\n")
    functions.time_sleep(.5, "\n")
    functions.time_sleep(.5, "\n")
    functions.time_sleep(1, "You hit the bottom of the pit. Landing on a pile of dirt, borderline unharmed.\n")
    functions.time_sleep(5, "It's dark. The only light that seeps through comes from the hole you fell down above you.\n")
    functions.time_sleep(4, "You think to yourself: 'I must find a way out of here'.\n")
    functions.time_sleep(4, "The only way forward is straight. Despite the darkness, you head forward through the tunnel.\n")
    functions.time_sleep(4, "You start making your way through.\n")
    functions.time_sleep(5, "As you step forward you bang your head into a metal, vault-like door you failed to see.\n")
    functions.time_sleep(4, "You step back and feel the circular vault knob thing.\n")
    functions.time_sleep(3.5, "And attempt to open it.\n")
    functions.time_sleep(4, "As you turn the knob, it slowly gives way and starts to turn, releasing the door.\n")
    functions.time_sleep(4, "It takes an immense amount of effort, but it opens and squeaks as it opens and reveals what's on the other side.\n")
    functions.time_sleep(5, "Inside the door is a room, about the size of a High School classroom, lit by torches.\n")
    functions.time_sleep(4, "Taking one step inside the room, the door shuts behind you..\n")
    functions.time_sleep(2, "Ominously...\n")
    functions.time_sleep(4, "You notice three hallways on the far wall of the room. All of which have signs above them.\n")
    functions.time_sleep(5, "Out of curiousity, you approach the wall to get a better look.\n")
    functions.time_sleep(4, "The sign above the left hallway has an crude drawing of a skull and crossbones.\n")
    functions.time_sleep(4, "The sign above the middle hallway has another drawing of what appears to be an ingot of some kind.\n")
    functions.time_sleep(4, "Finally, the sign above the right hallway has a drawing of a very basic fish. Something like a kindergartener would draw.\n")

    first_branch()

def first_branch():
    
    user_choice = input("Which hallway do you go down? (left/middle/right): ").capitalize()

    if user_choice == "Left":
        left_hallway()
    elif user_choice == "Middle":
        middle_hallway()
    elif user_choice == "Right":
        right_hallway()

def left_hallway():
    print("left")

def middle_hallway():
    print("middle")

def right_hallway():
    print("right")

