def collatz(number):
	if (number % 2 == 0): #even number
		print(number // 2)
		return(number // 2)
	else:
		print(3 * number + 1)
		return(3 * number + 1)

print('Enter a number')
userNum = int(input())

while userNum != 1:
	userNum = collatz(userNum)

print('You finished the Collatz sequence')