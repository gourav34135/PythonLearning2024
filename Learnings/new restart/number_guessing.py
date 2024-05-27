#prograam for guessing the number by giving the hint to the users
import random
secretnum=random.randint(0,100)
guessnum=int(input("enter the mnumber you gusssed betwween 1 to 100:"))
while guessnum !=secretnum:
    if guessnum<secretnum:
        print("your guesss is too low")
    else:
        print("your guess is too high")
    guessnum=int(input("guess a number between 0 to 100:"))
print("congratulations you gussed the n umber correctly")
