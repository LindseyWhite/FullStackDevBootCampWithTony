class Abbreviation():
	def __init__(self, string):
		self.string = string
		#abbrev(string)

	def __str__(self):
		return abbrev(self.string)

	def __add__(self, new):
		newString = self.string + " " + new
		return abbrev(newString)

def abbrev(string):
	string_list = string.split(" ")
	abbrev = ""
	for i in string_list:
		abbrev += i[0]
	return abbrev

import time

def main():
	start_time = time.time()
	MyDict = {"oh my god" : "omg"}
	MyDict["laugh out loud"] ="lol"
	MyDict["be right back"] = "brb"
	print(MyDict)
	if "laugh out loud" in MyDict:
		print("haha")
	print(not False)
	ab1 = Abbreviation("oh my god")
	print(ab1)
	ab2 = ab1.__add__("wow")
	print(ab2)
	print("Time to execute: ", time.time() - start_time)
main()