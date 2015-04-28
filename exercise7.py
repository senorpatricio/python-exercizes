
weathers = {"Boston": "0 C", "Boise": "48 F", "Phoenix": "85 F", "Miami": "40 C", "Riverside": "30 C", "Baltimore": "32 F"}


def c2f(ctemp):
    return (ctemp * 1.8) + 32


def f2c(ftemp):
    return (ftemp - 32.0) / 1.8


def conversion():
    for key, val in weathers.itervalues():
        if "F" in val:
            fahr = int(val[:2])
            new_temp = f2c(fahr)
            print "In %s it is %i degrees fahrenheit, which is equivalent to %i degrees celsius" % (key, fahr, new_temp)
    for val in weathers.itervalues():
        if "C" in val:
            cels = int(val[:2])

# cities = {
#     "Boston": "0 C",
#     "Boise": "48 F",
#     "Phoenix": "85 F",
#     "Miami": "40 C",
#     "Riverside": "30 C",
#     "Baltimore": "32 F",
# }
# print
#
# for key, value in cities.iteritems():
#     if value[-1] == "C":
#         value = value[:-2]
#         print "In {} it is {} degrees Celsius" .format(key, value)
#         print "\twhich is equivalent to {} in Fahrenheit\n".format((int(value) * 1.8) + 32)
#     else:
#         value = value[:-2]
#         print "In {} it is {} degrees Fahrenheit" .format(key, value)
#         print "\twhich is equivalent to {} in Celsius\n".format((int(value) - 32) / 1.8)
