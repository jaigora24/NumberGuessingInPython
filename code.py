import random
import math

lower = 1;  #fix the range of numbers
upper = 100;


x = random.randint(lower, upper)   #generate random numbers 

count = 0    #initialize count to 0

while count < math.log(upper - lower + 1, 2):
	count += 1

	guess = int(input("Guess a number:- "))   #guessing input

	if x == guess:   #conditions for testing
		print("Congratulations you did it in ",
			count, " try")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")
