
def main():
    # remove the pass statement and write your program here.
    name = "hungriers"
    print(name[0])
    print(name[1])
    print(name[2])
    print(name[3])
    print(name[4])
    print(name[5])
    print(name[6])
    print(name[7])


    print(name[:0])
    print(name[:1])
    print(name[:2])
    print(name[:3])
    print(name[:4])
    print(name[:5])
    print(name[:6])
    print(name[:7])
    print(name[:8])
    print(name[:9])



    print(name[0:])
    print(name[1:])
    print(name[2:])
    print(name[3:])
    print(name[4:])
    print(name[5:])
    print(name[6:])
    print(name[7:])
    print(name[8:])
    print(name[9:])

    print(len(name))
    print(name[len(name)-1:])
    print(name[1:len(name)-1])
    a = int((len(name)-3)/2)
    print(name[0:a])
    b = int((len(name)+1)/2+1)
    print(name[b:len(name)])

    print(name.index("h"))
    print(name.index("u"))
    print(name.index("n"))
    print(name.index("g"))
    print(name.index("r"))
    print(name.index("i"))
    print(name.index("e"))
    print(name.index("r"))
    print(name.index("s"))

    print(len("what does the fox say"))

    d = "sun"
    print(d[:3])
    print(d[:2])
    print(d[:1])
    print(d[:0])
    w = "david wippman"
    print(w[13:42])
    print(d[2:47])

    my_string = "the cat and this dog are in the garden"
    x = my_string.split(' ', 1)[0]
    z = my_string.split(' ', 1)[1]
    print(x)
    print(z)

    print(my_string[0:my_string.index(" ")+1])
    print(my_string[my_string.index(' ')+1:len(my_string)])


    sentence = str(input('enter a sentence'))
    print(sentence[:sentence.index(" ")])
    print(sentence[sentence.index(' ')+1:])

if __name__ == "__main__":

    main()
