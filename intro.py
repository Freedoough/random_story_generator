import functions
from main_ import main



def intro(user_name):

    
    
    functions.time_sleep(2, "")
    functions.time_sleep(3, "Welcome to this awesome program!")
    functions.time_sleep(2, "This program generates a random interactive story!")
    functions.time_sleep(3, "Enjoy and have fun :)")

    
    user_name = input("Please enter your name: ").capitalize()
    print("Hello " + user_name + "!")
    
    main()
    return user_name;
    
   
    


    
    