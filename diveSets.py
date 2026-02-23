import itertools

diveGems = {
    "fusedSwimPrimary" : {
        "swimSpeed" : 11,
        "airCap" : 5.5,
    },

    "fusedAirPrimary" : {
        "airCap" : 22,
        "swimSpeed" : 2.76,
    },

    "mirror" : {
        "airCap" : 13.75,
        "swimSpeed" : 6.88,
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

    # returns type : set of tuple of string    -> ex: 
    # {("mirror", "mirror", "mirror", "mirror"), ("mirror", "mirror", "mirror", "pureSwim"), ..., ("pureSwim", "pureAir", "pureAir", "pureAir"), ("pureAir", "pureAir", "pureAir", "pureAir")}

    return set(itertools.combinations_with_replacement(dictToSet(diveGems), gemSlots))

def statSum(gems, stat, combination):
    
    # sums all values of the chosen stat

    # gems : dict       -> the gems you want to use, same format as the diveGems dict
    # stat : string     -> the stat summed 
    # allCombinations : list of tuples of string    -> refer to possibleCombinations function

    # returns statTot : int -> sum of the desired stat for one specific combination

    statTot = 0

    for num, i in enumerate(combination):

        check = gems[(combination)[num]]

        if stat not in check:
            pass
        
        else:
            statTot += check[stat]

    return statTot

def writeGems(gems, i):

    # avoids nesting loops mainly

    # gems : dict       -> the gems you want to use, same format as the diveGems dict
    # i : tuple of strings -> an element of bestSets in bestSet function

    # returns : niceText : string -> it's a nice text ;D

    niceText = ""

    for j in gems.keys():
        amount = i.count(j)
        niceText += j + ": " + str(amount) + "\n"

    return niceText

def bestSet(gems, gemSlots, minimumStat, minimumPercentage, rankingStat) : 

    # creates all possible sets and choses the best depending on:

    # gems : dict               -> the gems you want to use, same format as the diveGems dict
    # gemSlots : int            -> how many gem slots you are using
    # minimumStat : string      -> the key in the gems sub-dictionary related to the stat you want to filter
    # minimumPercentage : int   -> the minimum percentage you want for the stat, ex: 99% air cap
    # rankingStat : string      -> the stat used to decide which is the best set, ex: swim speed for dive sets

    # returns nothing since the output is in the file it creates

    allCombinations = possibleCombinations(dictToSet(gems), gemSlots)
    bestRanking = 0
    bestMinimum = 0
    bestSets = set()

    for i in allCombinations:

        rankStatTot = statSum(gems, rankingStat, i)
        minimumStatTot = statSum(gems, minimumStat, i)

        if minimumStatTot >= minimumPercentage and rankStatTot > bestRanking:
           bestRanking = rankStatTot
           bestMinimum = minimumStatTot
           bestSets.clear()
           bestSets.add(i)

        elif minimumStatTot >= minimumPercentage and rankStatTot == bestRanking:
            bestSets.add(i)

    with open( "bestSets.txt", "w") as f:
        for num, i in enumerate(bestSets, start=1):
            f.write(
            "Option " + str(num) + 
            "\n\n" + 
            writeGems(gems, i) + 
            "\n" + 
            minimumStat + ": " + str(bestMinimum) +
            "\n" +
            rankingStat + ": " + str(bestRanking) +
            "\n\n"
            )

    return 

bestSet(diveGems, 15, "airCap", 99, "swimSpeed")
