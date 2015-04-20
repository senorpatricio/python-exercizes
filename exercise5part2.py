from collections import Counter

#
# import re
# words = re.findall(r'\w+', open('AliceInWonderland.txt').read().lower())
# print Counter(words).most_common(5)

# this is a different way to do it, but doesn't sort by occurrence
with open('AliceInWonderland.txt', 'r') as f:
    wordcount = {}
    for word in f.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    for key in wordcount.keys():
        print ("%s %s " % (key, wordcount[key]))