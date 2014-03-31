#!/usr/bin/env python

from fileinput import input as stdin
from json import dumps

def get_text_from_stdin():
    text = []
    for line in stdin([]):
        l = line.strip()
        if l.startswith('|') or l.startswith('+'):
            text.append(l.rstrip())
    return '\n'.join(text)

def detablize(text):
    keys = []
    rows = []
    for line in text.split('\n'):
        if line.startswith('+'):
            continue
        line = line.strip('|')
        columns = [x.strip() for x in line.split('|')]
        if not keys:
            keys = columns
        else:
            row = dict(zip(keys, columns))
            rows.append(row)
    return rows

if __name__ == '__main__':
    from sys import argv
    text = get_text_from_stdin()
    obj = detablize(text)
    for key in argv[1:]:
        try:
            obj = obj[key]
        except TypeError:
            obj = obj[int(key)]
    print dumps(obj, sort_keys=True, indent=2)
