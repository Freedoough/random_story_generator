import time

# Time sleep function with message and time arguments
def time_sleep(_time, message):
    print(message)
    time.sleep(_time)



# You died function to be called
def you_died():
    n = 0

    while n < 10:
        n += 1
        time.sleep(.75)
        print("\n")

    print("...YOU DIED...")

    x = 0

    while x < 10:
        x += 1
        time.sleep(.75)
        print("\n")

def loading():
    i = 0

    while i < 5:

        time.sleep(.5)
        print("LOADING...\n")

        i += 1

      
    print("done!")
loading()

