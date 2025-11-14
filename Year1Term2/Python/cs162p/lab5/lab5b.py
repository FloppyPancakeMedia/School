from annoyance import Annoyance
import printspeed

a : Annoyance = Annoyance()

printspeed.print_medium("What's your name, son?")
name : str = input()
a.set_name(name)

printspeed.print_medium("Now how old are you?")
age_str : str = input()
age : int = int(age_str)
a.set_age(age)

while (a.get_defcon() < 4):
    a.set_annoyances()

