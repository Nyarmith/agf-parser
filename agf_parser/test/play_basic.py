#!/usr/bin/env python3

import agf_parser as ap

ag = ap.loadAGF('basic_yn.json')

print(ag.state())
print(ag.choices())
ag.choose(1)
print(ag.state())
print(ag.choices())
