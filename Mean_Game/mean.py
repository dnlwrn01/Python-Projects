#
#  Python: 3.6.4
#
#  Author: Daniel Warren
#
#   Purpose: Nice / Mean Chose Your Own Adventure Game
#
#

from colorama import init

def start(nice=0, mean=0, name=""):
    #get users name
    name = describe_game(name)
    nice,mean,name = nice_mean (nice,mean,name)

def describe_game(name):
    """
        check if this is a new game or not.
        If new game, get users name.
        If !new game thank user for playing again, and continue
    """
    #meaning, if we do not already have this users name,
    #then they are a new player and we need to get their name
    if name != "":
        print(f"\nThank You for playing again, {name}!")
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print (Fore.BLUE + f"\nWelcome, {name}!")
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches for a \nconversation. Will you be nice \nor mean? (N/M) \n>>> ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice +1)
            stop = False
        if pick == "m":
            print("\nThe strangerstares at you \nmenacingly and storms off...")
            mean = (mean +1)
            stop = False
    
    score(nice,mean,name) # pass the 3 variables to score()

def show_score(nice,mean,name):
    print(f"\n{name}, your current total: \n{nice} nice and {mean} mean.")


def score(nice,mean,name):
    # score fucnction os being passed the values stored within 3 variables
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print(f"\nNice job {name}, you WIN! \nEveryone loves you and you've \nmade lots of friends along the way!")
    again(nice,mean,name)

def lose(nice,mean,name):
    print(f"\nAhhh, game over {name}, you LOSE! \nYou are destined to be alone forever. That's called karma, {name}. Karma...")
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:        
        choice = input("\nDo you want to play again? (y/n):\n>>> ")
        if choice == 'y' or choice == 'Y':
            stop = False
            reset(nice,mean,name)
            
        if choice == 'n' or choice == 'N':
            print(f"\nOh, sad to see you go {name}")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO': \n>>> ")

def reset(nice,mean,name):
          nice = 0
          mean = 0
          start(nice,mean,name)
            



if __name__ == "__main__":
    start()
