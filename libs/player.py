
import random,pyfiglet, argparse


# game name
def Banner():
    game_banner = "CONQUERORS"
    ascii_banner = pyfiglet.figlet_format(game_banner)
    print(ascii_banner)


def Start():
     
    Banner()
    # Asking the use if he want to play or not
    choice  =input('Do you want to start the game ? ').lower()
    if choice in ['Y','Yes', 'y', 'yes'] :
        Initialize()
    else:
        print("Good bye")

def get_args():
    """
    This function define the how the arguments should be parsed
    """
    parser = argparse.ArgumentParser(
        prog=''
    )
            
def Initialize():
    """
This is a codebase for the player and the methods used by him

"""
    FLAG = "insec{34sy_7h3_g4m3_w4s_1337}"
    HP = 100
    NPC_HP = 100
    POINTS = 0
    ATTACK_LIMITS = 0
    ACTIONS = ['attack', 'defend','heal']
    PLAYER_ATTACKS = ["Basic","Powerfull","Fatal"]
    START = True
    BANDIT_ATTACKS = ["Basic","Powerfull","Fatal"]
    name = input(str("Type your character name: "))
    print("Welcome player: {}. Try to survive from the Conquerors".format(name))
    while START:
        choice = input(f"What action you want to do from this list: {ACTIONS}: ")
        # the player is choising which action to perform
        if choice == 'attack':
            #while ATTACK_LIMITS <= 4 and NPC_HP :
            print(f"Here are you attacks list: {PLAYER_ATTACKS}")
            player_attack = input('Which attack you want to perform: ')
            if player_attack == PLAYER_ATTACKS[0]:
                #adding points for player and respectively descrease it from the NPC 
                NPC_HP -= 10
                ATTACK_LIMITS += 1
                POINTS += 10
                print("You damage the ennemy with {}".format(PLAYER_ATTACKS[0]))
                print("Your ennemy have {} HP".format(NPC_HP))
            elif player_attack == PLAYER_ATTACKS[1]:            
                NPC_HP -= 50
                ATTACK_LIMITS += 1
                POINTS += 50
                print("You damage the ennemy with {}".format(PLAYER_ATTACKS[1]))
                print("Your ennemy have {} HP".format(NPC_HP))
            else:
                print("Please choose an attack")
                break
            # defining the NPC attack logic
            # todo when defend it's lead to infinite loops
        elif choice == 'defend':
                # getting a random attack for the NPC
            ennemy_attack = random.choice(BANDIT_ATTACKS)
            print(f"The bandit is attacking with a: {ennemy_attack} technic")
            if ennemy_attack == BANDIT_ATTACKS[0]:
                HP -= 10
                ATTACK_LIMITS += 1
                print("Your HP is {} and you have {} left".format(HP,ATTACK_LIMITS))
            elif ennemy_attack == BANDIT_ATTACKS[1]:
                HP -= 50
                ATTACK_LIMITS += 1
                print("Your HP is {} and you have {} left".format(HP,ATTACK_LIMITS))
            elif HP == 0:
                print('You lose the game ')
            else:
                print("You lose again the Boss he perform {} attack".format(ennemy_attack[2]))
                START = False
        
        elif choice == 'heal':
             print('This function is under construction...')
        else:
            START = False
    else:
        pass


    


