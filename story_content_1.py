#Story 1:
#A maze
import functions
import random
import time

def main():
    functions.loading()

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
    else:
        functions.time_sleep(2, "INVALID...")
        first_branch()

def left_hallway():
    # Skull & crossbones
    functions.time_sleep(5, "You confidently enter the hallway to the left. Ignorant of what might await you.\n")
    functions.time_sleep(4, "As you make your way down the corridor, you notice lights in the distance.\n")
    functions.time_sleep(3, "You approach the lights.\n")
    functions.time_sleep(4, "You hear faint whispers in your ear that makes the hair on the back of your neck stand on end.\n")
    functions.time_sleep(4, "The lights in the distance disappear.\n")
    functions.time_sleep(3, "Your skin crawls..\n")
    functions.time_sleep(4, "You hesitate to go forward, but decide to push on.\n")
    functions.time_sleep(4, "Continuing down the corridor, you eventually reach the end.\n")
    functions.time_sleep(4, "You reach out in front of you, not being able to see anything, and feel another door.\n")
    functions.time_sleep(5, "Opening the door, you're met with a long room.\n")
    functions.time_sleep(4, "You can clearly see giant swinging pendulums that are shaped like hatchets.\n")
    functions.time_sleep(4, "At the opposite end of the room, you see another door, which looks welcoming.\n")
    functions.time_sleep(2, "'The way out?'")
    functions.time_sleep(4, "You whisper to yourself.\n")
    functions.time_sleep(4, "You approach the first set of pendulums cautiously and plan out your next moves carefully.\n")
    
    # First function random event for pendulum room
    def chance_of_survival():
        time.sleep(2)

        chance = input("Enter 'E' to execute: ").capitalize()

        if chance == "E":

            random_num = random.randint(1,20)

            if random_num >= 11:
                left_hallway_survival_success()
            elif random_num <= 10:
                print("FAIL!")
                functions.you_died()
                chance_of_survival()
            else:
                print("INVALID")
                time.sleep(3)
                chance_of_survival()
        else:
            print("INVALID")
            time.sleep(3)
            chance_of_survival()

    chance_of_survival()
# Successful pendulum dodge for random event function
def left_hallway_survival_success():
    # Successful hidden passage code for hidden passage random event function
    def hidden_passage():
        functions.time_sleep(4, "The whole room starts to shake and behind the casket you notice a hole in the floor start to open.\n")
        functions.time_sleep(4, "A moment later, the hole in the ground reveals a staircase made of stone.\n")
        functions.time_sleep(4, "You contemplate going down the dark staircase, but decide to head down.\n")
        functions.time_sleep(4, "")
    # Random event for hidden passage
    def random_event_hidden_passage():
        random_event = input("Enter 'R' for random event chance: ").capitalize()

        if random_event == "R":

            random_num = random.randint(1,20)
        
            if random_num >= 12:
                hidden_passage()
            elif random_num <= 11:
                print("You go back to the main room with the three doors.")
                first_branch()
            else:
                print("INVALID")
                time.sleep(3)
                first_branch()
        else:
            print("INVALID")
            random_event_hidden_passage()
    
    functions.time_sleep(3, "You break into a sprint and carefully dodge each pendulum and make it to the other side.\n")
    functions.time_sleep(4, "As you approach the door, you step on a pressure plate and all the pendulums slowly stop swinging.\n")
    functions.time_sleep(4, "They lift up into the ceiling, out of sight.\n")
    functions.time_sleep(3, "You wonder how this is possible, but turn around and continue on.\n")
    functions.time_sleep(5, "Before you stands the door. You're unaware of what is on the other side.\n")
    functions.time_sleep(4, "You carefully grasp the handle and open it slowly. The hinged creak as you do this as the door appears to be very old.\n")
    functions.time_sleep(5, "Inside the door is yet another room. Quite smaller than the one you were just in.\n")
    functions.time_sleep(5, "In the center of the room you notice what appears to be a marble rectangle of some sort.\n")
    functions.time_sleep(5, "The room appears to be some sort of crypt, with a casket.\n")
    functions.time_sleep(3, "You open the lid.\n")
    # ancient tomb of famous person.. look around for hidden passageway but make it a random chance of finding it.
    functions.time_sleep(5, "As the lid slowly scraped across the top of it, you feel a cold breeze escape the casket.\n")
    functions.time_sleep(3, "You feel chills run down your spine.\n")
    functions.time_sleep(4, "You then look around the room and notice a sign above the casket.\n")
    functions.time_sleep(3, "It reads:\n")
    functions.time_sleep(1, "Arnold Princeton")
    functions.time_sleep(3, "1845-1862\n")
    functions.time_sleep(4, "From the looks of the tomb, he seemed to be a wealthy man...\n")

    random_event_hidden_passage()
    
def left_hallway_survival_failure():
    time.sleep(2)
    functions.time_sleep(4, "You break into a sprint towards the pendulums, trying to time it just right.\n")
    functions.time_sleep(4, "You make it past the first pendulum, you feel so proud of yourself that you lose your focus...\n")
    functions.time_sleep(3, "And therefore, your balance.\n")
    functions.time_sleep(4, "Causing you to trip going into the second pendulum.\n")
    functions.time_sleep(4, "You stumble into its path as you look to it swinging in your direction.\n")
    functions.time_sleep(3, "It's only a split second until you get hit with the pendulum...\n")
    functions.time_sleep(3, "It happens so fast, you can't process it fast enough.\n")
    functions.you_died()
    time.sleep(3)
    # Prompt the user to choose whether they want to try this story again, or go back to the main program file
    # and start another one

def middle_hallway():
    #Ingot
    print("middle")

def right_hallway():
    #Fish
    print("right")















# For debugging purposes
left_hallway_survival_success()
