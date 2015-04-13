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
        print result
        z += 1
        f.write('\n' + result)
        solution = Counter(result)
        print solution
        for key, value in result:
            print
        # for line in result:
        #     for letter in line:
        #         count = 0
        #         word = letter
        #         print word + '\n',
        #         count += 1
