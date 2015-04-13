__author__ = 'patrickh'

# Return half of the string


def first_half(str):
    return str[:len(str)/2]


print "WooHoo" [:3:]

# return the first 2 elements in the array
# codingbat practice: list-1>sum2


def sum2(nums):
    if len(nums) == 0:
        total = 0
        return total
    elif len(nums) < 2:
        total = nums[0]
        return total
    elif len(nums) >= 2:
        total = nums[0] + nums[1]
        return total

# examples in class


class Person(object):
    some_variable = 5

    def __init__(self, name, message):
        self.name = name
        self.message = message
        print self.name

    def __add__(self, other):
        return '%s and %s' % (self.name, other.name)

    def __str__(self):
        return self.name + " is the best!"

    def speak(self):
        print self.message


bob = Person("Bob", "I'm a good guy")
mary = Person("Mary", "I'm a nice person")
bob.age = 30
print bob.age

print hasattr(bob, "age")
print hasattr(mary, "age")

# print getattr(bob, "age")


setattr(bob, "age", 31)
print bob.age

delattr(bob, "age")
print bob.age  # Fails

bob.speak()
bob.age = 87
# print bob.age
# print bob + mary
print bob
print mary

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

rabbit = Car('2007', 'VW', 'Rabbit', '2', 'Tornado Red')

print rabbit