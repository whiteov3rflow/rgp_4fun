# import player
import random

class Npc():
    
    def __init__(self):
        self.hp = 100
        self.attacks = {"Basic":10,"Powerfull":50,"Fatal":100}    

    def get_hp(self) -> int:
        """ Getter for the npc hp"""
        #print("[+] Getting the HP of the NPC")
        return self.hp
    
    def get_attacks(self) -> int:
        """
        This function get a random attacks from the dict
        """
        return random.choice(list(self.attacks.values()))
 

# npc = Npc()
