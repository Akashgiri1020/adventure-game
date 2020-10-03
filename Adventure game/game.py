import time
import random


weapon = random.choice([" Mjölnir hammer","storm breaker"])
items = []
stone=[]


def print_pause(string):
    print(string)
    time.sleep(2)


def restart_game():
    if weapon in items:
        items.remove(weapon)
    print_pause("GAME OVER\n")
    response = input("Would you like to play again yes or no?\n")
    if "yes" in response:
        adventure_game()
    elif "no" in response :
        print_pause("Thanks for playing this game! See you next time.")
    else:
        print_pause("I will ask you again")
        restart_game()


def intro():
    print_pause("you are Salman bhai ")
    print_pause("You find yourself standing in asgard")
    print_pause("The place is very deserted")
    print_pause(f"Rumor has it that Loki the magician is live inside a palace, "
                "and has been terrifying the  neraby planets.")
    print_pause("after sometime,you find out the loki's palace.")
    print_pause("and your aim is to kill loki the magician who want to become GOD")
    print_pause("but you have only a dagger which is not affect the loki\n")
    print_pause(f"Loki is only kill by a {weapon} that is  hide by  Reality stone")
    print_pause("which is hide in asgardian secure house : Oregan")
    print_pause("reality stone is used to change the reality for other persons")
    print_pause("so you have two options:")
    
                


def asgard():
    # when player thinks what he do next
    print_pause(f"Enter 1 to enter in the palace.")
    print_pause("Enter 2 Find the reality stone.")
    print_pause("what would you like to do?")
    response = (input("(please enter 1 or 2).\n"))

    
    if "reality stone" in stone:
        print_pause("finally you got stone and use it to see reality")
        print_pause(f"you use it and take {weapon}")
        items.append(weapon)
    else:
        print("you have not reality stone")
    if response == '1':
        palace()
    elif response == '2':
        oregan()
    else:
        print("plz choose 1 or 2 nothing else")
        asgard()
    


def palace():
    # Things that happen to the player in the house.
    print_pause("You entered in the palace.")
    print_pause("You put your dagger on guard's neck"
                "And ask! where is the loki?")
    print_pause("And then enter in loki's room")

    if weapon in items:
        print_pause("As the loki moves to attack, ")
        print_pause(f"you unsheath your new {weapon}.")
        print_pause(f"The {weapon} with full of thunder "
                    "you and your weapon is ready to attack.")
        print_pause("But the loki takes one look at "
                    "your new weapon and surprised")
        print_pause("And loki use unlish power and attack on you"
                    "suddenly you use realitiy and change the reality")
        print_pause("and failed the power of loki")
        print_pause(f"and then he use his {weapon} and defeat him")
        restart_game()

    elif weapon not in items:
        print_pause("As loki moves to attack")
                    
        response = input("Would you like to (1) fight or (2) run away?\n")

        if response == '1':
            print_pause("you face loki with  dagger")
            print_pause("finally loki defeat you.")
            print_pause("You have been defeated!")
            restart_game()

        elif response == '2':
            print_pause("You run back outside the palace. Luckily, "
                        "you don't seem to have been followed.\n")
            asgard()


def oregan():
    # Things that happen to the player goes in the forest
    if weapon in items:
        print_pause("finally you findout the oregan in asgard.")
        print_pause("You go cautiously into oregan.")
        print_pause("You've been here before, and gotten reality stone "
                    "the good stuff. It's just an empty  now.")
        print_pause("You walk back out from oregan.")
        asgard()
    else:
        print_pause("You go cautiously into the oregan.")
        print_pause("finally you see reality stone inside the oregan")
        print_pause("you see that it is fantastic made")
        print_pause("take the reality stone with you.")
        print_pause("You walk back out from oregan.\n")
        stone.append("reality stone")
        asgard()


def adventure_game():
    intro()
    asgard()


adventure_game()
