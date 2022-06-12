class Duck:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('I can run!')


class Car:
    def __init__(self, model):
        self.model = model

    def run(self):
        print('I can run, too!')


def quacks(obj):
    obj.run()


donald = Duck('Donald Duck')
car = Car('Tesla')
quacks(donald)
quacks(car)
