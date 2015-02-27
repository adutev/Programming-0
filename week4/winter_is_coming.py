seasons = ["winter", "summer", "summer", "spring", "srping", 'winter', "summer", "summer", "spring", "srping"]

def winter_is_coming(seasons):
    start = 0
    end = 0
        
    for s in range(0, len(seasons)):
        if seasons[s] == 'winter':
            start = s
            end = s
        else:
            end += 1
    if end - start >= 5:
        return True
    else:
        return False
print(winter_is_coming(seasons))
            
