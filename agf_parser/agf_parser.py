#!/usr/bin/env python3
import json #file format
import re  #regexp

#to use for parsing stuff
xml_regex = "(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>"

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

    def checkCondition(self, strng):
        if strng == 'R' or strng == '':
            return True

        conds = strng.split('&&')
        ret = True
        for c in conds:
            expr = c.split(' ')
            left  =  getVar(expr[0])
            mid   =  expr[1]
            right =  getVar(expr[2])
            ret = ret and eval(str(left)+mid+str(right))

        return l

    def runCode(self, strng):
    #TODO
        stmt = #find and repalce all a::b things with self.state[a][b]
        try:
            ret = eval(stmt)
        except:
            ret = false
        return ret

    def getVar(self, name):
        if name.isdigit():
            return name.isdigit()

        namespace,var = name.split('::')
        try:
            ret = self.states[namespace][var]
        except:
            ret = 0
        return ret


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


