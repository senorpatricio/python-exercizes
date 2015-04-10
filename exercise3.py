
# exercise 3

def isFloat(string):
   try:
       float(string)
       return True
   except ValueError:
       return False
def check():
    mph = raw_input("Enter a speed in miles per hour: ")
    if mph.isdigit() and mph is not "0":
        return mph
    elif isFloat(mph) and mph is not "0":
        return mph
    else:
        print "Reenter speed, it must be a number > 0: "
    return check()
mph = float(check())

meters_per_mile = 1609.34
meters_per_hour = mph * meters_per_mile
barleycorns = mph * 117.647 * 24
furlongs = (meters_per_hour / 201.168) * 24 * 14
mach = meters_per_hour / ((1130 * 60 * 60) / 3.28084)
light_speed = meters_per_hour/(299792458 * 60 * 60)

print "Converted to Barleycorns per day is: {}" .format(barleycorns)
print "Converted to Furlongs per fortnight is: {}" .format(furlongs)
print "Converted to Mach number is: {}" .format(mach)
print "Converted to percentage of the speed of light is: {}" .format(light_speed)
print "Thanks for playing, dude!"


