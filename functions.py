import random

def randomSum(value):
    sumOrMinus = [-1,1]
    toAdd = (random.randint(0,10) * random.random()) * random.choice(sumOrMinus)
    return max(0, round(value + toAdd, 2))