#!/usr/bin/env python
"""
STOM.PY
Pipe in a JSON document, and the structure will be stomped
so that every value is prefixed with a dotted path key.
"""

import json
import sys


def stomp(J, prefix=''):
    if isinstance(J, dict):
        for k in sorted(J):
            p = ('%s.%s' % (prefix, k)) if prefix else k
            for line in stomp(J[k], prefix=p):
                yield line
    elif isinstance(J, list):
        for i, v in enumerate(J):
            p = ('%s.%i' % (prefix, i)) if prefix else '%i' % i
            for line in stomp(v, prefix=p):
                yield line
    else:
        yield '%s = %s' % (prefix, J)


if __name__ == '__main__':
    X = json.loads(sys.stdin.read())
    for line in stomp(X):
        print(line)
