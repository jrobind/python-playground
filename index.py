# learning playground

from datetime import datetime

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

# class practice
class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def printIntro(self):
        print(f"Hello I'm {self.name}, I am {self.age} years old and I am a {self.occupation}.")

    def calculateDrinkAge(self):
        if self.age > 18:
            print('I can legally buy alcohol in the UK')
        else:
            print('I cannot legally buy alcohol in the UK')
    
james = Person('James Robinson', 27, 'Developer')
andrew = Person('Andrew Doe', 17, 'Waiter')

james.printIntro()
james.calculateDrinkAge()
andrew.printIntro()
andrew.calculateDrinkAge()

# decorators practice
def my_decorator(fn):
    def wrapper():
        return fn() + ' From the decorator!'
    return wrapper

# decorators wrap a function, modifying its behavior.
@my_decorator
def greeting():
    return 'Hello!'

print(greeting())

def greet_during_day(fn):
    def wrapper():
        if datetime.now().hour < 18:
            return fn() + ' From the decorator!'
        else:
            pass
    return wrapper

@greet_during_day
def greet():
    return 'Good day!'

print(greet())

# read and write practice
test_file_w = open('./test.txt', 'w')

# write
test_file_w.write('Hello World')
test_file_w.close()

# read
test_file_r = open('./test.txt', 'r')
print(test_file_r.read())

# looping over file contents
file = open('./test.txt', 'r')

for line in file:
    print(line)