#!/usr/bin/env python
"""
CHOM.PY
Pipe in a JSON document, and include a list of keys to drill
into. Chompy will return only the subset of the document reached
via that path. Lists of dictionaries support a key=value notation.
"""

import json
import sys


def chomp(J, keys=None):
    if not J or not keys:
        return J
    k = keys.pop(0)
    if isinstance(J, dict):
        return chomp(J[k], keys)
    if isinstance(J, list) and isinstance(k, int):
        return chomp(J[k], keys)
    elif isinstance(J, list) and isinstance(k, str):
        if '=' not in k:
            return chomp(J[int(k)], keys)
        kk, vv = k.split('=', 1)
        for i in J:
            if not isinstance(i, dict):
                continue
            if i[kk] == vv:
                return chomp(i, keys)
        else:
            return chomp([], keys)


if __name__ == '__main__':
    X = json.loads(sys.stdin.read())
    X = chomp(X, sys.argv[1:])
    print(json.dumps(X, indent=2, sort_keys=True))
