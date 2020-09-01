import numpy as np

def calculateGroupScore(scores):
    index = 0
    summation = 0.0
    for x in scores:
        term = (1 / 5) * x * (np.power(4 / 5, index))
        summation += term
        index += 1
    return summation

numInputs = int(input())
index = 0
summation = 0.0
plainValues = []

for r in range(numInputs):
    x = input()
    x = float(x)
    term = (1 / 5) * x * (np.power(4 / 5, index))
    summation += term
    index += 1

    plainValues.append(x)
print(summation)

averageList = []
for i in range(len(plainValues)):
    averageList.append(calculateGroupScore(plainValues[:i]+plainValues[i+1:]))

sum = 0.0
for j in averageList:
    sum+=j
print(sum/len(averageList))


