#Story 1:
#A maze
import functions
import random
import time
from intro import intro
import main_


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
    functions.time_sleep(5, "Finally, the sign above the right hallway has a drawing of a very basic fish. Something like a kindergartener would draw.\n")

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
        functions.time_sleep(4, "You contemplate going down the dark staircase, and decide to head down.\n")
        functions.time_sleep(4, "Going down the first few steps, the path quickly turns to the right and turns into a spiral staircase.\n")
        functions.time_sleep(4, "At the very bottom, about 2 flights worth of steps, you can see a light flickering.\n")
        functions.time_sleep(3, "You make your way down.\n")
        functions.time_sleep(4, "At the bottom, you follow the light down a single hallway.\n")
        functions.time_sleep(4, "Down the hallway, you walk into a room.\n")
        functions.time_sleep(3, "You can't believe your eyes.\n")
        functions.time_sleep(.5, "\n")
        functions.time_sleep(.5, "\n")
        functions.time_sleep(4, "Inside the room lies hidden treasures the likes of which you've never seen before.\n")
        functions.time_sleep(4, "Gold, Diamonds, Pearls, Jewelery and so much more!\n")
        functions.time_sleep(4, "You contemplate stuffing your pockets for when you escape...\n")

        greed = input("Do you stuff your pockets? (Y/N):").capitalize()


        if greed == "Y":
            # The treasure is booby trapped and the room collapses when it detects the weight of the treasure get moved/removed
            functions.time_sleep(4, "You're a greedy human.\n")
            functions.time_sleep(4, "You make your way back to the main room.\n")
            functions.time_sleep(.5, "\n")
            functions.time_sleep(.5, "\n")
            first_branch()
        elif greed == "N":
            functions.time_sleep(4, "You're a good human.\n")
            functions.time_sleep(4, "You make your way back to the main room.\n")
            functions.time_sleep(.5, "\n")
            functions.time_sleep(.5, "\n")
            first_branch()
        else:
            print("INVALID")
            time.sleep(4)
            print("You head back to the main room.\n")
            time.sleep(3)
            first_branch()




    # Random event for hidden passage
    def random_event_hidden_passage():
        random_event = input("Enter 'R' for random event chance: ").capitalize()

        if random_event == "R":

            random_num = random.randint(1,20)
        
            if random_num >= 12:
                hidden_passage()
            elif random_num <= 11:
                print("You go back to the main room with the three doors.\n")
                time.sleep(4)
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
    functions.time_sleep(5, "As the lid slowly scraped across the top of it, you feel a cold breeze escape the casket.\n")
    functions.time_sleep(3, "Chills run down your spine.\n")
    functions.time_sleep(4, "You then look around the room and notice a sign above the casket.\n")
    functions.time_sleep(3, "It reads:\n")
    # Make the name of the sign say the user's name somehow
    functions.time_sleep(1, "Arnold Princeton\n")
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

    def minecart_enter():

        minecart_choice = input("Get in the minecart? (Y/N): ").capitalize()

        if minecart_choice == "Y":
            minecart_ride()
        elif minecart_choice == "N":
            print("\n")
            functions.time_sleep(4, "You refuse to enter the cart. Just staring at it.\n")
            functions.time_sleep(4, "You then feel a pull towards the cart.\n")
            functions.time_sleep(4, "You hear it beckoning to you.\n")
            functions.time_sleep(4, "Unable to control yourself, you enter the cart.\n")
            minecart_ride()
        else: 
            functions.time_sleep(4, "INVALID")
            functions.time_sleep(2, "\n")
            minecart_enter()

    def minecart_ride():

        def ride_continues():
            #user continues down minecart track
            functions.time_sleep(4, "After that close encounter, you and the cart continue down the tracks.\n")
            functions.time_sleep(3, "They lead out of the lava room.\n")
            functions.time_sleep(3, "Visibility diminishes as you travel away from the lava room.\n")
            functions.time_sleep(3, "The only way of knowing where you're going is purely based on the feeling of the minecart.\n")
            functions.time_sleep(3, "The tracks suddenly drop, same with your stomach as it would on a roller coaster.\n")
            functions.time_sleep(3, "You pick up speed...\n")
            functions.time_sleep(2, "So much speed...\n")
            functions.time_sleep(1, "TOO MUCH speed!\n")
            functions.time_sleep(2, "The bottom of the drop approaches and it quickly levels out.\n")
            functions.time_sleep(3, "Going an ungodly speed in a dark mineshaft, you feel the cart follow the tracks left.\n")
            functions.time_sleep(3, "And then right.\n")
            functions.time_sleep(2, "You fear for your life.\n")
            functions.time_sleep(3, "The tracks suddenly go uphill.\n")
            functions.time_sleep(3, "The cart loses speed as you approach the crest of the hill.\n")
            functions.time_sleep(3, "At the end of the tracks, the cart comes to a stop against a track buffer.\n")
            functions.time_sleep(3, "Your cart ends up at the end of another dark tunnel.\n")
            functions.time_sleep(3, "With zero hesitation, you exit the cart.\n")
            functions.time_sleep(3, "You make your way down the tunnel, once again.\n")
            functions.time_sleep(4, "You become anxious for what seems like zero reason.\n")
            functions.time_sleep(4, "Your heart rate increases, and sweat beads manifest on your skin.\n")
            functions.time_sleep(5, "Eventually reaching the end of the long straight tunnel, ignoring the signs your body is telling you.\n")
            functions.time_sleep(4, "The end of the tunnel reveals another large, spherical room. About the size of a small apartment.\n")
            functions.time_sleep(4, "You enter the room, barely being able to see your hands in front of you.\n")
            functions.time_sleep(4, "As you make your way towards the center, you kick something with your foot.\n")
            functions.time_sleep(4, "Out of curiousity and ignorance, you reach down to pick up the object to try and identify it.\n")
            functions.time_sleep(4, "Upon very close examination, about as close as you can get with the visibility; you discover that it's a bone.\n")
            functions.time_sleep(3, "Who knows what type of animal it came from.\n")
            functions.time_sleep(4, "Perhaps a human...\n")
            functions.time_sleep(4, "While you're inspecting the bone, an ominous sound eminates from behind you.\n")
            functions.time_sleep(4, "You turn around slowly...\n")
            functions.time_sleep(3, "The ground begins to shake beneath your feet.\n")
            functions.time_sleep(4, "A small glimmer of light emerges out of nowhere from a huge hole in the wall right next to where you came in.\n")
            functions.time_sleep(4, "It appears to be some sort of cave, not part of the mineshaft.\n")
            functions.time_sleep(4, "A large, humanoid creature emerges from behind the light, making the ground rumble with every step.\n")
            
            functions.time_sleep(4, "")
            
            # Figure out ending:
            # An unknown creature is lurking deep in the mineshaft,
            # the user has an encounter with the creature and the storyline ends with either 
            # being killed by the creature or by the creature causing a collapse of the mineshaft, killing
            # both the creature and the user
            # after death or either outcome, prompt the user to replay the program to get a different story


        def lava_dodge_success():
            # user dodges lava plume
            
            functions.time_sleep(3, "\nYou lean your body weight to one side of the cart.\n")
            functions.time_sleep(4, "The cart leans on two wheels as the lava plume shoots straight up.\n")
            functions.time_sleep(3, "It successfully misses the cart!\n")
            ride_continues()


        def lava_dodge_fail():
            functions.time_sleep(1, "Unfortunately, you weren't able to dodge the lava plume.\n")
            functions.time_sleep(3, "In the split second of you attempting to dodge it, your cart gets hit.\n")
            functions.time_sleep(3, "Instantly, the cart melts from the intense heat.\n")
            functions.time_sleep(2, "You have zero time to comprehend what is happening as you evaporate in the blink of an eye.")

            functions.you_died()



        def lava_dodge():

            functions.time_sleep(1, "QUICK!")

            dodge = input("PRESS 'S' TO AVOID THE LAVA:").capitalize()

            chance = random.randint(1, 12)

            if chance >= 7:
                lava_dodge_success()
            elif chance <=6:
                lava_dodge_fail()



        functions.time_sleep(3, "After entering the cart, it starts to roll down the tracks.\n")
        functions.time_sleep(3, "The torches on the wall disappear after a few hundred feet.\n")
        functions.time_sleep(4, "The cart continues to roll down the tracks, going deeper and deeper into the mine.\n")
        functions.time_sleep(4, "You roll through an opening into a pretty big room, about the size of a football field.\n")
        functions.time_sleep(4, "The room is brightly lit. You hesitate to look down, but do it anyway.\n")
        functions.time_sleep(3, "Below you, about 200 feet down is a giant lava pit.\n")
        functions.time_sleep(4, "As you roll down the rails, losing speed, you hear the pit below you rumble...\n")
        functions.time_sleep(4, "Suddenly, you notice a giant stream of lava start to burst up straight towards your cart.\n")
        functions.time_sleep(4, "You have little time to react. You need to act fast.\n")
        
        lava_dodge()
     
    time.sleep(2)
    functions.time_sleep(4, "You hastily enter the middle hallway.\n")
    functions.time_sleep(4, "The hallway starts moving down, like a ramp.\n")
    functions.time_sleep(4, "The path narrows slightly as you move forward and flattens out after a little bit.\n")
    functions.time_sleep(4, "You can make out metal beams on the ground, like some sort of rail system.\n")
    functions.time_sleep(4, "Torches on the wall light the way.\n")
    functions.time_sleep(4, "You then notice wooden support beams surrounding the entirety of the hallway and intermittently in the distance.\n")
    functions.time_sleep(3, "You're in an abandoned mineshaft...\n")
    functions.time_sleep(3, "You hear rumbling in the distance.\n")
    functions.time_sleep(3, "It appears to be getting closer.\n")
    functions.time_sleep(3, "A lone minecart rolls in your direction from the distance.\n")
    functions.time_sleep(4, "It comes to a stop in front of you.\n")
    
    minecart_enter()



    


def right_hallway():
    #Fish
    # have this be the way out
    print("right")


# For debugging purposes
#middle_hallway()
