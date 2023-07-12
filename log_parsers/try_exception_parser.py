import json
import csv

with open('ports.csv', 'r') as file:
	print('---------------------------')
	print('running csv dictionary example')
	print('---------------------------')
	data = csv.reader(file)

	for line in data:
		my_dictionary ={
			'id': line[0],
			'something': line[1],
			'something else': line[2]
		}
		print(my_dictionary)

with open('aws_elb.json', 'r') as file:
	print('---------------------------')
	print('running try except example')
	print('---------------------------')
	data = json.load(file)
	try:
		print(data['load_balancers'])
		for item in data['load_balancers']:
			print(item['dns name'])
			for instance in item['attached instances']:
				print(instance['instance_id'])

	except KeyError as error:
		print('WAIT key error', error)
	except TypeError as error:
		print('WAIT type error', error)
	else:
		print('nice job')
