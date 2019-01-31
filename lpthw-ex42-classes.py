## Animal is-a object (Yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):
	def __init__(self, name):
		## Dog has-a name
		self.name = name

## Cat is-a Animal
class Cat(Animal):

	def __init__(self,name):
		##Cat has-a name
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name
		##Person has-a pet (of none)
		self.pet = None

## Employee is-a person
class Employee(Person)

	def __init__(self,name, salary)
	## run the init method of the parent class (reliably)
	super(Employee, self).__init___(name)
	## Employee has-a salary
	self.salary = salary

## Fish is an object
class Fish(object):
	pass

##Salmon is-a Fish
class Salmon(Fish):
	pass

##Halibut is-a Fish
class Halibut(Fish):
	pass

##Rover is-a Dog
rover = Dog("Rover")

#Satan is-a cat
satan = Cat("Satan")

#Mary is-a person
mary = Person("Mary")

# Mary has-a pet, satan
mary.pet = satan

#frank is-a Employee that has-a salary of 120000
frank=Employee("Frank", 120000)

#Frank has-a pet, named rover
frank.pet = rover

#Flipper is-a fish
flipper = Fish()

#crouse is-a Salmon
crouse = Salmon()

# harry is a Halibut
harry = Halibut()