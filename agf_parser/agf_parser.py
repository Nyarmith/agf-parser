#!/usr/bin/env python3
import json

class adventureGame:
    def __init__(self):
        self.states = {}    #save game-related states
        self.data   = None  #the description of the game
        self.pos    = None  #ptr to current place in game
        self.xpand  = None  #expanded storage for current state
    def choose(self, c):
        #input choice c and progress game
        nextNode = self.data[self.pos][c][-2]
        self.parseNode(nextNode)
        self.pos = nextNode

    def state(self):
        #show current state, return current state text
    def choices(self):
        ch = self.data['states'][self.pos]
        return 
        #list current choices
    #private
    def parseNode(self,n):
        #parse the XML conditions in a string
        #process the functional portion of node n
        # to stuff w/ self.xpand

    def isEnd(self):
        #shouldn't point to any other nodes
        #might want to implement this after doing parseNode

    def isWin(self):
        return self.pos in self.data['end']

def parseAGF(s):
    #turn string s into AGF
    ag = adventureGame()
    ag.data = json.loads(ag.data)
    ag.pos  = ag.data['start_state']

def serialize(ag):
    #turn adventureGame object into string
    return json.dumps(ag.data)

#load a .agf file
def loadAGF(f):
    with open(f) as fd:
        ag = parseAGF(fd.read())
    return ag

def saveAGF(ag, fn):
    with open(fn,'w') as fd:
        fd.write(serialize(ag)


