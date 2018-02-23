#!/usr/bin/env python3

import unittest
import agf_parser as ap

class TestAGF(unittest.TestCase):
    def test_foo(self): #methods that start with test_ are discovered and run?
        self.assertEqual(2,2)

#ag = ap.loadAGF('basic_yn.json')
#
#print(ag.state())
#print(ag.choices())
#ag.choose(1)
#print(ag.state())
#print(ag.choices())
