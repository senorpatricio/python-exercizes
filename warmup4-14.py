

def make_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)

print make_tags("i", "yes")


class Parent(object):
    def implicit(self):
        print "PARENT implicit()"

    def explicit(self):
        print "Parent explicit()"

    def altered(self):
        print "Parent altered"


class Child(Parent):
    def explicit(self):
        print "Child explicit()"

    def altered(self):
        print "Child before Parent altered()"
        super(Child, self).altered()
        print "Child after parent altered()"


dad = Parent()
son = Child()
#
# dad.implicit()
# son.implicit()
#
# dad.explicit()
# son.explicit()

dad.altered()
son.altered()