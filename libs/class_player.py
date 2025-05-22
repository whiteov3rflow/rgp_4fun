"""
The main purpose of this is to re-implement the player function to a class
"""
import random,sys
from libs.npc import Npc


npc = Npc()

class Player():


    def __init__(self):
        self.name = input(str("Your player name: "))
        self.attacks = {"Basic":10,"Powerfull":50,"Fatal":100}
        self.hp = 100
        self.actions = ['attack', 'defend','heal', 'quit']
        self.last_action = ""
        self.turn_count = 0



    def get_attacks(self):
        """
        This function get a random attacks from the dict
        """

        self.attack = random.choice(list(self.attacks)) 
        
        return self.attack
    
    def play(self):

        print(f"Here are the actions you can perform {self.actions}")
        self.choice = input("What actions do you want to perform: ")
        # set a variable to track the last action of the player
        self.last_action = self.choice

        if self.choice.lower() not in self.actions:
            
            print(f"Please make a choice from the actions list {self.actions}")

        elif self.choice.lower() == "attack":

            self.player_attack = self.get_attacks() 
    
            npc_health = npc.get_hp()

            npc_health -= self.attacks[self.player_attack] # return the key ==> value 
            #print(f'{npc_health}')
            
            if npc_health <= 0:
                print("You won the game !! ")
                sys.exit() # exit the game since the player won

            self.SCORE = self.attacks[self.player_attack] # The score the value of the attack 10,50,100
            
            
            #print(f'[*] The Score as been update {SCORE}')
            print(f'[+] Attack performed {self.player_attack} attack 🚀\n')
        
        elif self.choice.lower() == "defend":
            npc_attack = npc.get_attacks()
            
            print(f'[+] The Enemy hit you with {npc_attack} points of damage')
            
            self.hp -= npc_attack
            if self.hp <= 0:
                print("You die by KO")
                sys.exit()
            print(f'Your HP is {self.hp} ')
            #print(f'The score is: {self.SCORE}')
            
            return npc_attack
        
        elif self.choice.lower() == "heal":
            """
            The last choice of the player. So when a player decided to heal what can we do ? what are the conditions ? 
            Can we heal before without receiving a damage ?  
            """
            if self.hp == 100:
                print(f"You can't heal your HP is: {self.hp}")
            
            else:
                heal_amount = random.randint(10,90)
                self.hp += heal_amount

                if self.hp > 100:

                    self.hp = 100
                    print(f'Your HP is now: {self.hp}')
                else:
                    print(f"Your HP is now: {self.hp}")
        else:
            sys.exit()
        
        self.turn_count +=1

        #print(f"It's been: {self.turn_count} turn")

        if self.turn_count >= 1:
            self.npc_turn()
        
    def npc_turn(self):
        npc_health = npc.get_hp()
        
        if npc_health < 30:
            print('The ennemy looks desperate')
        
        elif self.last_action == "heal":
            print("The ennemy sees an opening")
            npc_attack = npc.get_attacks()
            print(f'The ennemy just attacks you for {npc_attack}')
            self.hp -= npc_attack
        else:

            npc_attack = npc.get_attacks()
            print(f'The ennemy just attacks you for {npc_attack}')

            self.hp -= npc_attack

        if self.hp <= 0:
            print("You die by KO")
            sys.exit()
    
    def get_player(self) -> str:
        return f"{self.name}:{self.hp}"
