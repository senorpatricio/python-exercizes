__author__ = 'patrickh'
#Define a function that takes 2 parameters (weekday and vacation). The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


#Patrick's code that doesn't work
#weekday = False
#vacation = True
#def sleep_in(weekday, vacation):
#    if weekday:
#        return False
#    elif weekday & vacation:   ****'&' is not for python!***
#        return False
#    elif vacation & weekday:
#        return False
#    else:
#        return True

#sleep_in(weekday, weekday)

#Jay's code that does work
def sleep_in(weekday, vacation):
    if weekday == True and vacation == False:
        return False
    elif weekday == True or vacation == True:
        return True
    else:
        return True

print sleep_in(False, False)
print sleep_in(True, False)
print sleep_in(False, True)

#Jared's code that does work
def sleep_in(weekday, vacation):
    if weekday and not vacation:
        return False
    elif not weekday and not vacation:
        return True
    elif weekday and vacation:
        return True
    else:
        return True

print sleep_in(False, False)
print sleep_in(True, False)
print sleep_in(False, True)

#bob's code that is condensed
def sleep_in(weekday, vacation):
    return vacation or not weekday

print sleep_in(False, False)
print sleep_in(True, False)
print sleep_in(False, True)

