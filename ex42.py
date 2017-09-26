## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## ??
class Dog(Animal):
	
	def __init__(self, name):
		# ??
		self.name = name
		
## ??
class Cat(Animal):
	
	def __init__(self, name):
		## ??
		self.name = name
		
## ??
class Person(object):
	## ??
	def __init__(self, name):
		self.name = name
		
	## Person has-a pet of some kind
		self.pet = None
		
## ??
class Employee(Person):
	
	def __init__(self, name, salary):
		##?? hmm, what is this strange magic?
		super(Employe, self).__init__(name)
		## ??
		self.salary = salary
		
## ??
class Fish(object):
	pass
	
## ??
class Salmon(Fish):
	pass
	
## ??
class Halibut(Fish):
	pass
	

## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ?? 
mary = Person("Mary")

## 
mary.pet = satan

## set frank as an instance of employee with self, the name Frank and salary of 120000 as arguments
frank = Employee("Frank", 120000)

## set the pet attribute of Frank to rover
frank.pet = rover

## set flipper as an instance of class Fish
flipper = Fish()

## set crouse as an instance of class Salmon
crouse = Salmon()

## Set harry as an instance of class Halibut
harry = Halibut()