from random import randint

print("==========================")
print("WELCOME")
print("GUESS THE NUMBER OF M&Ms")
print("You have 7 chances to find the right number. Numbers from 1 to 130. Good luck!")
print("==========================")

def game():
    answer = randint(1, 130)

    while True:
        for n in range(7):
            user_guess = int(input("Guess the number?\n"))
            if user_guess == answer:
                print("WTF😱 dude, you won!")
                break
            elif user_guess > answer:
                print("Your guess is higher!")
            else:
                print("Your guess is smaller!")
        else:
            print(f"You lost! That's too bad. The answer was {answer}.")

        again = str(input("Do you want to play again? y or n: "))
        if again == "y":
            game()
        else:
            break

game()

