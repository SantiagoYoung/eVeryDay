import tokenize




reader = open('/home/neon/catfile').next
# print reader
tokens = tokenize.generate_tokens(reader)
# print tokens
# print tokens.next()
# print tokens.next()



def power(values):
    for value in values:
        print 'powering %s' % value
        yield value


def adder(values):
    for value in values:
        print 'adding to %s' % value
        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2
elements = [1, 4, 7, 9, 12, 19]
res = adder(power(elements))

# print res.next()
# print res.next()
# print res.next()




def psychologist():
    print 'please tell me your problem.'
    while True:
        answer = yield
        if answer is not None:
            if answer.endswith('?'):
                print 'don"t ask '
            elif 'good' in answer:
                print 'good  and go.'
            elif 'bad' in answer:
                print 'bad u .'
free  = psychologist()
# print free.next(), '././././'
# print free.send('i feel bad')
# print free.send('why i am not?')
# print free.send('ok u bad son of bitch.')
# print free.throw(StandardError)
print free.close()



def my_generator():

    try:
        yield 'hello'
    except ValueError:
        yield 'dealing with the exception'
    finally:
        print 'ok let me go.'

gen = my_generator()
print gen.next()
print gen.throw(ValueError('mean'))
gen.close()
print gen.next()



















