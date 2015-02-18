score = input("Enter score: ")
score = int(score)


if score < 0 or score > 100:
	print("Sore must be in range 0 - 100")
elif score >= 0 and score <= 50:
	print("Слаб 2")
elif score > 50 and score <= 60:
	print("Среден 3")
elif score > 60 and score <= 70:
	print("Добър 4")
elif score > 70 and score <= 80:
	print("Много Добър 5")
elif score > 81 and score < 100:
	print("Отличен 6")
else:
	print("Много Отличен 7")
