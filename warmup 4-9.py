__author__ = 'patrickh'


# my code that kinda works
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False

print monkey_trouble(True, True)
print monkey_trouble(False, False)
print monkey_trouble(True, False)
print monkey_trouble(False, True)


# alex's code that is condensed
def monkey_trouble(a_smile, b_smile):
    return (a_smile and b_smile) or (not a_smile and not b_smile)


print monkey_trouble(True, True)
print monkey_trouble(False, False)
print monkey_trouble(True, False)
print monkey_trouble(False, True)

# Jay's condensed code
def monkey_trouble(a_smile, b_smile):
    return a_smile is b_smile  # essentially if a_smile is not the same as b_smile we are in trouble


print monkey_trouble(True, True)  # Want True
print monkey_trouble(False, False)  # Want True
print monkey_trouble(False, True)  # Want False
print monkey_trouble(True, False)  # Want False

# Chinmay's code using xor
def monkey_trouble(a_smile, b_smile):
    return not (a_smile ^ b_smile)

print monkey_trouble(True, True)
print monkey_trouble(True, False)
print monkey_trouble(False, True)
print monkey_trouble(False, False)