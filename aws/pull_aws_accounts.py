import boto3


def assume_role(account):
	sts_client = boto3.client('sts')
	assumed_role_object = sts_client.assume_role(
		RoleArn='arn:aws:iam::' + account + ':role/MyRole',
		RoleSessionName='AssumeRoleSession'
	)
	credentials = assumed_role_object['Credentials']
	return credentials


def get_client(region, service, credentials):
	client = boto3.client(
		service,
		region_name=region,
		aws_access_key_id=credentials['AccessKeyId'],
		aws_secret_access_key=credentials['SecretAccessKey'],
		aws_session_token=credentials['SessionToken']
	)
	return client


def pull_accounts(client):
	paginator = client.get_paginator('list_accounts')
	page_iterator = paginator.paginate()
	with open('accounts/accounts_list.txt', 'w') as file:
		for page in page_iterator:
			for acct in page['Accounts']:
				iD = acct['Id']
				name = acct['Name']
				status = acct['Status']
				file.write(f'{status},{iD} - {name}')


master_org_account = 'account_id'
assumed_credentials = assume_role(master_org_account)

org_client = get_client('us-east-1', 'organizations', assumed_credentials)

pull_accounts(org_client)


