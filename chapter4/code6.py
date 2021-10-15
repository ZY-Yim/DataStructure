# dynamic programming

"""
numCoins = min(1 + numCoins(originalamount - 1), 
 1 + numCoins(originalamount - 5), 
 1 + numCoins(originalamount - 10), 
 1 + numCoins(originalamount - 25))
"""

def recMC(coinValueList, change, knownResults):
    """
    knownResults: save result, avoid repeating searching
    """
    minCoins = change

    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in (c for c in coinValueList if c <= change):
            numCoins = 1 + recMC(coinValueList, change-i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins

    return minCoins

# print(recMC([1, 5, 10, 25], 63, [0]*64))


# dyamic programming solution
def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1 
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin 

    return minCoins, coinsUsed

def printCoins(coinsUsed, change): 
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

res = dpMakeChange([1, 5, 10, 21, 25], 63, [0]*64, [0]*64)
print(res[0])
printCoins(res[1], 63)
