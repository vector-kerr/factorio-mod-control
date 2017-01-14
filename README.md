# factorio-mod-control
Enable and disable sets of modules for Factorio.

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
    * Click `Apply` followed by `OK`
    * Rename your shortcut to something meaningful, like `Activate Base Factorio Mods`
  * Option 4: Create a shortcut for a modset (Linux)
    * Create a new file
      `touch ./shortcut-name`
    * Open the file in your favourite editor (`vi`, `nano`, ...)
    * Add the following content, replacing appropriate file paths as required
      ```
      #!/bin/bash
      python3 /path/to/control.py /path/to/modset.json
      ```
    * Save and quit
    * Add the execute bit to the permissions vector
      `chmod u+x ./shortcut-name`
      
