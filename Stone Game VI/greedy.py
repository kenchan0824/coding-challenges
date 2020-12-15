def greedy(aliceValues, bobValues):

    total = [sum(x) for x in zip(aliceValues, bobValues)]
    table = sorted(zip(total, aliceValues, bobValues), reverse=True)
    
    alice, bob = 0, 0
    for i, row in enumerate(table):
    
        if i % 2 == 0:
            alice += row[1]
        else:
            bob += row[2]
    
    if alice == bob: return 0
    return 1 if alice > bob else -1
    
if __name__ == "__main__":
    
    aliceValues = [2,4,3]
    bobValues = [1,6,7]
    greedy(aliceValues, bobValues)
