import random
def guess(a):
    random_number = random.randint(1,a)
    guess = 0
    while guess != random_number:
        guess = int(input('Guess a number between 1 and {a}: '))
        if guess < random_number:
            print("It's Low, Go High")
        elif guess > random_number:
            print("Going Good! decrease the number please")
        else:
            print('You Guessed it correct')

guess(10)