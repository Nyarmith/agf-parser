#!/usr/bin/env python3
import sys
import agf_parser as ap

def usage():
    print("Usage: {} adventure-file.json".format(sys.argv[0]))

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        usage()
        sys.exit(0)

    game = ap.loadAGF(sys.argv[2])

    while (not game.isEnd()):
        print(game.state())
        print("--------\n")
        choices = ap.choices()
        for ch in choices:
            print( choices )
        c = -1
        while ( c <=0 and c>len(c) ):
            c = read("Choose an option [1-{}]: ".format(len(c)))

        game.choose(c - 1)
        print("vvvvvvvv")

    print("^^^^^^^^\n")
    if ( game.isWin() ):
        print("Congratulations, you've won!\n")
    else:
        print("Unfortunately, it looks like you've hit a dead end!\n")
