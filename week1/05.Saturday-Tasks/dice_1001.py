from random import randint

ivan = 1001
maria = 1001

while (ivan != 0) and (maria != 0):
    current_sum_ivan = 0
    print ("Ivan is : ", ivan)
    for i in range(0, 5):
        current_sum_ivan += randint(1, 6)

    if ivan > 0:
        ivan -= current_sum_ivan
    else:
        ivan += current_sum_ivan    
    print("Dices sum of Ivan is: ", current_sum_ivan)
    print ("Ivan is : ", ivan)
    print ("-------------")
    current_sum_ivan = 0
        
    current_sum_maria = 0
    print ("Maria is : ", maria)
    for i in range(0, 5):
        current_sum_maria += randint(1, 6)

    if maria > 0:
        maria -= current_sum_maria
    else:
        maria += current_sum_maria
    print("Dices sum of Maria is: ", current_sum_maria)
    print ("Maria is : ", maria)
    print ("-------------")
    current_sum_maria = 0

    
    
if ivan == 0:
    print ("Ivan is the winner.")
else:
    print("Maria is the winner.")
