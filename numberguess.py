import random

target = random.randint(1, 100)
count = 0

while True:
    user_input = input("Enter a number between 1 to 100 OR QUIT (Q): ")

    # Check if user wants to quit
    if user_input.lower() == "q":
        print("---------   EXIT  ---------")
        break

    # Check if input is a valid number
    if not user_input.isdigit():
        print("Invalid input. Please enter a number between 1 to 100 or Q to quit.")
        continue

    num = int(user_input)
    count += 1

    if num == target:
        print("🎉 Congoo!! You guessed the right number!")
        print(f"You guessed the number in {count} {'try' if count == 1 else 'tries'}")
        print("---------- SUCCESS --------")
        print("--------- GAME OVER ---------")
        break
    elif num > target and num <= 100:
        print("Your number was too BIG...\nPlease guess a LESSER number...")
    elif num < target and num >= 1:
        print("Your number was too SMALL...\nPlease guess a BIGGER number...")
    else:
        print("You're guessing in the wrong direction. Range is 1 to 100.")
