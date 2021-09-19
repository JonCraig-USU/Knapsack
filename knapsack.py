from random import random, randint

s = [None, 7, 5, 8, 8, 3, 4]
v = [None, 2.5, 6.3, 1.3, 8.5, 5.0, 3]

def knapsack(n, kA, kB):
    if kA < 0 or kB < 0:
        return (0 - v[n+1])

    elif n <= 0:
        return 0

    else:
        return max(
            v[n] + knapsack(n-1, kA-s[n], kB),
            v[n] + knapsack(n-1, kA, kB-s[n]),
            knapsack(n-1, kA, kB)
            )

print("knap(6, 10, 12) = " + str(knapsack(6, 10, 12)))
print("knap(6, 15, 15) = " + str(knapsack(6, 15, 15)))
print("(knap(6, 8, 8) = " + str(knapsack(6, 8, 8)))
print("(knap(2, 8, 8) = " + str(knapsack(2, 8, 8)))