import printspeed

class Annoyance:
    def __init__(self):
        self._name = "name"
        self._age = 0
        self._level : float = 0
        self._cur_annoyances : list[str] = []
        self._defcon_level : int = 0


    def set_name(self, name : str): self._name = name
    def get_name(self): return self._name

    def set_age(self, age : int): self._age = age
    def get_age(self): return self._age

    def set_annoyances(self):
        printspeed.print_medium("What's annoying you?")
        annoyance : str = input()
        self._cur_annoyances.append(annoyance)
        char_count = len(annoyance)
        if char_count < 10:
            printspeed.print_slow("That's not too bad I suppose...")
        elif char_count < 20:            
            printspeed.print_slow("Yeah, I agree.")
        else:
            printspeed.print_medium("You're f***in' a' right, brother.")
        
        self.check_defcon()
    def get_annoyances(self): return self._cur_annoyances

    def are_we_exploding(self):
        match self._defcon_level:
            case 0: pass
            case 1: 
                string : str = "Good job, soldier, you're holding it together."
                printspeed.print_slowest(string)
            case 2:
                string : str = "Easy there, fella', your eye's twitchin' a little."
                printspeed.print_slower(string)
            case 3:
                string : str = "Brother, brother calm down! You don't look so hot."
                printspeed.print_slow
            case 4:
                string : str = "JESUS CHRIST ALMIGHTY WE'RE ALL GONNA DIEEEEE!!!!@#!@#!@#!@#!@#"
                printspeed.print_medium(string)

    def check_defcon(self):
        self._level = (self._age / 1.5) + len(self._name)
        for i in self._cur_annoyances:
            self._level += len(i)
        print(f"(annoyance level currently: {self._level})")
        
        if self._level < 20:
            self._defcon_level = 0
        elif self._level < 30:
            self._defcon_level = 1
        elif self._level < 50:
            self._defcon_level = 2
        elif self._level < 100:
            self._defcon_level = 3
        else:
            self._defcon_level = 4
        
        self.are_we_exploding()

    def get_defcon(self):
        if len(self._cur_annoyances) > 4:
            s : str = "Oh shit.... you've a lot of annoyances"
            printspeed.print_slowest(s)
        return self._defcon_level
        
        

    def set_defcon(self, level : int):
        printspeed.print_slowest("Are you sure you want to do this..?")
        choice : str = input()
        if choice == "yes":
            self._defcon_level = level
        elif choice == "no":
            print("That's probably for the best..")
        else:
            print("Learn to answer a frickin' question.")

    name : str = property(get_name, set_name)
    age : int = property(get_name, set_name)
    cur_annoyances : list[str] = property(get_annoyances, set_annoyances)
    defcon : int = property(get_defcon, set_defcon)