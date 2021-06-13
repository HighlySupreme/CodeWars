# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

# test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
# test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')

def pig_it(text):
    theWords = text.split()
    for index, x in enumerate(theWords):
        theWords[index] = x[1:] + x[:1] + "ay"

    return " ".join(theWords)



