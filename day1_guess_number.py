import random as rnd
import sys
counter = 1
select_range = list(map(int,input("enter the start and end").split(" ")))
print(select_range)

rnd_number = rnd.randint(select_range[0],select_range[1])
#print(rnd_number)

while counter < 6 :
    guess_number = int(input())
    if guess_number > rnd_number:
        print("Try Again! You guessed too high")
    elif guess_number < rnd_number:
        print("Try Again! You guessed too small")
    else :
        print("Guess was right")
        sys.exit(1)
    counter += 1
