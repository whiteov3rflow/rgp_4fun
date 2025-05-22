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
    
    def set_hp(self,hp):
        """Setter for the npc hp"""
        self.hp += hp
        return self.hp
    
    def get_attacks(self) -> int:
        """
        This function get a random attacks from the dict
        """
        self.attack = random.choice(list(self.attacks.values()))
        return self.attack
    
    # def get_actions(self) -> str:
    #     return random.choice(self.actions) #return a random actions betwen "attack,defend,heal"

    # def turn(self):

    #     hp = self.get_hp()
    #     if hp < 50:
    #         self.set_hp(10)
    #         return self.set_hp(10)
        
    #     elif hp >= 50 and hp < 80:
    #         return self.get_attacks()
        
        
npc = Npc()
