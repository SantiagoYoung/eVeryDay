

def psychologist():

    print 'Please tell me your problems.'
    while True:
        answer = (yield )
        print answer,"[][][]"
        if answer is not None:
            if answer.endswith('?'):
                print " don't ask yourself too much questions"
            elif 'good' in answer:
                print " a that's good , go on"
            elif 'bad' in answer:
                print "don't be so negative."

# free = psychologist()
# free.next()
#
# free.send('I feel bad')
# free.send('why i should"t ?')
# free.send('ok then i should find what is good for me')



def my_generator():
    try:
        yield 'something'
    except ValueError:
        yield 'dealing with the exception'
    finally:
        print 'ok let"s clean.'

gen = my_generator()
print gen.next()
print gen.throw(ValueError('mean mean mean'))
print gen.close()







