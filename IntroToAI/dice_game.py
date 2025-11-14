import random

class Die:
    """Represents a single, standard six-sided die"""

    def __init__(self):
        pass
    
    def roll(self) -> int:
        """Returns random int between 1 and 6"""
        return random.randint(1, 6)


class Player:
    """Represents player with a name and roll value"""

    def __init__(self, name : str, roll_value : int):
        self.name = name
        self.roll_value = roll_value
    
    def roll_die(self, die : Die):
        """Prints number of a rolled die for the player"""
        self.roll_value = die.roll()
        print(f"\n{self.name} rolled a {self.roll_value}")
    

class DiceBattle:
    """Manages the two players and single die for the game"""

    def __init__(self, die : Die, p1_name : str, p2_name : str):
        self.die = die
        self.player1 = Player(p1_name, 0)
        self.player2 = Player(p2_name, 0)
    
    def play(self):
        """Plays one round of dice game"""
        self.player1.roll_die(self.die)
        self.player2.roll_die(self.die)

        if (self.player1.roll_value > self.player2.roll_value):
            print(f"\n{self.player1.name} wins! ")
        elif (self.player1.roll_value < self.player2.roll_value):
            print(f"\n{self.player2.name} wins!")
        else:
            print("\nIt's a draw!")
        
        print("\n---------------------------------------")
    

game : DiceBattle = DiceBattle(Die(), "Jim", "Bob")
game.play()

second_game = DiceBattle(Die(), "Marie", "Antonio")
second_game.play()