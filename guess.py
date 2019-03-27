#import the random module to generate a random integer
import random

#generate an integer between 1 and 20
randomNum = random.randint(1, 20)

#this only reads at game start
print "I'm thinking of a number between 1 and 20"

#function that handles user input as well as conditional for output.
def guesser():
    print "Take your guess: "
    guess = input()

# if and elif have recursive functions so the number randomNum is not reset on an incorrect guess because the scope hasn't returned to global, where randomNum lives.
    if (guess > randomNum):
        print "Guess a lower number!"
        guesser()
    elif (guess < randomNum):
        print "Guess a higher number!"
        guesser()
    else:
        print "Nice Job!"

#call function after greeting player and defining in code
guesser()


