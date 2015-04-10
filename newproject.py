__author__ = 'patrickh'

person = {
    "name": {
        'first_name': "Patrick",
        'last_name': 'Harding',
        },
    "age": 31,
    'hair_color': 'brown',
    'eye_color': 'blue',
    'is_cool': True
}

# print person.get('hair_color')
# print person["is_cool"]
print person.items()

# things = person.keys()
# things.sort()
# print things
# my_tuple = ('thing1', 'thing2')
# item1, item2, = my_tuple
# print item1
# print item2

# for key, val in person.items():
#     print "%s is the key, and %s is the value" % (key, val)