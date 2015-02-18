n = input("Enter n: ")
n = int(n)

perfect_numbers = 0
end = 6
sum = 3
while perfect_numbers < n:
        for i in range(3, int(end/2 + 1)):
                if end % i == 0:
                        sum += i
                        if sum > end:
                                break
        if sum == end:
                print(str(end) + " is perfect")
                perfect_numbers += 1
                
        end += 2
        sum = 3
