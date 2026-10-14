import time
run = True

print("öndring")

wizard_name = "Rayan"

wizard_age = 17


wizard_name = input("What is your hero's name? ")
wizard_age = int(input("How old is your wizard? "))

print("This is your new story... your great adventure,", wizard_name)
time.sleep(2)
print(wizard_name, "is", wizard_age, "years old.")
time.sleep(1.2)

print("You have been summoned,", wizard_name, "and you see an old man.")
print("The old man asks: Do you remember who you are?!")

choice = input("Do you remember who you are, great wizard? (yes/no): ")

if choice == "yes": 
    print("Good...", wizard_name, "now lets begin.")
else:
    print(wizard_name,"does not remember who they are.")

choice = input("Will you help the village? (yes/no): ")

if choice == "yes":
    print("The old man gives you 10 magic coins.")
else:
    print("The old man looks disappointed.")

print("You begin your adventure to find the monster.")
print("Before you leave, the old man offers you some potions.")

potions = int(input("How many potions do you want to take? (1-5): "))

if potions >= 3:
    print("You are well prepared for the adventure!")
else:
    print("You might need more potions, but you continue anyway.")

inventory = ["Magic Wand", "Health Potion", "Sword"]

print("Here are the items in your inventory:")

for item in inventory:
    print(item)

print("You leave the village and start your adventure.")
print("After walking for a while, you enter a dark forest.")
print("You see two different paths.")

path = input("Do you want to go left or right? (left/right): ")

if path == "left":
    print("You go left and find a small house.")
    print("Inside the house you find a magic book.")
else:
    print("You go right and find a river.")
    print("You cross the river and continue your adventure.")

print("After a long adventure you finally make it to the village.")

print("But something is wrong.")

print("You see people running away and houses are destroyed.")

print("Then you see the monster in the middle of the village!")

fight = input("Do you want to fight the monster? (yes/no): ")

if fight == "yes":
    print(wizard_name, "gets ready to fight the monster!")
    print("You use the great magic blast to kill the monster!")
    print("You have killed the monster!")
else:
    print(wizard_name, "gets scared and runs away!")

print("The adventure of", wizard_name, "is over.")

print("THE END") 

