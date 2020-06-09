#!/usr/bin/env python3.7

a = int(input())
b, c = [int(i) for i in input().strip().split()]
s = input().strip()
print('{} {}'.format(a+b+c, s))
