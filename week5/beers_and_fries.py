def max_score(beers, fries):
	score = 0
	beers = sorted(beers)
	fries = sorted(fries)
	
	for i in range(0, len(beers)):
		score += beers[i] * fries[i]

	return score

beers = [10, 11]
fries = [1, 5]

print (max_score(beers, fries))

beers = [5]
fries = [5]

print (max_score(beers, fries))

beers = [1000, 1010, 1020, 1030, 1040]
fries = [834, 500, -1, 0, 60]

print (max_score(beers, fries))