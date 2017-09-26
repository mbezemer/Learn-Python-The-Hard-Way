## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## create a class Dog that is-a Animal
class Dog(Animal):
	
	def __init__(self, name):
		# class Dog has an init that takes self and name as parameters
		self.name = name
		
## create a class Cat that is-a Animal
class Cat(Animal):
	
	def __init__(self, name):
		## class Cat has an init that takes self and name as parameters
		self.name = name
		
## create a class Person that is-a object
class Person(object):
	## class Person has an init that takes self and name as attributes
	def __init__(self, name):
		self.name = name
		
	## Person has-a pet of some kind
		self.pet = None
		
## create a class Employee that is a Person
class Employee(Person):
	
	def __init__(self, name, salary):
		## run the __init__ method of a parent class reliably
		super(Employe, self).__init__(name)
		##  Employee has-a salary attribute
		self.salary = salary
		
## create a class Fish that is-a object
class Fish(object):
	pass
	
## create a class Salmon that is-a Fish
class Salmon(Fish):
	pass
	
## create a class Halibut that is-a Fish
class Halibut(Fish):
	pass
	

## rover is-an instance of class Dog with name "Rover"
rover = Dog("Rover")

## satan is-an instance of class Cat with name "Satan"
satan = Cat("Satan")

## mary is-an instance of class Person with name "Mary"
mary = Person("Mary")

## set pet attribute of mary to satan
mary.pet = satan

## frank is-an instance of employee with self, the name Frank and salary of 120000 as arguments
frank = Employee("Frank", 120000)

## set pet attribute of Frank to rover
frank.pet = rover

## flipper is-an instance of class Fish
flipper = Fish()

## crouse is-an instance of class Salmon
crouse = Salmon()

## harry is-an instance of class Halibut
harry = Halibut()