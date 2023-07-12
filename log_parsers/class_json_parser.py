import json


class MyParser:
	def __init__(self, dns_name, instance_id, owner):
		self.dns_name = dns_name
		self.instance_id = instance_id
		self.owner = owner
	
	def get_dns_name(self):
		dns_data = f'I found your dns name {self.dns_name} with owner {self.owner}'
		return dns_data
	
	def get_instances(self):
		instance_data = f'I found your instances {self.instance_id} with owner {self.owner}'
		return instance_data


def parser():
	with open('aws_elb.json', 'r') as data_file:
		load_data = json.load(data_file)
		for data in load_data['load_balancers']:
			dns_n = data['dns name']
			owner = data['instance owner']
			for instance in data['attached instances']:
				instance = instance['instance_id']
				
				my_data = MyParser(dns_n, instance, owner)
				instances = my_data.get_instances()
				dns_data = my_data.get_dns_name()
				print(f'returned instance data', instances)
				print(f'returned dns data', dns_data)


parser()
