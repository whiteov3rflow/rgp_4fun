import pyfiglet
from libs.class_player import Player



class Main():
    """
    The core class of the game which will just start the game and add some features:
    - Displaying the Banner 
    - Next Feature: Pending 
    """

    def __init__(self):
        self.START = False

    def Banner(self):
        game_banner = "CONQUERORS"
        ascii_banner = pyfiglet.figlet_format(game_banner)
        print(ascii_banner)

    def Start(self):
        self.Banner()
        self.choice = input("Do you wanna start the game ? ")
        
        if self.choice.lower() in ["yes","y"]:
            
            game = Player()
            self.START = True
            
            while self.START:
                game.play()
        else:
            print("Goodbye ^_^")




if __name__ == '__main__':
    main_game = Main()
    main_game.Start()
