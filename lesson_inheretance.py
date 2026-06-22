class Animal:
    def __init__(self, name, sound):
        self.name = name

    def speak(self):
        return '...'

class Dog(Animal):
    def speak(self):
        return f'{self.name} says Woof'

print(Dog('Dog', 'Woof').speak())