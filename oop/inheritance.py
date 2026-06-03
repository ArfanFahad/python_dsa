class Animal:
    def speak(self):
        print("Animal Sound")
        
class Dog(Animal):
    def speak(self):
        print("Woof")

d = Dog()
d.speak()
    