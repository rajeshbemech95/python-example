class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return print(" ")

class Dog(Animal):
    def speak(self):
        return print(self.name,"woof")
    
class Cat(Animal):
    def speak(self):
        return print(self.name,"miyoow")
    
dog = Dog("puppy")
cat =Cat("cat")

dog.speak()
cat.speak()
