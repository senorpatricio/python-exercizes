__author__ = 'patrickh'
first_number = int(raw_input("Enter the first number: "))

while first_number == 0:
    first_number = int(raw_input('You must enter a non-zero number:'))

second_number = int(raw_input("Enter the second number: "))

while second_number == 0:
    second_number = int(raw_input('You must enter a non-zero number:'))


sum_number = first_number + second_number
difference = first_number - second_number
product = first_number * second_number
quotient = first_number/second_number
remainder = first_number % second_number

print "The sum of %s and %s is: %s" % (first_number, second_number, sum_number)
print "The difference of %s and %s is: %s" % (first_number, second_number, difference)
print "The product of %s and %s is: %s" % (first_number, second_number, product)
print "The quotient of %s and %s is: %s with remainder %s" % (first_number, second_number, quotient, remainder)
