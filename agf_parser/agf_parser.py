#!/usr/bin/env python3
import json
import re
import random
from lxml import etree

#to use for regex parsing stuff
subst_vars  = [r'(\w+)::(\w+)',r'self.states["\1"]["\2"]']
misc_substs = [r'true',r'True']

"""
This module lets you import and query adventure-game-format files as documented here https://docs.google.com/document/d/1ZAJcbe_a729lz6I1N9DyvFBcn74Mggtkr1RtJAPfS-Q/edit?usp=sharing
"""


class adventureGame:
    """
    This class holds the adventure game json object and allows you to navigate throughit, holding data to maintain the state of the game.
    """
    def __init__(self):
        self.title   = None  #given title of adventure
        self.states  = {}    #save game-related states
        self.data    = None  #the description of the game
        self.pos     = None  #ptr to current place in game
        self.choices = []    #current valid choices and their mappings to original choices
        self.text    = ''    #current text after processing

    def start(self):
        """
        Method must be called when starting a game
        """
        self.title = self.data['title']
        self.states = self.data['gamevars']
        self.pos = self.data['start_state']
        start_node = self.data['states'][self.pos]
        self.pruneChoices(start_node)
        self.processText(start_node)


    def choose(self, c):
        """
        Pass the integer c to pick from the list of valid choices
        """
        #translate choice c to og choices
        c = self.choices[c][0]
        c = self.data['states'][self.pos]['options'][c]

        #random transition are marked by the transition option being a list of options
        if isinstance(c[-2], list):
            pos = random.choice(c[-2])
        else:
            pos = c[-2] 
        #pos is a string of the nextNode

        nextNode = self.data['states'][pos]        #nextNode(var)
        #get parts of the node

        #==== main transition steps ====
        self.execStmt(c[1])          # execute transition function
        self.pruneChoices(nextNode)  # prune the choices the user can pick
        self.processText(nextNode)   # process text based on env states
        self.pos = pos               # finally, set our position string
    
    def adventureTitle(self):
        """
        returns adventure's given name
        """
        return self.title
    
    def state(self):
        """
        returns current state text
        """
        return self.text

    def getChoices(self):
        """
        returns an ordered list of strings describing the current player choices
        """
        return [c[-1] for c in self.choices]

    def pruneChoices(self, node):
        """
        given a node, filers the valid choices a player can make and stored them
        internally
        
        you can get later get these choice with method getChoices()
        """
        ch = node['options']
        self.choices = []
        for i in range(0,len(ch)):
            c = ch[i]
            if (c[0] == '' or self.evalStmt(c[0])):  #is choice valid?
                flavorText = c[-1]
                self.choices.append([i,flavorText])

    def processText(self,node):
        """
        given a node, uses the current state of the game to parse any
        conditions or xml tags in the node description and produce the
        final string that the user will see

        you can get the result of this method with method state()
        """
        #parse string to display
        #n = self.data['states'][node] #im now passing this directly
        text = '<base>' + node['text'] + '</base>'
        root = etree.fromstring(text)
        self.text = self.parseXML(root)

    def parseXML(self, root):
        """
        given an xml node in the current game's state-text, compose a string
        from its contents and all valid subnodes and return it
        """
        strng = ''
        strng += root.text
        for i in root.getchildren():  #this is where we define the tag types, could use dict for switch/case logic here
            if (i.tag == 'cond' and self.evalStmt(i.attrib['expr'])):
                strng += self.parseXML(i)
            strng += i.tail
        return strng

    def isEnd(self):
        """
        test if the current node is an end-state
        (i.e. if it has no connections to other nodes)
        """
        if (len(self.data['states'][self.pos]['options']) == 0):
            return True
        else:
            return False

    def isWin(self):
        """
        test if the current node is a win-state
        """
        return self.pos in self.data['win_states']

    def execStmt(self, expr):
        """
        execute the given state-modification string
        """
        try:  #just turning it into a valid python expression
            exec(self.substPythonString(expr))
        except:
            return False

    def evalStmt(self, expr):
        """
        return the value of a state expression
        """
        try:
            return eval(self.substPythonString(expr))
        except:
            return 0

    def substPythonString(self, expr):
        """
        turns the game's syntax into a valid python expression
        """
        #this is really exploitable without additional checks
        expr = re.sub(subst_vars[0], subst_vars[1], expr)
        expr = re.sub(misc_substs[0], misc_substs[1], expr)
        return expr


def parseAGF(s):
    """
    turn a valid adventure-game-format string into an AdventureGame object
    """
    #turn string s into AGF
    ag = adventureGame()
    ag.data = json.loads(s)
    ag.start()
    return ag

def serialize(ag):
    """
    turn an AdventureGame object into an equivalent string
    """
    #turn adventureGame object into string
    return json.dumps(ag.data)

#load a .agf file
def loadAGF(f):
    """
    load AdventureGame from file
    """
    with open(f) as fd:
        ag = parseAGF(fd.read())
    return ag

def saveAGF(ag, fn):
    """
    save AdventureGame object to file
    """
    with open(fn,'w') as fd:
        fd.write(serialize(ag))


