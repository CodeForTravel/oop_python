class Animal:
    def Walk(self):
        print('Hello, I am the parent class')


class Dog(Animal):
    def Walk(self):
        print('Hello, I am the child class')


print('The method Walk here is overridden in the code')

# Invoking Child class through object r

r = Dog()
r.Walk()

# Invoking Parent class through object r

r = Animal()
r.Walk()
