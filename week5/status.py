def status_count(students):
	result = {
		"finalized":[],
		"not_finalized":[]
	}

	for student in students:
		if student['status'] == 'finalized':
			result['finalized'].append(student['name'])
		else:
			result['not_finalized'].append(student['name'])

	return result
	
students = [{
              "name": "RadoRado",
              "status": "not_finalized"
            }, {
              "name": "Ivo",
              "status": "finalized"
            }, {
              "name": "Genadi",
              "status": "finalized"
            }]

print(status_count(students))