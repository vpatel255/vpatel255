#!/usr/bin/env python3

'''
generate a list of random numbers and letters
'''

import sys
import random as r
import os

names = ['alpha', 'beta', 'gamma', 'test', 'example', 'banana', 'orange', 'apple', 'capybara', 'kangaroo', 'network',
         'program', 'quiz', 'output']

suffixes = ['jpg', 'png', 'gif', 'txt', 'md', 'docx', 'rtf', 'csv', 'pdf', 'py', 'sh', 'bash', 'html', 'exe', 'conf',
            'hex']

numbers = range(0, 9)


def randofilename(percentage=60):
    maxrange = (100 - percentage) + 1
    if r.randint(0, maxrange) == 0:
        return r.choice(names) + str(r.choice(numbers))
    else:
        return r.choice(names) + str(r.choice(numbers)) + '.' + r.choice(suffixes)


def randotouch(randofile):
    x = os.system('touch ' + 'test/' + randofile)
    if x:
        print('An error occurred.')


def headsortails(percentage):
    "given a percentage chance of true, flip a coin"
    max = (100 - percentage) + 1
    fraction = (r.randint(0, max)) / 100
    return bool(fraction)


def randofile(file, filesize, outputfile='test/datafile.txt'):
    with open(outputfile, 'a') as f:
        f.write(file + ':' + str(filesize) + '\n')


def write_bytes(filename, numbytes):
    "fill up file with specified data"
    stringthing = "All work and no play makes Jack a dull boy."
    complete = len(stringthing) + 1  # add 1 for newline character
    count = numbytes
    f = open('test/' + filename, 'w')
    while count > complete:
        f.write(stringthing + '\n')
        count -= complete
    count2 = count
    while count2 > 0:
        x = count - count2
        if x == len(stringthing):
            x = 0
        f.write(stringthing[x])
        count2 -= 1
    f.close()


if __name__ == "__main__":
    try:
        total = sys.argv[1]
    except:
        total = 20
    os.system('mkdir test')
    for i in range(0, int(total)):
        dog = randofilename()
        size = r.randint(0, 7680)
        if headsortails(60):
            randofile(dog, size)
            randotouch(dog)
            write_bytes(dog, size)
        elif headsortails(50):
            randofile(dog, size)
            randotouch(dog)
            write_bytes(dog, r.randint(0, 7680))
        elif headsortails(50):
            randotouch(dog, size)
        else:
            randofile(dog, size)

    # numlines = 15
    # for i in range(0, 21):
    #     print(randofilename())
    # randofile('files.txt')
    # randotouch()

    # write_bytes('test.txt', 150)
    # make about 20 filenames/sizes
    # of the 20,
    # choose if going into file, touch or both
    # then do those.
    # one func writes a name to file
    # one func touches it


