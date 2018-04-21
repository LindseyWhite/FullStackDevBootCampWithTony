class Acronym():
	def __init__(self, string):
		self.string = string
		#abbrev(string)

	def __str__(self):
		return acro(self.string)

	def __add__(self, new):
		newString = self.string + " " + new
		return acro(newString)

def acro(string):
	string_list = string.split(" ")
	acro = ""
	for i in string_list:
		acro += i[0]
	return acro

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
	ac1 = Acronym("oh my god")
	print(ac1)
	ac2 = ac1.__add__("wow")
	print(ac2)
	print("Time to execute: ", time.time() - start_time)
main()