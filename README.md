    # Dog Calorie Calculator and Tracker
    #### Video Demo:  https://www.youtube.com/watch?v=tTaL5PB3hrU
    #### Description:
    My project is a Calorie Tracker and Calculator for Dogs (well for Humans who have dogs or are interested in the calroie intake of one)

    ##Starting with a global list named dogs:
    this is getting used and alterd by almost every function so I made it a global to be edited and only exported into a csv file once all potential changes to the dogs have been made.

    ## main()
    Creates a csv file if there isnt one allready with headers for proper formating later and checks if there are dogs allready listed in an existing one. If so, it calls list_dogs() and check_action() to show them and ask for the next action. If not it calls make_new() which asks for information for a new dog.

    ## get_name()
    askes for a name as input and checks for alpha and either returns it or promts again with a message. The Name will be used in many functions for formating purposes and readability aswell as creating the dict for each individual dog.

    ## get_weight()
    takes in name for formating and asks to input weight in kg as float for said dog and returns it as float or reprompts with a message showing the user how the input is needed

    ## get_activity()
    has a list with viable activity levels which it prints and then asks for one and checks if given level is viable if so it returns it as string or if not it reprompts with a message asking for one of the given activity levels

    ##clac_kcal()
    has a dict with key:value pairs for multiplayers corresponding to given activity level. It takes in weight and activity level which where asked before and calculates kcal per day based on given weight and multiplayer of the activity level then returns a rounded int

    ##check_action():
    while Loop that askes for input for the next action. it calls the functions according to given input which are N for make_new(), L for list_dogs(), C for change_dog(), D for delete() and E for exit()

    ##make_new()
    calls functions to get name (for formating), weight, activity, kcal and appends dict of dog to global list of dogs, prints confirmation and calls check_action()

    ##list_dogs()
    iterates through global list of dogs and prints stats formated then calls check_action()

    ##change_dog()
    takes name of dog to change, checks imput of what to change, calls functions if necessary, then iterates over dogs, changes as needed and calls check_action()

    ##delete()
    asks if delete all or specific dog and does so in the global list of dogs then calls check_action()

    ##exit()
    writes final list of dogs as dicts to csv and exits the programm


    # Final words
    I hope you enjoy my project. I must say CS50P is a great expierence and i appriciate everthing the CS50 Team have done for new coders like me.


# dog-calorie-calculator
# dog-calorie-calculator
#   c s 5 0 p - f i n a l - p r o j e c t  
 