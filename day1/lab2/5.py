import random

def run_game():
    t = 10
    num = random.randint(0, 100)
    while t > 0:
        g = int(input("enter a number: "))
        if g not in range(100):
            print("out of range")
            continue
        if g == num:
            print(f"congratulations you got it correctly and the remaining trials are {t}")
            return
        if g < num:
            print(f"{g} is smaller")
        else: print(f"{g} is greater")
        t = t - 1
    print("you missed all your trails")

while input("do you want to play a game? y/n") == "y":
    run_game()


