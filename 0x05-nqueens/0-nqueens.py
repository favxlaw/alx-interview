#!/usr/bin/python3
""" N queens """
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])

def queens(n, i=0, a=[], b=[], c=[]):
    """ find possible positions """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                # yields a list of rows. We need to store the positions of queens in each row.
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a

def solve(n):
    """ solve """
    k = []
    for solution in queens(n):
        for i, s in enumerate(solution):
            k.append([i, s])
        print(k)
        k = []

solve(n)
