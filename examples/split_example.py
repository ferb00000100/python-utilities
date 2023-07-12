emails = "han.solo@here.com, chewbacca@here.com, yoda@here.com, boba.fett@here.com"

print(f'string: {emails}')
count = 0
if "," in emails:
	emails = emails.split(',')
	print(f'list: {emails}')
	for email in emails:
		email = email.strip(' ')
		print(email)
		count += 1

