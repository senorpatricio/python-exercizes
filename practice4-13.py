"""
# write a car class
every object from the car class will nee typical attributes of a car
(wheels, steering wheel, doors, owner, engine, etc)

make 3 instances of your car class and print out the attributes of each car
"""

class Car(object):
    def __init__(self, year, make, model, num_doors, color):
        self.year = year
        self.make = make
        self.model = model
        self.num_doors = num_doors
        self.color = color
# this will format it so that it will print it out nicely, this is the Python 3 way to do it.

    def __str__(self):
        return "A {} {} {} with {} doors in {}".format(self.year, self.make, self.model, self.num_doors, self.color)

rabbit = Car(2007, 'VW', 'Rabbit', 2, 'Tornado Red')
gti = Car(2009, 'VW', 'GTI', 2, 'Graphite Grey')
gti.turbo = True
karmann_ghia = Car(1963, 'VW', 'Karmann Ghia', 2, 'Orange')

print rabbit
print gti
print karmann_ghia