first_name = input("Enter first name: ")
second_name = input("Enter second name: ")
third_name = input("Enter third name: ")
birth_year = input("Enter birth year: ")
birth_year = int(birth_year)
current_age = input("Enter age: ")
current_age = int(current_age)

details = {}
details['current_age'] = current_age
details['birth_year'] = birth_year
details['second_name'] = second_name
details['third_name'] = third_name
details['first_name'] = first_name

print(details)
