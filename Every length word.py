f = []

def evenLengthwords(sentence):

    l = sentence.split(" ")

    for i in l:

        if len(i) % 2 == 0:

            f.append(i)

    print(' '.join(f))

evenLengthwords("i am python")
