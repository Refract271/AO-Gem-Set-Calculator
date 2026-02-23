# AO-Gem-Set-Calculator
A modular python script to calculate the best gems affixes combinations in the roblox game [Arcane Odyssey](https://www.roblox.com/games/3272915504/Arcane-Odyssey).  
Created by Refract271

## How to use?  

Simply download or copy-paste the [diveSets.py](https://github.com/Refract271/AO-Gem-Set-Calculator/blob/main/diveSets.py) file.  
Running the program will create a .txt file with the output, the file should be located in the same folder as the script.  
If you are already familiar with python it's all explained in it but down below is a *slightly* more in-depth explanation.

### Calling the function :

You will need to edit the line that calls the function and give it the arguments you want to then run the code:

```python
bestSet(diveGems, 15, "airCap", 0, "swimSpeed")
```

> [!NOTE]
> You will obviously need python to run it, any modern version should work

  
### The arguments :

All the arguments are explained in the code but here is a run-through:

- **gems** : *dict* : the gems you want to use, it has to be implemented manually as of now and it follows the same structure as the example.
  
- **gemSlots** : *int* : how many gem slots you want to use, self explanatory
  
- **minimumStat** : *string* : the stat you want a minimum of (*in the case of a dive set it was air capacity*). If you don't need that just set **minimumPercentage** to 0 and **minimumStat** to any *string* you want.
  
- **minimumPercentage** : *int* : the minimum percentage you want for the **minimumStat**, ex: 99% air cap. Set to 0 to not use it.
  
- **rankingStat** : *string* : the stat used to decide which is the best set, ex: swim speed for dive sets. I might make it a list later on so that it can rank multiple stats.

> [!CAUTION]
> Respect the *types* of the **arguments** or it will just error and not work.

### Gems dict structure :
here is the structure of the dictionary used to input gems and their stats :  

```python
gems = {
    "name" : {
        "affix1" : int,
        "affix2" : int,
    },

    "name2" : {
        "affix1" : int,
        "affix2" : int,
    },
```

> [!NOTE]
> You can add as many gems and affixes as you want, however it currently only outputs the affixes used to filter 

## Future Updates + Contact 
This was made for fun as my first published git-hub code. I might update it to work with main stats too and let you simulate jewel crafting. This would probably help clear the confusion regarding jewels in the game.  
  
- Probably going to clean up the output at least. **[Done]**
- It bugs me that it's not fully scaleable so might be the next update

If you have questions DM **Refract271** in the Official AO discord server.
