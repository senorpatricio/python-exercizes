from collections import Counter
import random
import string


__author__ = 'jared'


def generate_random_string():
    symbols = "!@#$%^&*()_+-=/|{}\\<>?`~"
    size = random.randint(1, 500000)
    return "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + symbols)
                   for _ in range(size))


def main():
    with open("exercise_five.dat", "w+") as f:
        for x in range(0, 10):
            data = generate_random_string()
            f.write(data + "\n")
        f.close()
    with open("exercise_five.dat", 'r') as f:
        all_chars_count = 0
        all_chars = ""
        for line in f.readlines():
            line = line.strip()
            all_chars += line
            all_chars_count += len(line)
            print line + "\n" + "*"*220 + "\nTotal Characters for the above string: " + str(len(line)) + "\nMost Common: "
            print Counter(line).most_common()

        print "\n" + "*"*220 + "\nTotal characters for all of the above strings: " + str(all_chars_count) + "\nMost common: "
        print Counter(all_chars).most_common()




if __name__ == '__main__': main()