import random

# Input the range of number from the user
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

lst1 = []
for i in range(a, b + 1):
    lst1.append(i)
num = random.choice(lst1)

# creating a list for storing the count value of the particular player.
count = []
# using a loop for 2 players
for j in range(2):
    print(f"*****************Player {j+1}'s Turn*****************")
    for i in range(10):
        test = int(input(f"Guess the number between {a} and {b}: "))
        if test > num:
            print("Wrong choice, pls select smaller no \n")
        elif test < num:
            print("Wrong choice, pls select greater no \n")
        else:
            print(f"Correct, you took {i + 1} chances")
            count.append(i+1)
            break

# for checking the player's turn for the winner
print("**************************************************************")
if count[0] < count[1]:
    print(f"Player 1 wins with counts - {count[0]}")
elif count[0] > count[1]:
    print(f"Player 2 wins with counts - {count[1]}")
else:
    print(f"Match draws, with {count[0]}")