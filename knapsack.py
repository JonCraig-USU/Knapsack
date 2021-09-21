from random import random, randint

from numpy import inf
import nimTime
import math

# test arrarys with known solutions
# s = [None, 7, 5, 8, 8, 3, 4]
# v = [None, 2.5, 6.3, 1.3, 8.5, 5.0, 3]


''' recursive alogorithm for solving knapsack problem '''
def knapsack(n, kA, kB):
    global s
    global v
    # if the bag over flows, remove item
    if kA < 0 or kB < 0:
        return (-math.inf)

    # if run out of items, end
    elif n <= 0:
        return 0

    # continue recursing
    else:
        return max(
            v[n] + knapsack(n-1, kA-s[n], kB),
            v[n] + knapsack(n-1, kA, kB-s[n]),
            knapsack(n-1, kA, kB)
            )

# test cases
# print("knap(6, 10, 12) = " + str(knapsack(6, 10, 12)))   # 22.8
# print("knap(6, 15, 15) = " + str(knapsack(6, 15, 15)))   # 25.3
# print("(knap(6, 8, 8) = " + str(knapsack(6, 8, 8)))      # 19.8
# print("(knap(2, 8, 8) = " + str(knapsack(2, 8, 8)))      # 8.8

'''
Code to be used for the timing study'''
def probGen(N, aveSize):
    s = [None] * (N+1)
    v = [None] * (N+1)
    for i in range(1, N+1):
        s[i] = randint(1, 2*aveSize)
        v[i] = random() * 20
    return (s, v)

# test the problem generator script 
# print(probGen(8, 5))   

def timingTest(n):
    global s
    global v
    s, v = probGen(30, 3)
    knapsack(n, 12, 15)

# time graph for the recursive algorithm
# nimTime.showTime(timingTest, [5, 10, 15, 20])

''' 
    Memoizing code, pretty sure I used too many globals
'''
def knapMemo(n, kA, kB):
    global sol
    global s
    global v
    # if the bag over flows, remove item
    if kA < 0 or kB < 0:
        return (-math.inf)

    # if run out of items, end
    if n <= 0:
        return 0

    if (kA, kB) in sol:
        return sol[(kA, kB)]

    # continue recursing
    else:
        ans = max(
            v[n] + knapMemo(n-1, kA-s[n], kB),
            v[n] + knapMemo(n-1, kA, kB-s[n]),
            knapMemo(n-1, kA, kB)
            )
        sol[(kA, kB)] = ans
        return ans

def initKnapMemo():
    # set up sol for the memoizing algorithm
    global sol
    global s
    global v
    sol = {}

def timingTestMemo(n):
    global s
    global v
    initKnapMemo()
    s, v = probGen(n, 3)
    knapMemo(n, 8, 10)

# timing graph for memoizing
# nimTime.showTime(
    # timingTestMemo, 
    # [50, 100, 150, 200], 
    # init = initKnapMemo, 
    # fit = 'polynomial')


