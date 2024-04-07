class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Voice")

class Dog(Animal):

    
    print("Bark")
    
class Cat(Animal):
    def speak(self):
        print("Meow")
Dog.speak()
dog = Dog("puppy")
cat = Cat("cat")
ani = Animal("name")

print(dog.name)
print(dog.speak())
print(cat.name)
print(cat.speak())
print(ani.speak())