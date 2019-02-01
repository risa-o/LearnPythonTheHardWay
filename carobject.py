class Car(object):
	def __init__(self, make, model,color):
		self.make = make
		self.model = model
		self.color = color
		self.speed = 0
		self.miles = 0

	def accelerate(self):
		self.speed += 1
		self.miles += 1

	def decellerate(self):
		if self.speed > 0:
			self.speed -= 1
		self.speed = 0
		print ("The car is stopped")

	def stop(self):
		self.speed = 0

	def honk(self):
		print("Fashion! Beep beep!")


	def describe(self):
		print(f"The {self.color} {self.model} has {self.miles} miles and is going {self.speed} mph.")

mycar = Car("Toyota","Prius","blue")
mycar.describe()

mycar.accelerate()
mycar.accelerate()
mycar.describe()

mycar.accelerate()
mycar.accelerate()
mycar.accelerate()
mycar.describe()

mycar.stop()
mycar.describe()

mycar.accelerate()
mycar.decellerate()
mycar.decellerate()
mycar.decellerate()
mycar.describe()