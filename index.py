# learning playground

# function and conditional practice
def testFunction(name, config):
    if name:
        name = name
    else:
        name = 'James Robinson'
    # print name 10 times with for loop if specified in config
    if config['toPrint']:
        for i in range(10):
            if config['caps']:
                print(name.upper())

testFunction('John Doe', { 'toPrint': True, 'caps': True})

# list practice
def testLists(names):
    if isinstance(names, list):
        # list is passed in
        names.reverse()
        for i in names:
            print(i.capitalize())
    else:
        raise Exception('Please pass in a list of names')

testLists(['james', 'kevin', 'joe', 'Katie', ''])

# tuple practice
def testTuple(toTuple):
    if isinstance(toTuple, tuple):
        # if tuple already, throw exception
        raise Exception('Object is already a tuple')
    else:
        print(tuple(toTuple))

testTuple([12, 45, 6, 79, 105])