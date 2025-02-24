
import random,pyfiglet, argparse
from libs import npc


# game name
def Banner():
    game_banner = "CONQUERORS"
    ascii_banner = pyfiglet.figlet_format(game_banner)
    print(ascii_banner)

def Start():     
    Banner()
    # Asking the user if he want to play or not
    choice = input('Do you want to start the game ? ')

    if choice.lower() == "y" or "yes" :
        Initialize()
    else:
        print("Good bye")

def Initialize():
    """
This is a codebase for the player and the methods used by him

"""
    SECRET = "Enjoy the moment "
    HP = 100
    NPC_HP = 100
    POINTS = 0
    ATTACK_LIMITS = 0
    ACTIONS = ['attack', 'defend','heal']
    PLAYER_ATTACKS = {"Basic":10,"Powerfull":50,"Fatal":100}
    START = True
    BANDIT_ATTACKS = {"Basic":10,"Powerfull":50,"Fatal":100}
    name = input(str("Type your character name: "))
    print(f"Welcome player: {name}. Try to survive from the Conquerors")
    while START and ATTACK_LIMITS <= 3:
        choice = input(f"What action you want to do from this list: {ACTIONS}: ")
        # the player is choising which action to perform
        if choice == 'attack':
            #while ATTACK_LIMITS <= 3 and NPC_HP :
            print(f"Here are you attacks list: {list(PLAYER_ATTACKS.keys())}")
            player_attack = random.choice(list(PLAYER_ATTACKS.keys()))
            if player_attack:
                #adding points for player and respectively descrease it from the NPC 
                NPC_HP -= PLAYER_ATTACKS[player_attack]
                ATTACK_LIMITS += 1
                POINTS += PLAYER_ATTACKS[player_attack]
                print(f"You damage the ennemy with {player_attack} attack 🚀​")
                print(f"Your ennemy have {NPC_HP} HP")
                if NPC_HP <= 0:
                    print(f"You won the game is a quotes {SECRET}")
                    break
                else:
                    pass
            else:
                print("Please choose an attack 🦂​")
                break
            # To-Do: re-implement this as a function and import it 
        elif choice == "defend":
            ennemy_attack = random.choice(list(BANDIT_ATTACKS.keys())) # get the key from the bandit_attacks dict
            retrieve_healh = BANDIT_ATTACKS[ennemy_attack]  # store ennemy_attack key value and deduct it from player_hp
            HP -= retrieve_healh
            if HP > 0:
                print(f"Your HP is {HP} and the bandits hit you with {ennemy_attack} attack 🦂 ")
            else:
                print(f"The bandit performed {ennemy_attack} attack 🦂 and your HP is {HP}")
                break
                
        elif choice == 'heal':
             print('This function is under construction... 🏗️​')
        else:
            START = False

    else:
        pass