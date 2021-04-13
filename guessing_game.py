from random import randint

print("==========================")
print("GUESS THE NUMBER OF M&Ms")
print("==========================")

def game():
    answer = randint(1, 100)

    while True:
        for n in range(5):
            user_guess = int(input("Guess the number?\n"))
            if user_guess == answer:
                print("WTF😱 dude, you won!")
                break
            elif user_guess > answer:
                print("Your guess is higher!")
            else:
                print("Your guess is smaller!")
        else:
            print(f"You loose! That's too bad. The answer was {answer}.")

        again = str(input("Do you want to play again? y or n: "))
        if again == "y":
            game()
        else:
            break

game()

