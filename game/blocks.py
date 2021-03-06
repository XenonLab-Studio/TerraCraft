#!/bin/python3

"""
 ________                                        ______                       ______     __
|        \                                      /      \                     /      \   |  \ 
 \$$$$$$$$______    ______    ______   ______  |  $$$$$$\  ______   ______  |  $$$$$$\ _| $$_
   | $$  /      \  /      \  /      \ |      \ | $$   \$$ /      \ |      \ | $$_  \$$|   $$ \ 
   | $$ |  $$$$$$\|  $$$$$$\|  $$$$$$\ \$$$$$$\| $$      |  $$$$$$\ \$$$$$$\| $$ \     \$$$$$$
   | $$ | $$    $$| $$   \$$| $$   \$$/      $$| $$   __ | $$   \$$/      $$| $$$$      | $$ __
   | $$ | $$$$$$$$| $$      | $$     |  $$$$$$$| $$__/  \| $$     |  $$$$$$$| $$        | $$|  \ 
   | $$  \$$     \| $$      | $$      \$$    $$ \$$    $$| $$      \$$    $$| $$         \$$  $$
    \$$   \$$$$$$$ \$$       \$$       \$$$$$$$  \$$$$$$  \$$       \$$$$$$$ \$$          \$$$$


Copyright (C) 2013 Michael Fogleman
Copyright (C) 2018/2019 Stefano Peris <xenonlab.develop@gmail.com>

Github repository: <https://github.com/XenonLab-Studio/TerraCraft>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


def _tex_coord(x, y, n=8):
    """ Return the bounding vertices of the texture square.

    """
    m = 1.0 / n
    dx = x * m
    dy = 1 - (y + 1) * m
    return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m


def _tex_coords(top, bottom, side):
    """ Return a list of the texture squares for the top, bottom and side.

    """
    top = _tex_coord(*top)
    bottom = _tex_coord(*bottom)
    side = _tex_coord(*side)
    result = []
    result.extend(top)
    result.extend(bottom)
    result.extend(side * 4)
    return result


class Block:
    __slots__ = ('name', 'tex_coords')

    def __init__(self, name, tex_coords):
        """A class for Blocks

        :param name: The name of the Block material.
        :param tex_coords: The texture coordinates for this material.
        """
        self.name = name
        self.tex_coords = tex_coords


DIRT = Block('dirt', _tex_coords((0, 2), (0, 2), (0, 2)))
DIRT_WITH_GRASS = Block('dirt_with_grass', _tex_coords((1, 3), (0, 2), (0, 3)))
SAND = Block('sand', _tex_coords((1, 2), (1, 2), (1, 2)))
COBBLESTONE = Block('cobblestone', _tex_coords((2, 3), (2, 3), (2, 3)))
BRICK_COBBLESTONE = Block('brick_cobblestone', _tex_coords((3, 3), (3, 3), (3, 3)))
BRICK = Block('brick', _tex_coords((3, 2), (3, 2), (3, 2)))
BEDSTONE = Block('bedstone', _tex_coords((2, 2), (2, 2), (2, 2)))
TREE = Block('tree', _tex_coords((1, 1), (1, 1), (0, 1)))
LEAVES = Block('leaves', _tex_coords((2, 1), (2, 1), (2, 1)))
SNOW = Block('snow', _tex_coords((1, 0), (1, 0), (1, 0)))
WOODEN_PLANKS = Block('wooden_planks', _tex_coords((2, 0), (2, 0), (2, 0)))
CLOUD = Block('cloud', _tex_coords((1, 0), (1, 0), (1, 0)))
DIRT_WITH_SNOW = Block('dirt_with_snow', _tex_coords((1, 0), (0, 2), (0, 0)))
WATER = Block('water', _tex_coords((3, 1), (3, 1), (3, 1)))
STONE = Block('stone', _tex_coords((0, 4), (0, 4), (0, 4)))
STONE_WITH_SNOW = Block('stone_with_snow', _tex_coords((1, 0), (0, 4), (0, 5)))
COAL_ORE = Block('coal_ore', _tex_coords((1, 4), (1, 4), (1, 4)))
IRON_ORE = Block('iron_ore', _tex_coords((2, 4), (2, 4), (2, 4)))
GOLD_ORE = Block('gold_ore', _tex_coords((3, 4), (3, 4), (3, 4)))

# A reference to the 6 faces (sides) of the blocks:
FACES = [(0, 1, 0), (0, -1, 0), (-1, 0, 0), (1, 0, 0), (0, 0, 1), (0, 0, -1)]
