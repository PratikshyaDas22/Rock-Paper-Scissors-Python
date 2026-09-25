import random
'''
1 for rock
-1 for paper
0 for scissor

'''
computer = random.choice([-1,0,1])
your_choice = input("Enter your choice: ")
dict = {"r":1,"p":-1,"s":0}
reversedict = {1:"Rock🪨", -1:"Paper📄", 0:"Scissor✂"}

you = dict[your_choice]

print(f"You chose: {reversedict[you]}\nComputer chose: {reversedict[computer]}")

if computer == you:
    print("It's a draw😅")

else:
    if computer == -1 and you == 1:
        print("You Lose!😔")

    elif computer == -1 and you == 0:
            print("You Win!🥳🎉")

    elif computer == 1 and you == -1:
            print("You Win!🥳🎉")

    elif computer == 1 and you == 0:
            print("You Lose!😔")

    elif computer == 0 and you == 1:
            print("You Win!🥳🎉")

    elif computer == 0 and you == -1:
            print("You Lose!😔")

    else:
        print("Something went wrong ⚠")
