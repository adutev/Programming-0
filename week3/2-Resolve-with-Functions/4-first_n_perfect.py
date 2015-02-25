def first_n_perfect(n):
        perfect_numbers = 0
        end = 6
        sum = 3

        result = []
        while perfect_numbers < n:
                for i in range(3, int(end/2 + 1)):
                        if end % i == 0:
                                sum += i
                                if sum > end:
                                        break
                if sum == end:
                        result.append(end)
                        perfect_numbers += 1
                end += 2
                sum = 3
        return result


n = input("Enter n: ")
n = int(n)

print(first_n_perfect(n))
