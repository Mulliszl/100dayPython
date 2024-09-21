print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island. Find the treasure and don't die.\n\n")

choice1 = input("Arriving upon the island there is what's left of a ruined stone structure.\n"
                "Immedietely upon entering you arrive at a fork.\n'Left' or 'right'\n").lower()

if choice1 == "left" or fork == "Left":
    choice2 = input("The ruins open up into a large room with murky water.\n"
                    "You hear a deep rumbling that appears to be getting closer to you.\n"
                    "'Swim' or 'wait'?\n").lower()
    # continue
else:
    print("You fall into a hole, breaking both legs. Trapped there you slowly die of thirst.\n Game Over.")
    #Death
if choice2 == "swim" or choice2 == "Swim":
    print("You dive into the freezing water."
          "As you begin to swim across something winds around you leg and drags you into the depths.\n Game Over.\n")
    #Death
else:
    choice3 = input("A rolling boulder crashes through what remains of the ruined wall to the left of you."
                    "Peering through the new hole you make out three colored doors.\n"
                    "Through which do you proceed?\n 'Red', 'Yellow', 'Blue'\n").lower()
    #Continue

if choice3 == "blue" or choice3 == "Blue":
    print("You are eaten by a swarm of giant crabs.\n Game Over.")
elif choice3 == "red" or choice3 == "Red":
    print("The floor collapses, you scream as you are burned alive in a pool of lava.\n Game Over.")
elif choice3 == "yellow" or choice3 == "Yellow":
    print("You find a chest full of unmarked gold bullion. Careful not to crash the market!\n You Win!")
else:
    print("The floor collapses and you fall into a spike trap.\n Game Over.")
