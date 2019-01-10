#!/usr/bin/env python
import sys
import collections
from math import sqrt
import math

class Z(object):

    def pFactors(self, n):
        """Finds the prime factors of 'n'"""

        pFact, limit, check, num = [], int(sqrt(n)) + 1, 2, n
        if n == 1: return [1]
        for check in range(2, limit):
             while num % check == 0:
                pFact.append(check)
                num /= check
        if num > 1:
          pFact.append(num)
        return pFact

    def calc_z(self, n):
        '''For any positive integer N, Z(N) is the number of
        zeros at the end of the decimal form of number N!'''
        pfacts = []
        for i in range(n):
            pfacts = pfacts +self.pFactors(i+1)

        cntr = collections.Counter(pfacts)
        return min(cntr[2], cntr[5]) + cntr[10]

if __name__ == '__main__':
    num = None
    while True:
        try:
            _l = int(input())
        except EOFError:
            break

        if num == None:
            num = _l
        else:
            print(Z().calc_z(_l))
            if num > 0:
                num -= 1
            else:
                break
