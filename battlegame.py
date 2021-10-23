#Wizzard
wizzard = "Wizzard"
wizzard_hp = 70
wizzard_damage = 150

#Elf
elf = "Elf"
elf_hp = 100
elf_damage = 100

#Human
human = "Human"
human_hp = 150
human_damage = 20


#Dragon
dragon_hp = 300
dragon_damage = 50

while True:
    print("""
    1. Wizzard
    2. Elf
    3. Human
    """)
    choice = input("Select your character: ")
    if(choice == "1"):
        character = wizzard
        my_hp = wizzard_hp
        my_damage = wizzard_damage
        break
    if(choice == "2"):
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if(choice == "3"):
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    print("Unknown character")
print("Class: " + str(character) + "\n" + "HP: " + str(my_hp) + "\n" + "Damage: " + str(my_damage))


while True:
    dragon_hp = dragon_hp - my_damage
    print("The " + str(character) + " hit the dragon!")
    print("The Dragon's hitpoints are now: " + str(dragon_hp))
    print("\n")
    if(dragon_hp <= 0):
        print(" The dragon has been defeated!")
        break
    my_hp = my_hp - dragon_damage
    print("The " + str(character) + " has been damaged by the dragon. The " + str(character) + " is set at: " + str(my_hp))
    print("\n")
    if(my_hp <= 0):
        print("Your character has lost the battle")
        break