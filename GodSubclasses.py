class Human():
	def __init__(self, name):
		self.species = "human"
		self.name = name

	def __str__(self):
		return self.name

class Woman(Human):
	def __init__(self, name):
		self.sex = "woman"
		self.name = name

class Man(Human):
	def __init__(self, name):
		self.sex = "man"
		self.name = name

def creation(woman, man, humans):
	woman = Woman(woman)
	man = Man(man)
	humans.append(woman)
	humans.append(man)
	for i in range(0,len(humans)):
		print(humans[i])

def main():
	humans = []
	creation("Eve", "Adam", humans)
main()