# is this finished ???


def open_text(text_file):
    try:
        with open(text_file, 'r') as f:
            f.read()
    except IOError:
        print "That is an invalid file name!"


def open_file(text_file):
    with open(text_file, 'r') as f:
            f.read()

print open_text('text_file.txt')
try:
    open_file('text_file.txt')
except IOError:
    print "That file does not exist!"