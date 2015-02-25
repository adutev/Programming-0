def twin_prime(p):
        q1 = p - 2
        q2 = p + 2

        p_is_prime = False
        q1_is_prime = False
        q2_is_prime = False

        for j in range(2, int(p + 1)):
                if p % j == 0:
                    if j == p:
                        p_is_prime = True
                    else:
                        p_is_ptime = False
                        break
        for j in range(2, int(q1 + 1)):
                if q1 % j == 0:
                    if j == q1:
                        q1_is_prime = True
                    else:
                        q1_is_ptime = False
                        break
        for j in range(2, int(q2 + 1)):
                if q2 % j == 0:
                    if j == q2:
                        q2_is_prime = True
                    else:
                        q2_is_ptime = False
                        break
        if p_is_prime and (not q1_is_prime) and (not q2_is_prime):
                print(str(p) + " is prime")
                print("But " + str(q1) + " and " + str(q2) + " are not.")
        elif p_is_prime:
            if q1_is_prime:
                print(q1, p)
            if q2_is_prime:
                print(q2, p)
        else:
                print(str(p) + " is not prime.")

p = input("Enter p: ")
p = int(p)

twin_prime(p)
    
