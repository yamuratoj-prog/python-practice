import random


def guess_the_number():
    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Угадай число от 1 до 100: "))
        attempts += 1

        if guess < secret:
            print("Загаданное число больше")
        elif guess > secret:
            print("Загаданное число меньше")
        else:
            print(f"Угадали за {attempts} попыток!")
            break


guess_the_number()