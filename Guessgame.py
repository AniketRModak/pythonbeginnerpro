import random
n = random.randint(1, 10)

count = 0  # this for three chnace
while n != "guess":
    if count == 3:  # this for three chnace
        print("you lose")
        break
    guess = int(input("Enter a number : "))   # this for input
    if guess > n:
        print(" guess is High")
    elif guess < n:
        print(" guess is low ")
    else:
        print("you  win !")
        break
    count += 1  # tis for three chnace
