"""
The main purpose of this is to re-implement the player function to a class
"""
import random
from libs.npc import Npc


npc = Npc()

class Player():


    def __init__(self):
        self.name = input(str("Your player name: "))
        self.attacks = {"Basic":10,"Powerfull":50,"Fatal":100}
        self.hp = 100
        self.actions = ['attack', 'defend','heal']

    
    def play(self):

        print(f"Here are the actions you can perform {self.actions}")
        self.choice = input("What actions do you want to perform: ")

        if self.choice.lower() not in self.actions:
            
            print(f"Please make a choice from the actions list {self.actions}")

        elif self.choice.lower() == "attack":

            self.player_attack = random.choice(list(self.attacks)) 
            npc_health = npc.get_hp()

            npc_health -= self.attacks[self.player_attack] # key ==> value 
            
            self.SCORE = self.attacks[self.player_attack] # The score the value of the attack 10,50,100
            
            #print(f'[*] The Score as been update {SCORE}')
            print(f'[*] Attack performed {self.player_attack} attack 🚀')
        
        elif self.choice.lower() == "defend":
            npc_attack = npc.get_attacks()
            
            print(f'[+] The Npc is attacking {npc_attack}')
            
            self.hp -= npc_attack
            print(f'Your HP is {self.hp} ')
            #print(f'The score is: {self.SCORE}')
            
            return npc_attack
        
        else:
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

            # return f'This function is under construction ...🏗️​'
    
    def get_player(self) -> str:
        return f"{self.name}:{self.hp}"
    
class Test():
    """
    Just wanna check how the module importing works
    """
    pass
    
# test = Player()
# test.play()
