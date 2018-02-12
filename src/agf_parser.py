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
    def state(self):
        #show current state, return current state text
    def chocies(self):
        #list current choices
    #private
    def parseNode(self,n):
        #parse the XML conditions in a string
        #process the functional portion of node n
        # to stuff w/ self.xpand

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


