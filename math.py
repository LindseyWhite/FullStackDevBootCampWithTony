def math(divisor, bound):
	maxN = 0
	for i in range(0, bound):
		if (i % divisor == 0):
			if i > maxN:
				maxN = i
	return maxN

def main():
	print(math(92, 10001))
main()