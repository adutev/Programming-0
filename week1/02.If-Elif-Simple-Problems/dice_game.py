from random import randint

n = input("Enter dise side: ")
n = int(n)

player1 = input("Enter player1 name: ")
player2 = input("Enter player2 name: ")

player1_roll = randint(1, n)
print(player1 + " rolls: " + str(player1_roll))

player2_roll = randint(1, n)
print(player2 + " rolls: " + str(player2_roll))

if player1_roll > player2_roll:
    print(player1 + " wins!")
elif player2_roll > player1_roll:
    print(player2 + " wins!")
else:
    print("Draw!")
