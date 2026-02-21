# AO-Gem-Set-Calculator
A modular python script to calculate the best gems affixes combinations in the roblox game [Arcane Odyssey](https://www.roblox.com/games/3272915504/Arcane-Odyssey).  
Created by @github/Refract271

## How to use?  

### Calling the function :

You will need to edit the line that calls the function and give it the arguments you want then run the code:

```python
print(bestSet(diveGems, 15, "airCap", 0, "swimSpeed"))
```

> [!NOTE]
> You will obviously need python to run it, any modern version should work

  
### The arguments :

All the arguments are explained in the code but here is a run-through:

- **gems** : *dict* : the gems you want to use, it has to be implemented manually as of now and it follows the same structure as the example.
  
- **gemSlots** : *int* : how many gem slots you want to use, self explanatory
  
- **minimumStat** : *string* : the stat you want a minimum of (*in the case of dive set it was air capacity*). If you don't need that just set **minimumPercentage** to 0 and **minimumStat** to whatever *string* you want.
  
- **minimumPercentage** : *int* : the minimum percentage you want for the **minimumStat**, ex: 99% air cap. Set to 0 to not use it.
  
- **rankingStat** : *string* : the stat used to decide which is the best set, ex: swim speed for dive sets. I might make it a list later on so that it can rank multiple stats.

> [!CAUTION]
> Respect the *types* of the **arguments** or it will just error and not work.

### Gems dict structure :
here is also the structure of the dictionary used to input gems and their stats :  

```python
gems = {
    "name" : {
        "affix1" : int,
        "affix2" : int,
        "amount" : 0
    },

    "name2" : {
        "affix1" : int,
        "affix2" : int,
        "amount" : 0
    },
```

> [!NOTE]
> You can add as many gems and affixes as you want, it's technically infinitely scaleable

## Future Updates + Contact 
This was made for fun as my first published git-hub code. I might update it to work with stats too and let you simulate jewel crafting. This would probably help clear the confusion regarding jewels in the game.
If you have questions DM Refract271 in the Official AO discord server.
