"""
The main purpose of this is to re-implement the player function to a class
This need to be change so it's only handle the player logic.
"""
import random,sys


class Player():


    def __init__(self):
        self.attacks = {"Basic":10,"Powerfull":50,"Fatal":100}
        self.hp = 100

    def get_attacks(self):
        """
        This function get a random attacks from the dict
        """

        self.attack = random.choice(list(self.attacks.values())) 
        
        return self.attack
    
    def get_hp(self):
        """
        Getter for player HP
        """  
        return self.hp

    def is_alive(self):
        """
        This function check if the player is alive or not 
        """
        hp = self.get_hp()

        if hp <= 0:
            return False
        else:
            return True

