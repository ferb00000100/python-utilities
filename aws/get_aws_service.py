import boto3


def get_client(region, service, credentials):
	client = boto3.client(
		service,
		region_name=region,
		aws_access_key_id=credentials['AccessKeyId'],
		aws_secret_access_key=credentials['SecretAccessKey'],
		aws_session_token=credentials['SessionToken']
	)
	return client


def get_resource(region, service, credentials):
	resource = boto3.resource(
		service,
		region_name=region,
		aws_access_key_id=credentials['AccessKeyId'],
		aws_secret_access_key=credentials['SecretAccessKey'],
		aws_session_token=credentials['SessionToken']
	)
	return resource


def assume_role(account):
	sts_client = boto3.client('sts')
	assumed_role_object = sts_client.assume_role(
		RoleArn='arn:aws:iam::' + account + ':role/MyRole',
		RoleSessionName='AssumeRoleSession'
	)
	credentials = assumed_role_object['Credentials']
	return credentials
	
	
#  example on calling the functions
my_account = 'account_id'
assumed_credentials = assume_role(my_account)

dynamodbClient = get_client('us-east-1', 'dynamodb', assumed_credentials)
