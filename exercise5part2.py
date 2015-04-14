from collections import Counter
#     print "~" * 75
#     print "\n" + "~" * 75 + "\nTotal of each character in all of the strings above: " + str(all_chars_count) + "\nMost common: "
#     print Counter(all_chars).most_common()
#     print "~" * 75


import re
words = re.findall(r'\w+', open('AliceInWonderland.txt').read().lower())
print Counter(words).most_common()


