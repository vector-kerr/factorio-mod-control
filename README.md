# factorio-mod-control
Enable and disable sets of modules for Factorio.

## Why?
When you install mods on otherwise vanilla Factorio, the mods that you have enabled must exactly match the mods that have been configured for use in the game you want to play. This wouldn't be so much of a pain in the ass if you didn't have to toggle the enabled/disabled status of mods **one at a time** from within the game.

This script allows you to mass enable/disable entire sets of mods in one hit. Once you've got it set up, all you need to do is enable the desired mod set before you start the game. Given that Factorio has to restart every time you change your selected mods, it's no more work for you, and much less mucking about in the long run.

# Requirements
* [Python](https://www.python.org/downloads/) (Works with 3.x, may work with 2.x)
* Very basic JSON knowledge

# Assumptions
* You have installed Python
* You already have Factorio
* You have already installed mods
* By proxy, you already have a `mod-list.json` file available

# Usage
* Place `control.py` into your Factorio mods folder (on Windows, `%AppData%\Factorio\mods`)
* Create a "mod set" JSON file for each combination of mods that you would like to enable
  * The mod set file contains a single array of strings
  * Each string corresponds to the `name` of a mod, as given in the `mod-list.json` file.
    e.g., `[ "base", "boblogistics", "deathstar" ]`
  * Remember to include the base mod!
* Run the program to enable your mod set in the way that you would like
  * Option 1: drag-and-drop your modset JSON file onto `control.py`
  * Option 2: Run it from the command line like this: `python control.py <modset.json>`
  * Option 3: Create a shortcut for a modset (Windows)
    * Make a shortcut to control.py
    * Right-click on the shortcut and select Properties
    * Add the path to the mod set JSON file to load to the end of the `Target` field
      e.g., `C:\Users\vector\AppData\Roaming\Factorio\mods\control.py base.modset.json`
      Note: Depending on where you place your mod set file, you may need to include the
      full path to the mod set file, and it may need to be wrapped in double quotes
    * Click `Apply` followed by `OK`
    * Rename your shortcut to something meaningful, like `Activate Base Factorio Mods`
  * Option 4: Create a shortcut for a modset (Linux and OSX)
    * Create a new file
      `touch ./shortcut-name`
    * Open the file in your favourite editor (`vi`, `nano`, ...)
    * Add the following content, replacing appropriate file paths as required
      ```
      #!/bin/bash
      (
        # The path here is for OSX; Linux will be different...
        cd "/Users/vector/Library/Application Support/factorio/mods"
        python3 control.py bob.modset.json
      )
      ```
    * Save and quit
    * Add the execute bit to the permissions vector
      `chmod u+x ./shortcut-name`
* Play!
