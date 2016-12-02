
# Iterables
'''
when u create a list,
u can read its items one by one,
reding its items one by one is called iteration.
'''
mylist = [1, 2, 3]
for i in mylist:
    print i

# everything u can use 'for ... in ...' on is iterable: list, strings, files...

# Generators
'''
Generators are iterators, but u can only iterate over them once.
it's because they do not store all the values in memory,
they generate the values on the fly.
'''
mygenerator = ( x*x for x in range(3))
for i in mygenerator:
    print i

# Yield
'''
Yield is a keyword that is used like return ,
except the function will return a generator.
'''
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i
mygenerator  = createGenerator()
print mygenerator

# when u call the function , the code you have
# written in the function body does not run.


# Controlling a generator exhaustion
class Bank(object):

    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield '$100'


hsbc = Bank()
atm = hsbc.create_atm()

print atm.next()
print [atm.next() for i in range(3)]
hsbc.crisis = True
# print type(atm.next())


# Itertools, your best friend


import itertools
horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
print races
print list(races)


