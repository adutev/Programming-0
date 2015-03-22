def forecast(days):
	snow = days.count("snow")
	rain = days.count("rain")
	sunshine = days.count("sunshine")

	if rain > snow and rain > sunshine:
		return "rain"
	elif snow > rain and snow > sunshine:
		return "snow"
	elif sunshine > rain and sunshine > snow:
		return "sunshine"
	elif snow == rain and snow > sunshine:
		return "sunshine"
	elif snow == sunshine and snow > rain:
		return "rain"
	elif rain == sunshine and rain > snow:
		return "snow"
	elif snow == rain == sunshine:
		return days[len(days) - 1]

days = ["snow", "snow", "rain", "sunshine"]
print(forecast(days))

days = ["rain", "rain", "snow", "snow", "sunshine", "sunshine"]
print(forecast(days))

days = ["rain", "rain", "sunshine", "sunshine"]
print(forecast(days))