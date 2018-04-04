<p align="center"><img src="/PyCraft.png" width="450" >

## Goals and Vision

I would like to see this project turn into an educational tool. Kids love Minecraft and Python is a great first language.
This is a good opportunity to get children excited about programming.

The code should become well commented and more easily configurable. It should be easy to make some simple changes
and see the results quickly.

I think it would be great to turn the project into more of a library / API... a Python package that you import and then
use / configure to setup a world and run it. Something along these lines...


```python
import pycraft

world = pycraft.World(...)
world.set_block(x, y, z, pycraft.DIRT)
pycraft.run(world)
```

The API could contain functionality for the following:

- Easily configurable parameters like gravity, jump velocity, walking speed, etc.
- Hooks for terrain generation.
<br/>

## How to Run

```bash
sudo pip3 install pyglet
git clone https://github.com/XenonCoder/PyCraft.git
cd PyCraft
python3 main.py
```
<br/>

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

See the [wiki](https://github.com/XenonCoder/PyCraft/wiki) for this project to install Python, and other tips.
<br/>

## How to Play
<br/>

### Moving

- W: forward
- S: back
- A: strafe left
- D: strafe right
- Mouse: look around
- Space: jump + vertical flying
- Left Shift: run
- Tab: toggle flying mode

### Building

- Selecting type of block to create:
    - 1: Dirt_with_Grass
    - 2: Sand
    - 3: Brick
    - 4: Oak trunk
    - 5: Leaves
    - Mouse left-click: remove block
    - Mouse right-click: create block
    
### Functions

- F1: toggles reticle, block highlight, and fps counter.
- F2: toggles just the fps counter.
- F12: Save the screenshot in the main folder.

**Warning! By pressing F12, the previous screenshot is automatically overwritten.**

### Quitting

- ESC: release mouse, then close window

## License

Copyright (C) 2013 Michael Fogleman<br>
Copyright (C) 2018 Stefano Peris<br>

eMail: <xenon77.dev@gmail.com><br>

Github repository: <https://github.com/XenonCoder/PyCraft><br>

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

<p align="center"><img src="/gpl3_logo.png" width="300" >

<p align="center"><i>Find a copy of the full license within this project (LICENSE).</i>
