#!/usr/bin/python

import collections
import itertools
import sys

with open('file1') as f:
    before = collections.deque(maxlen=10)
    for line in f:
        if 'when' in line:
            sys.stdout.writelines(before)
            sys.stdout.write(line)
            sys.stdout.writelines(itertools.islice(f, 10))
            break
        before.append(line)
