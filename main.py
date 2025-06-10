import pyfiglet,random,sys
from libs.player import Player
from libs.npc import Npc


class Main():
    """
    The core class of the game which will just start the game and add some features:
    - Displaying the Banner 
    - Next Feature: ??? 
    """

    def __init__(self):

        self.name = input(str("Your player name: "))
        self.START = False

    def Banner(self):

        game_banner = "CONQUERORS"
        ascii_banner = pyfiglet.figlet_format(game_banner)
        print(ascii_banner)

    def Start(self):

        self.Banner()
        self.name = input(str("Your player name: "))
        self.choice = input("Do you wanna start the game ? ")
        
        if self.choice.lower() in ["yes","y"]:
            
            game = Player()
            self.START = True
            
            while self.START:
                game.play()
        else:
            print("Goodbye ^_^")


class GameLogic():
    """
    New class for handling the game logic for a better readable code
    """

    def __init__(self):
        
        self.actions = ["attack", "heal"]
        self.player = Player()
        self.npc = Npc()

    def play(self):
        """
        Main function that handle the game scenario
        """
        self.last_action = ""
        self.npc_turn = False
        self.player_turn = True

        while True:
            print(f"You have a choice between these actions {self.actions}")
            self.choice = input("Please select an action: ")

            if self.choice.lower() not in self.actions:
                print(f"Make a choice from this list {self.actions}")
                continue

            if self.choice == "attack":
                player_attack  = self.player.get_attacks()
                print(f'The player attacks with: {player_attack}')
                self.npc.hp -= player_attack

                if not self.npc.is_alive():
                    print("You won the game!")
                    sys.exit()
                else:
                    self.player_turn = False
                    self.npc_turn = True

            elif self.choice == "heal":
                heal_amount = random.randint(0, 100)
                self.player.hp += heal_amount
                print(f'Your HP has increased by {heal_amount}. Total HP: {self.player.hp}')
                self.player_turn = False
                self.npc_turn = True

            if self.npc_turn:
                npc_attack = self.npc.get_attacks()
                self.player.hp -= npc_attack
                print(f"The NPC attacks! You lose {npc_attack} HP. Your HP: {self.player.hp}")

                if not self.player.is_alive():
                    print("You lost the game.")
                    sys.exit()
                else:
                    self.player_turn = True
                    self.npc_turn = False

if __name__ == '__main__':
    main_game = GameLogic()
    main_game.play()
    # main_game.Start()
