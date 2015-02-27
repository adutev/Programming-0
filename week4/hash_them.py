keys = ['Mimi', 'Gosho', 'Roro']
values = [5, 6, 9, 9]

def hash_them(keys, values):
    hash_table = {}
    max = len(keys)
    if len(values) > max:
        max = len(values)
        for i in range(len(keys), max):
            keys.append(None)
    elif len(values) < max:
         for i in range(len(values), max):
            values.append(None)
    for i in range(0, max):
        hash_table[keys[i]] = values[i]

    return hash_table
print(hash_them(keys, values))
