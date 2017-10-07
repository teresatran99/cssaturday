# Dragon Realm
# A game by Teresa Tran
# 10/7/2017

# import stuff
import random
import time

# Show Introduction
# def "showIntro():" OR "show_intro():" works, but code must be consistent
def showIntro():
    print('''You are in a land full of dragon. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on site.''')
    print()

# showIntro():
# showIntro()
# showIntro()
# ^ typing this three times will result to my whole introduction
# to be printed 3 times

def chooseCave():
    cave = ""
    while cave != "1" and cave != "2" :
        print("Which cave will you go into? (1 or 2)")
        cave = input()
    return cave

showIntro()
chooseCave()
