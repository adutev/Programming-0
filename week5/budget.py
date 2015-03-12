def on_budget(books, budget):
	books_on_budget = 0
	loan = 0
	books = sorted(books)

	for book in books:
		if budget >= book:
			books_on_budget += 1
			budget -= book
		else:
			budget -= book

	if budget < 0:
		loan = abs(budget)

	result = {
		"books_on_budget": books_on_budget,
		"loan" : loan
	}

	return result

books = [0, 10, 100, 5, 3, 8, 25]
budget = 35

print(on_budget(books, budget))

books = [0, 0, 0]
budget = 10

print(on_budget(books, budget))

books = [50, 60, 100]
budget = 20

print(on_budget(books, budget))