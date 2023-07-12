import json
import multiprocessing

'''
using multiprocessing when you need to loop through a large number of accounts and each region
'''


def parser(account, region):
	with open('fake_assets.json', 'r') as pub_file:
		data = json.load(pub_file)
		
		for items in data['assets']:
			if account == items['account_id']:
				print(items['account_id'])
				if region == items['region']:
					print(items['region'])


accounts = ['0000000001', '1200000202', '2000000020', '0000000002']
regions = ['us-east-1', 'us-east-2', 'us-west-2']


def run_faster():
	job_args = [
		[account, region]
		for account in accounts
		for region in regions
	]
	
	with multiprocessing.Pool(processes=5) as pool:
		pool.starmap(parser, job_args)


run_faster()
