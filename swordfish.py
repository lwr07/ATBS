import sys

attempts = 0
while True:
	attempts = attempts + 1
	if attempts == 6:
		break
	print ('Who are you?')
	name = raw_input()
	if name != 'Joe':
			continue
	print ('Hello, Joe. What is the password?')
	password = raw_input()
	if password == 'swordfish':
		print ('Access granted')
		sys.exit()
print ('Too many attempts')
