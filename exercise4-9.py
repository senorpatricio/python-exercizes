__author__ = 'patrickh'

my_list = [1, 2, 3, 'hello']
my_list.append([4,5])
print my_list

my_list.insert(2, "hi")
print(my_list)

item = my_list.pop()
print 'last item was: ' +str(item)

the_list = [1, 841818, 15, 1, 8151, 215, 56, 35, 484, 321654, 6984, 63251, 6, 65496, 65, 6498, 3241]
the_list.sort()
print the_list