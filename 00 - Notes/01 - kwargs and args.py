

#Using the *args operator for unlimited positional arguments
def add(*args):
    sum = 0
    for i in args:
        sum += i
    print( sum )


#Using unlimited keyword based arguments
def calculate(n, **kwargs):
    n += kwargs['add']
    n*= kwargs['multiply']
    print( n )

calculate(10, add=10, multiply=10)


#using unlimited keyword based arguments, safe for when parameter isnt specified
class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
    
toyota = Car(make='Toyoya')
print(toyota.model)
#Output: None
