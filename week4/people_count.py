from test_data import generate_test

def get_people_count(activity):
    return len(set(activity))

activity = generate_test(300)

print(get_people_count(activity))
