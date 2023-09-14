import csv

'''
This function grabs all the ports, counts them, sorts them and removes duplicates outputs summary
the format of the csv file is nmap output from a 3rd party scanner
'''


def count_sort():
	port_list = []
	final_list = []
	with open('ports.csv') as data_file:
		data = csv.reader(data_file)
		for port in data:
			print(port[3])
			port_list.append(port[3])
		port_list.sort()
		for x in port_list:
			data = port_list.count(x), x
			print(data)
			final_list.append(data)
		final_list = list(set(final_list))
		for line in final_list:
			print(line)


count_sort()

