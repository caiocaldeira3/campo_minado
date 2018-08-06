from random import randrange
from bombas import *

def init_minefield(lins, cols, num_bombs):
    minefield = [[inactive_bomb(y, x) for x in range(cols)] for y in range(lins)]

    i = 0
    while i < num_bombs:
        x, y = randrange(lins), randrange(cols)
        if minefield[x][y].active == 0:
            minefield[x][y] = active_bomb()
            i += 1

    for x in range(lins):
        for y in range(cols):
            if not minefield[x][y].active:
                minefield[x][y].calc_value(minefield)

    return minefield


def print_minefield(minefield, lins, cols):
    for i in range(cols+1):
        print('|----'.format(), end = '')
    print('|')

    print('| // ', end = '')
    for x in range(cols):
        print('|{:^4}'.format(x), end = '')
    print('|')

    for i in range(cols+1):
        print('|----'.format(), end = '')
    print('|')

    for x in range(lins):

        print('|{:^4}'.format(x), end = '')
        for y in range(cols):
            print('|{:^4}'.format(minefield[x][y].show), end = '')
            #print('|{:^4}'.format(minefield[x][y].value), end = '')
        print('|')

        for i in range(cols+1):
            print('|----'.format(), end = '')
        print('|')

    return None

def print_minefield_showed(minefield, lins, cols):
        for i in range(cols+1):
            print('|----'.format(), end = '')
        print('|')

        print('| // ', end = '')
        for x in range(cols):
            print('|{:^4}'.format(x), end = '')
        print('|')

        for i in range(cols+1):
            print('|----'.format(), end = '')
        print('|')

        for x in range(lins):

            print('|{:^4}'.format(x), end = '')
            for y in range(cols):
                print('|{:^4}'.format(minefield[x][y].value), end = '')
            print('|')

            for i in range(cols+1):
                print('|----'.format(), end = '')
            print('|')

        return None

def check_flags(minefield, lins, cols):

    for x in range(lins):
        for y in range(cols):
            if minefield[x][y].active == 1 and minefield[x][y].flagged == 0:
                return 0
            if minefield[x][y].active == 0 and minefield[x][y].flagged == 1:
                return 0
    return 1

def check_bombs(minefield, lins, cols):
    for x in range(lins):
        for y in range(cols):
            if minefield[x][y].active == 0 and minefield[x][y].show == '--':
                return 0
    return 1
