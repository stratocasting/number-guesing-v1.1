import random
answer = random.randint(0,101)
difficulty = ""
game_over = False
def loop():
    global game_over
    global health
    print (f"you are on {difficulty} mode, so you have {health} turns")
    guess = int(input("Make a guess between 0-100\n:"))
    if guess < answer:
        print ("too low")
    elif guess > answer:
        print ("too high")
    else:
        print (f"correct answer is {answer}, you win")
        game_over = True
        health = 1
def zorluk():
    global health
    global difficulty
    difficulty = input("Wanna try easy or hard? \n").lower()
    if difficulty == "easy":
        health = 10
    elif difficulty == "hard":
        health = 5
    else:
        zorluk()

health = 0
zorluk()

for x in range(health):
    while game_over == False:
        remainder = health
        loop()
        health -= 1
        if health > 0:
            print (f"{health} health left")

