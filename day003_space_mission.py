from random import choice

print(r'''
       -][][-
       /++++\
      /OOOOOO\
.=====!oooooo!=====.
 \____\_-_-_-/____/
      |<><><>|
       \    /
      ./\ |/\.
     ./  ^|  \.
     /"   |  "\
   ^^^   ^^^  ^^^''')

print("Welcome to Space Mission!")
print("Your mission is to explore the planet and return safely.\n")

choice1 = input("Your spaceship reaches a mysterious planet. Do you 'land' or 'orbit'? ").lower()

if choice1 == "land":
    choice2 = input("You are on the planet surface. Do you 'explore' the cave or 'stay' in the ship? ").lower()
    if choice2 == "explore":
        choice3 = input("Inside the cave, you find two paths. Do you go to the 'crater' or the 'hill'? ").lower()
        if choice3 == "crater":
            print("You discover alien technology and safely return to your ship! You Win!")
        else:
            print("You fall into a pit of quicksand. Game Over.")
    else:
        print("A meteor storm hits your ship. Game Over.")
else:
    print("Your orbit fails and your ship crashes. Game Over.")
