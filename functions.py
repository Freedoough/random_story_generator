import time
def time_sleep(_time, message):
    print(message)
    time.sleep(_time)




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

