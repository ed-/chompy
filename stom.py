#!/usr/bin/env python

from fileinput import input as stdin
from json import dumps, loads

def get_text_from_stdin():
    text = []
    for line in stdin([]):
        text.append(line.rstrip())
    while text and not text[0].startswith('{'):
        text = text[1:]
    return '\n'.join(text)

def replace_annoying_chars(text):
    t = text
    replacements = [
        ("'", '"'),
        ('u"', '"'),
        ("True", '"True"'),
        ("False", '"False"'),
        ("None", '"None"'),
        ("<", '"<'),
        (">", '>"'),
        ]

    for a, b in replacements:
        t = t.replace(a, b)
    return t

def flatten(obj, prefix=''):
    if type(obj) == dict:
        for k, v in obj.items():
            p = ('%s.%s' % (prefix, k)) if prefix else k
            for line in flatten(v, prefix=p):
                yield line
    elif type(obj) == list:
        for k, v in enumerate(obj):
            p = ('%s.%s' % (prefix, k)) if prefix else k
            for line in flatten(v, prefix=p):
                yield line
    else:
        yield '%s = %s' % (prefix, obj)


if __name__ == '__main__':
    text = get_text_from_stdin()
    text = replace_annoying_chars(text)
    for line in flatten(loads(text)):
        print line
