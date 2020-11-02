# LEGB RULE
# LOCAL
def report():
    # LOCAL ASSIGNMENT
    x = 'local'
    print(x)


# ENCLOSING
x = 'THIS IS GLOBAL LEVEL'


def enclosing():
    x = ' Enclosing Level'

    def inside():
        # LEGB
        # x = 'local'
        print(x)

    inside()


enclosing()

x = 'outside'


def report():
    # HEY GRAB THE GLOBAL LEVEL x VARIABLE!
    global x
    # REASSIGN GLOBAL x
    x = 'inside'
    return x


print(report())
print(x)