class Animal:
    
    name =""
    
    def eat(self):
        print("animal can eat")

class Dog(Animal):
    def display(self):
        print(self.name)

dog_name = Dog()
dog_name.name="puppy"
dog_name.display()


