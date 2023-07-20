#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n == 0:
      fb=[]
      return fb
    elif n==1:
      fb=[0]
      return fb
    else: 
      fb = [0,1]
    for i in range(2, n):
                fb.append(fb[i-1] + fb[i-2])
    return fb
