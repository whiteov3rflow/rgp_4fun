import random


class Npc():
    
    def __init__(self):
        self.hp = 100
        self.actions = ['attack', 'defend','heal'] 
        self.attacks = {"Basic":10,"Powerfull":50,"Fatal":100}    

    def get_hp(self) -> int:
        """ Getter for the npc hp"""
        #print("[+] Getting the HP of the NPC")
        return self.hp
    
    def get_attacks(self) -> int:
        """
        This function get a random attacks from the dict
        """
        self.attack = random.choice(list(self.attacks.values()))
        return self.attack

    def is_alive(self):
        """
        This function check if the npc is alive or not 
        """
        hp = self.get_hp()
        
        if hp <= 0:
            return False
        else:
            return True

