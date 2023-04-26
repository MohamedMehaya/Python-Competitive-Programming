import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
c = 0
for i in input().split():
    x = sum(int(y) for y in i)
    c += x

print(c)

