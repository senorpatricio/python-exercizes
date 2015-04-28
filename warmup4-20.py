my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = [x**2 for x in my_list]

print new_list

newer_list = [x**2 for x in my_list if x % 2 == 0]

print newer_list

old_way_list = []
for item in my_list:
    if item % 2 == 0:
        old_way_list.append(item**2)

print old_way_list

newest_list = [x**2 if x % 2 == 0 else x**3 for x in my_list]

print newest_list

# ----------------------------------------------------
# functions

# named variables

def foo(a, b, c, d):
    print a, b, c, d

foo("hello", "World", "I'm", "Patrick")

