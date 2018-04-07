<p align="center"><img src="img/Terracraft.png" width="600" >
<br>
<br>

### Goals and Vision

TerraCraft is a small SandBox game engine written in Python 3 + Pyglet.

The objectives of this project are as follows:

- The intention is to create a small complete game focused exclusively on creative mode.

- The project must remain simple, well documented (code and wiki) and easy to modify / improve for students and hobbyists. Keeping the code ordered is very important.

- I would like to see this project turn into an educational tool. Kids love Minecraft and Python is a great first language.

- This is a good opportunity to entertain children on programming.

- We are writing a new wiki to help users collaborate on the project in an easy and productive way. If you have questions, suggestions or want to help us, please write to xenon77.dev@gmail.com or open a discussion here on Github in the "Issues" section.

The code should be well commented and more easily configurable. It should be easy to make some simple changes and see the results quickly.

Thank you all.

<br>

### How to Run

```shell
sudo pip3 install pyglet
git clone https://github.com/XenonCoder/TerraCraft.git
cd TerraCraft
python3 main.py
```

### Mac

On Mac OS X, you may have an issue with running Pyglet in 64-bit mode. Try running Python in 32-bit mode first:

```shell
arch -i386 python3 main.py
```

If that doesn't work, set Python to run in 32-bit mode by default:

```shell
defaults write com.apple.versioner.python Prefer-32-Bit -bool yes 
```

This assumes you are using the OS X default Python.  Works on Lion 10.7 with the default Python 3.5+, and may work on other versions too.  Please raise an issue if not.

See the [wiki](https://github.com/XenonCoder/terracraft/wiki) for this project to install Python, and other tips.
<br/>

## Controls:

### Moving

- W: forward
- S: back
- A: strafe left
- D: strafe right
- Mouse: look around
- Space: jump + vertical flying up
- Tab: toggle flying mode
- Left-Shift: vertical flying down
- Left-Ctrl: run

### Building

- Selecting type of block to create:
    - 1: Dirt
    - 2: Dirt_with_Grass
    - 3: Snow
    - 4: Sand
    - 5: Brick
    - 6: Tree
    - 7: Leaves
    - 8: Wooden_Planks
    - Mouse left-click: remove block
    - Mouse right-click: create block
    
### Functions

- F1: toggles reticle, block highlight, and fps counter.
- F2: toggles just the fps counter.
- F5: Saving progress (the game will hang for a few seconds when writing the savegame.sav file, then it will resume normal operation). The       map is automatically loaded if the file savegame.sav is present in the main project folder.
- F12: Save the screenshot in the main folder.

**Warning! By pressing F12, the previous screenshot is automatically overwritten.**

### Quitting

- ESC: release mouse, then close window

### Screenshots

<p align="center"><img src="https://s9.postimg.org/cmjhqtlof/Schermata_del_2018-04-05_15-35-54.png" >


## License

Copyright (C) 2013 Michael Fogleman<br>
Copyright (C) 2018 Stefano Peris<br>

eMail: <xenon77.dev@gmail.com><br>

Github repository: <https://github.com/XenonCoder/terracraft><br>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.

<br>
<br>

<p align="center"><b>This software is licensed under the GPL3 license.</b>

<p align="center"><img src="img/gpl3_logo.png" width="300" >

<p align="center"><i>Find a copy of the full license within this project (LICENSE).</i>
