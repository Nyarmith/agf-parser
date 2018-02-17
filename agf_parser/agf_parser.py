#!/usr/bin/env python3
import json #file format
import re  #regexp

#to use for parsing stuff
xml_regex = "(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>"
subst_vars = [r'^(\w+)::(\w+)$',r'self.states[\1][\2]']

class adventureGame:
    def __init__(self):
        self.states  = {}    #save game-related states
        self.data    = None  #the description of the game
        self.pos     = None  #ptr to current place in game
        self.choices = []
    def choose(self, c):
        #input choice c and progress game
        nextNode = self.data['states'][self.pos][c][-2]
        self.parseNode(nextNode)
        self.pos = nextNode

    def state(self):
        #show current state, return current state text

    def choices(self):
        ch = self.data['states'][self.pos]['options']
        self.choices = []
        for c in ch:
            if (checkCondition(c[):
                self.choices = 

    #private
    def parseNode(self,node):
        strng      = ''
        n = self.data['states'][node]
        xml_parts  = re.finditer(xml_regex, n['text'])
        # do stuff with each xml match

    def isEnd(self):
        if (len(self.data['states'][self.pos]['options']) == 0):
            return True
        else:
            return False

    def isWin(self):
        return self.pos in self.data['states']['win_states']

    def evaluateStrExpression(self, expr):
        try:
            eval(substPythonString(expr))
        except:
            return 0;

    def substPythonString(self, expr):
        return re.sub(subst_vars[0], subst_vars[1], expr)

    def setVar(self, name, val):
        namespace,var = name.split('::')
        try:
            self.states[namespace]
        except:
            self.states[namespace] = {}
        states[namespace][var] = val

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


