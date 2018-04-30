# decorator practice
def decorator(funct):
	def new_funct(*nums, **options):
		try:
			return "The " + funct(*nums, **options)
		except TypeError:
			return ""
	return new_funct

@decorator
# multiple function arguments practice
def funct(*nums, **options):
	# exception handling practice
	try:
		num = 0
		for i in nums:
			num += i
		if options.get("action") == "reg":
			print("The original numbers added are %d" % (num))
		halfnum = num/2
		return "half number = " + str(halfnum)
	except TypeError:
		print("You did not enter a number.")
		output = nums
		print("You entered = ", output)

# generator practice (fibonacci sequence)
def fib():
	a, b = 1, 1
	while 1:
		yield a
		a, b = b, a+b


def main():
	print(funct("a"))
	print(funct(3.0, 4.0, 5.0, action = "reg"))

	# list comprehension practice
	sentence = "my very excellent mother just served us nachos"
	words = sentence.split()
	planets = [word[0] for word in words]
	print(planets)

	counter = 0
	for n in fib():
		print(n)
		counter += 1
		if counter == 10:
			break
main()