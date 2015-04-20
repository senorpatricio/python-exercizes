

weathers = {
    "Boston": "0 C",
    "Boise": "48 F",
    "Phoenix": "85 F",
    "Miami": "40 C",
    "Riverside": "30 C",
    "Baltimore": "32 F"
}
# how do i create a way for a loop to read the values as either fahrenheit or celsius and then convert
# if the value contains a C, convert to Fahrenheit. If the value contains an F, convert to Celsius

for key, val in weathers:
    print "In " + key + " it is " + val + ", which is equivalent to "