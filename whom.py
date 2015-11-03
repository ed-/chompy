#!/usr/bin/env python
"""
WHOM.PY
Pipe in a prettytable document, and the table will be
whomped into a JSON document, a list of dictionaries
using the table headers as keys.
"""

import json
import sys


def whomp(table):
    keys, rows = [], []
    for line in table.split('\n'):
        if not line or line.startswith('+'):
            continue
        line = line.strip('|')
        columns = [col.strip() for col in line.split('|')]
        if not keys:
            keys = columns
        else:
            rows.append(dict(zip(keys, columns)))
    return rows


if __name__ == '__main__':
    X = sys.stdin.read()
    X = whomp(X)
    print(json.dumps(X, indent=2, sort_keys=True))
