def grades_that_pass(students, grades, limit):
	result = []
	for index, grade in enumerate(grades):
		if grade >= limit:
			result.append(students[index])
	return result

students = ["Rado", "Ivo", "Maria", "Nina"]
grades = [3, 4.5, 5.5, 6]

result = grades_that_pass(students, grades, 4.0)
print result