###########################
from random import random, randint

N = 7
K = 100

def knapsackBool(i, size):
    # if the bag is exactly full return true
    if size == 0:
        return True
    # if we overfilled the bag return false
    if size < 0:
        return False
    # if we have run out of items to put in the bag return false
    if i == 0:
        return False
    # if there is still space, try the next object
    return knapsackBool(i-1, size) or knapsackBool(i-1, size - S[i])
    
for _ in range(0,100):
    S = [randint(1,K/2) for _ in range(0,N + 1)]
    if knapsackBool(N, K):
        print("Solution exists")
    else:
        print("Solution does not exist")

# S = [None, 1, 4, 7]
# print(knapsackBool(3, 10)) # False
# print(knapsackBool(3, 8))  # True
# print(knapsackBool(3, 12)) # True
# print(knapsackBool(3, 13)) # False
# print(knapsackBool(3, 3))  # False
    
    
N = 5
K = 10
S = [None, 11,12,23,435,44,4,20]
print(knapsackBool(N, K))
        
