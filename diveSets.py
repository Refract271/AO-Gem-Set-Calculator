import itertools

diveGems = {
    "pureSwim" : {
        "swimSpeed" : 11,
        "airCap" : 5.5,
        "amount" : 0
    },

    "pureAir" : {
        "airCap" : 22,
        "swimSpeed" : 2.76,
        "amount" : 0
    },

    "mirror" : {
        "airCap" : 13.75,
        "swimSpeed" : 6.88,
        "amount" : 0
    }
}

def dictToSet(gems):

    # creates a set with all the gems in the gems dictionary

    # gems : dict   -> the gems you want to use, same format as the diveGems dict

    # returns gemsSet : set of string   -> ex: {"mirror", "pureSwim", "pureAir"}

    gemsSet = set()

    for i in gems.keys():
        gemsSet.add(i)

    return gemsSet

def possibleCombinations(gemsSet, gemSlots):

    # creates a list of n length tuples of string with n = gemSlots, each tuple represents a possible combination of the gemsSet

    # gemsSet : set of string   -> refer to dictToSet function
    # gemSlots : int            -> how many gem slots you are using

    # returns type : list of tuple of string    -> ex: 
    # [("mirror", "mirror", "mirror", "mirror"), ("mirror", "mirror", "mirror", "pureSwim"), ..., ("pureSwim", "pureAir", "pureAir", "pureAir"), ("pureAir", "pureAir", "pureAir", "pureAir")]

    return list(itertools.combinations_with_replacement(dictToSet(diveGems), gemSlots))

def statSum(gems, gemSlots, stat, allCombinations, i):
    
    # sums all values of the chosen stat

    # gems : dict       -> the gems you want to use, same format as the diveGems dict
    # gemSlots : int    -> how many gem slots you are using
    # stat : string     -> the stat summed 
    # allCombinations : list of tuples of string    -> refer to possibleCombinations function
    # i : int           -> the indice of the tuple in allCombinations

    # returns statTot : int -> sum of the desired stat for one specific combination

    statTot = 0

    for j in range(gemSlots):

        if stat not in gems[(allCombinations[i])[j]]:
            pass
        
        else:
            statTot += gems[(allCombinations[i])[j]][stat]

    return statTot

def editAmount(gems, combination):
    
    for i in combination:
        gems[i]["amount"] += 1

    return gems

def bestSet(gems, gemSlots, minimumStat, minimumPercentage, rankingStat) : 

    # creates all possible sets and choses the best depending on:

    # gems : dict               -> the gems you want to use, same format as the diveGems dict
    # gemSlots : int            -> how many gem slots you are using
    # minimumStat : string      -> the key in the gems sub-dictionary related to the stat you want to filter
    # minimumPercentage : int   -> the minimum percentage you want for the stat, ex: 99% air cap
    # rankingStat : string      -> the stat used to decide which is the best set, ex: swim speed for dive sets

    # returns bestSetDict : dict   -> the same as the gem dictionary used for input but with the amount representing the number of gem used

    bestMinimum = 0
    bestRanking = 0
    bestSet = set()

    allCombinations = possibleCombinations(dictToSet(gems), gemSlots)
    numberCombinations = len(allCombinations)

    for i in range(numberCombinations):
        minimumStatTot = statSum(gems, gemSlots, minimumStat, allCombinations, i)
        rankingStatTot = statSum(gems, gemSlots, rankingStat, allCombinations, i)

        if minimumStatTot >= minimumPercentage and rankingStatTot > bestRanking:
            bestMinimum = minimumStatTot
            bestRanking = rankingStatTot
            bestSet = allCombinations[i]

    bestSetDict = editAmount(gems, bestSet)

    return str(bestSetDict) + "\n" + minimumStat + ": " + str(bestMinimum) + "\n" + rankingStat + ": " + str(bestRanking)

print(bestSet(diveGems, 15, "airCap", 99, "swimSpeed"))