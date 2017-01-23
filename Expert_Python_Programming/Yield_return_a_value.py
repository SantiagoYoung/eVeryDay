def shorten(_list):
    length = len(_list[0])
    for s in _list:
        length = yield s[:length]

ml = ['loremipsum', 'dolorsit', 'ametfoobar']
shortstring = shorten(ml)
result= []

try:
    s = next(shortstring)
    print s, 'OOOOOOOOOOOO'
    result.append(s)
    while True:
        number_of_vowels = len(filter(lambda letter: letter in 'aeiou', s))
        print number_of_vowels,'<<<<<<<<<<<<,'
        s = shortstring.send(number_of_vowels)
        result.append(s)
except StopIteration:
    pass
print result