# Program to illustrate method overloading
class edpresso:
    def Hello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')


# Create an instance
obj = edpresso()

# Call the method
obj.Hello()

# Call the method with a parameter
obj.Hello('Kadambini')
