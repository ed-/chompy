#!/usr/bin/env python

from fileinput import input as stdin
from json import dumps, loads
from sys import argv

text = []
for line in stdin([]):
    text.append(line.rstrip())

# Ignore junk like HTTP headers and curl feedback.
while text and not text[0].startswith('{'):
    text = text[1:]

obj = loads('\n'.join(text))

for key in argv[1:]:
    try:
        obj = obj[key]
    except TypeError:
        obj = obj[int(key)]

print dumps(obj, sort_keys=True, indent=2)
