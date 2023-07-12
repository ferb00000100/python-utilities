import csv
import pandas as pd


class MyPandasClass:
	def __init__(self, data):
		self.data = data
	
	def pandasize(self):
		df = pd.DataFrame(self.data)
		return df


class MyDict:
	def __init__(self, Id, name, env, port):
		self.Id = Id
		self.name = name
		self.env = env
		self.port = port
	
	def create_dictionary(self):
		my_dict = {
			'id': self.Id,
			'name':  self.name,
			'env': self.env,
			'port': self.port
		}
		return my_dict


def parse_it():
	with open('ports.csv', 'r') as csv_file:
		data = csv.reader(csv_file)
		
		for line in data:
			data = MyDict(line[0], line[1], line[2], line[3])
			returned_data = data.create_dictionary()
			print(returned_data)
			
		# uncomment for pandas
		# ---------------------
		# for line in data:
		# 	data = MyPandasClass(line)
		# 	panda_data = data.pandasize()
		# 	print(panda_data)


parse_it()

