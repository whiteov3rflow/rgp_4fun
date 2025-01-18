
import random
import pyfiglet


# game name
def Banner():
    game_banner = "GAME OF CONQUERORS"
    ascii_banner = pyfiglet.figlet_format(game_banner)
    print(ascii_banner)


def Start():
     
    Banner()
    # Asking the use if he want to play or not
    choice  =input('Do you want to start the game ? ')
    game = False
    if choice == 'Y' or 'Yes':
        game = True
        while game:
            Initialize()
    else:
        print('Bye Bye ...')

def Initialize():
    """
This is a codebase for the player and the methods used by him

"""
    FLAG = "insec{34sy_7h3_g4m3_w4s_1337}"
    HP = 100
    NPC_HP = 100
    POINTS = 0
    ATTACK_LIMITS = 4
    ACTIONS = ['attack', 'defend','heal']
    PLAYER_ATTACKS = ["Basic","Powerfull","Fatal"]
    START = True
    BANDIT_ATTACKS = ["Basic","Powerfull","Fatal"]
    name = input(str("Type your character name: "))
    print("Welcome player: {}. Try to survive from the Conquerors".format(name))
    while START:
        choice = input(f"What action you want to do from this list: {ACTIONS}: ")
        # the player is choising which action to perform
        if choice in ACTIONS:
            while ATTACK_LIMITS <= 4 and HP <= 100:

                if choice == 'attack':
                    print(f"Here are you attacks list: {PLAYER_ATTACKS}")
                    player_attack = input('Which attack you want to perform: ')
                    if player_attack == PLAYER_ATTACKS[0]:
                        #adding points for player and respectively descrease it from the NPC 
                        NPC_HP -= 10
                        ATTACK_LIMITS -= 1
                        POINTS += 10
                        print("You damage the ennemy with {}".format(PLAYER_ATTACKS[0]))
                        print("Your ennemy have {} HP".format(NPC_HP))
                    elif player_attack == PLAYER_ATTACKS[1]:
                        
                        NPC_HP -= 50
                        ATTACK_LIMITS -= 1
                        POINTS += 50
                        print("You damage the ennemy with {}".format(PLAYER_ATTACKS[1]))
                        print("Your ennemy have {} HP".format(NPC_HP))
                    else:
                        print("You win the game here's the flag :) {}".format(FLAG))
                    break
                    
                #print("Attacking the bandits ")
                #POINTS += 10
            # defining the NPC attack logic
            # todo when defend it's lead to infinite loops
                elif choice == 'defend':
                # getting a random attack for the NPC
                    ennemy_attack = random.choice(BANDIT_ATTACKS)
                    print(f"The bandit is attacking with a: {ennemy_attack} technic")
                    if ennemy_attack == BANDIT_ATTACKS[0]:
                        HP -= 10
                        ATTACK_LIMITS -= 1
                        print("Your HP is {} and you have {} left".format(HP,ATTACK_LIMITS))
                    elif ennemy_attack == BANDIT_ATTACKS[1]:
                        HP -= 50
                        ATTACK_LIMITS -= 1
                        print("Your HP is {} and you have {} left".format(HP,ATTACK_LIMITS))
                    else:
                        print("You lose again the Boss he perform {} attack".format(ennemy_attack[2]))
            else:
                print("Nothing to do yet")
        else:
            print("Please choose an action from the actions list")


    


