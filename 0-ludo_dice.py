import random

while True:
    command = input("Enter a command (toss/quit): ")
    if command.lower() == "toss":
        dice_roll1 = random.randint(1,6)
        dice_roll2 = random.randint(1,6)
        print("Your Dice roll is {} : {}".format(dice_roll1,dice_roll2))
    elif dice_roll1==6 and dice_roll2==6:
        dice_roll1 = random.randint(1,6)
        dice_roll2 = random.randint(1,6)
        print("Your Dice roll is {} : {}".format(dice_roll1,dice_roll2))
    elif command == "quit":
        print("Goodbye, game over")
        break
    else:
        print("Invalid command, try again.")