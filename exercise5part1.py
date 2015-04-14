# Your program will write out 10 strings of random characters (of random length) to a file called exercise_five.dat
import random
from collections import Counter


def random_alphanumeric(limit):
    r = (range(48, 58) + range(65, 91) + range(97, 123))
    random.shuffle(r)
    return reduce(lambda i, s: i + chr(s), r[:random.randint(0, len(r))], "")


with open('exercise_five.dat', 'w+') as f:
    z = 0
    while z < 10:
        result = random_alphanumeric(2)
        # print result
        f.write(result + '\n')
        z += 1
    f.close()
# Jared's helpful code
with open("exercise_five.dat", 'r') as f:
    all_chars_count = 0
    all_chars = ""
    for line in f.readlines():
        line = line.strip()
        all_chars += line
        all_chars_count += len(line)
        print line + "\nTotal Characters for the above string: " + str(len(line)) + "Most Common: "
        print Counter(line).most_common()
        print "~" * 75
    print "\n" + "~" * 75 + "\nTotal of each character in all of the strings above: " + str(all_chars_count) + "\nMost common: "
    print Counter(all_chars).most_common()
    print "~" * 75