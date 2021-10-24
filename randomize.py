import random


# RANDINT
pips = random.randint(1, 6)
print("You roll the die... it lands with", pips, "pips showing.")

# CHOICE
prizes = ["a car", "1,000,000", "a pony", "$500000"]
prize_won = random.choice(prizes)
# , is for adding strings. + is for adding space
print("You turn the wheel of fortune... it lands on a prize of", prize_won + "!!")

# SHUFFLE
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
random.shuffle(cards)
print("The cards are in this order: ")
print(cards)