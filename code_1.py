import random

house = float(input("Enter house advantage (as a decimal): "))
bet = float(input("Set the bet: "))
win = float(input("Set the win amount: "))
bank = float(input("How much money do you want to start with? "))

top = bet - (bet*house)
bottom = win + bet

while not top.is_integer() or not bottom.is_integer():
    top = top * 10
    bottom = bottom * 10

top = int(top)
bottom = int(bottom)

total = int(input("How many times do you want to play? "))
count = 1
while count <= total:
    x = random.randint(1, bottom)
    if x <= top:
        print("Win!")
        bank = bank + win
    else:
        print("Lose.")
        bank = bank - bet
    count = count + 1

print("Your bank is at", bank)
