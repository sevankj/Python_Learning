class Parent(object):
    'Thiru'

    def override(self):
        print "PARENT override()"


class Child(Parent):
    def override(self):
        print "CHILD override()"


dad = Parent()
son = Child()

dad.override()
son.override()

print "Employee.__doc__:", Parent.__doc__
