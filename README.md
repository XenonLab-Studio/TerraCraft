# PyCraft

###### Simple 3D sandbox game inspired by Minecraft/Minetest, written in Python 3 and Pyglet.
<br/>

Youtube: (WIP)
<br/>

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

```shell
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
- Space: jump
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

### Quitting

- ESC: release mouse, then close window
