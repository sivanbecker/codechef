#!/usr/bin/env python

t=int(input())
for a0 in range(t):
    n=int(input())
    i=0;sum=0
    while((5**i)<=n):
        sum+=n//(5**i)
        i+=1
    print(sum-n)
