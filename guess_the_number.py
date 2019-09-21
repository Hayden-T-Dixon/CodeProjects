import random
name = input("Please enter your name:   ")

print("Hello ", name, " it is so good to meet you!")

gameOn = True
while gameOn:
    print(name,", I am thinking of a number between 0 and 20")

    correct = False

    answer = random.randint(0,20)


    while not correct:
        guess = int(input("What is your guess?  "))

        
        if guess == answer:
            correct = True
            print("CORRECT! GOOD JOB!")

        elif guess < answer and guess > 0:
            print("That is lower than my number...")

        elif guess > answer and guess < 20:
            print("That is higher than my number...")

        else:
            print("That number is outside the range of 0 to 20...")


    playagain = input("Do you want to play again? (y or n)   ")

    if playagain == "n":
        gameOn = False



print("Thanks so much for playing!")
