def number_words(text):
    print('String-', text)
    no_of_words = 1
    for ch in text:
        if (ch == ' ' or ch == '\t' or ch == '\n'):
            no_of_words += 1
    print('Total number of words in String', no_of_words)

s = 'This Python program counts\tnumber of words in a String.'
number_words(s)
