class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return '...'

dog = Animal('Dog')

print(dog.speak())

class Dog(Animal):
    def speak(self):
        return f'{self.name} says Woof'

print(Dog('Dog').speak())