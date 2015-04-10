__author__ = 'patrickh'
# my code. needs a check to see if int or str
gallons = float(raw_input("Please enter the number of gallons of GAS: "))
if gallons.isalpha():
    gallons = float(raw_input("Please enter the number of gallons of GAS: "))

print "You chose %s gallons of Gasoline." % (gallons)

liters = gallons * 3.7854
barrels = gallons / 19.5
pounds = gallons * 20.0
btu = gallons * 75700.0
cost = gallons * 4.0

print "%.2f gallons is the equivalent of %.2f liters" % (gallons, liters)
print "%.2f gallons of gasoline is the equivalent of %.2f barrels of oil" % (gallons, barrels)
print "%.2f gallons of gasoline is the equivalent of %.2f pounds of CO2" % (gallons, pounds)
print "%.2f gallons of gasoline is the energy equivalent of %.2f gallons of ethanol" % (gallons, btu)
print "%.2f gallons costs %.2f US dollars (OMG)" % (gallons, cost)


# Jared's code that works great
def get_input(message):
        user_input = str(raw_input(message))
        sanitized_input = ""
        dot_count = 0
        for char in user_input:
            if char.isdigit() or (char is "." and dot_count < 1):
                if char is ".":
                    dot_count += 1
                sanitized_input = str(sanitized_input + char)
        if sanitized_input is not "0" and sanitized_input is not "" and sanitized_input is not ".":
            sanitized_input = float(sanitized_input)
            print "Your original input was '{}' but we extracted {} gallons.".format(user_input, sanitized_input)
            return sanitized_input
        print ("Cannot be 0 or a letter!")
        return None

gallons = None

while gallons is None:
    gallons = get_input("Please input the number of gallons: ")


liters = gallons * 3.7854
barrels = round(gallons / 19.5, 2)
co2 = round(gallons * 20, 2)
ethanol = round((gallons * 115) / 75.7, 2)
price = round(gallons * 4.00, 2)

print "Total liters: {} liters".format(liters)
print "Number of barrels of oil required: {} barrels".format(barrels)
print "Number of pounds of CO2 produced: {}lbs".format(co2)
print "Equivalent energy amount of ethanol gas: {} gallons. That is a difference of {} gallons."\
    .format(ethanol, (ethanol - gallons))
print "Total cost: ${}".format(price)