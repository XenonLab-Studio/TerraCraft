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
Copyright (C) 2018 Stefano Peris <xenonlab.develop@gmail.com>

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

import pyglet
import pickle
import json
import os

from time import gmtime, strftime


class SaveManager(object):
    def __init__(self):
        """SaveManager handles saving/loading of worlds and options.

        An internal dictionary (self._data) holds persistent data
        such as options, inventory, etc. To make accessing this easier,
        the "magic methods" `__getitem__` and `__setitem__` are used to
        add dictionary-like behavior to `SaveManager`.
        """

        # Get the appropriate OS specific save path:
        self.save_path = pyglet.resource.get_settings_path('TerraCraft')
        self.save_file = 'saveworld{}.dat'
        self.config_file = 'config.json'
        self.save_slot = 0

        self._data = {'revision': 0,
                      'options': {},
                      'inventory': {}}

    @staticmethod
    def timestamp_print(txt):
        print((strftime("%d-%m-%Y %H:%M:%S | ", gmtime()) + str(txt)))

    def has_save_game(self):
        """Returns True if the save path and file exist."""
        save_file = self.save_file.format(self.save_slot)
        return os.path.exists(os.path.join(self.save_path, save_file))

    def load_world(self, model):
        save_file = self.save_file.format(self.save_slot)
        save_file_path = os.path.join(self.save_path, save_file)
        self.timestamp_print('start loading...')

        try:
            with open(save_file_path, 'rb') as file:
                loaded_world = pickle.load(file)

            for position, block in loaded_world.items():
                if block.name == "dirt_with_grass":
                    model.add_block(position, block, immediate=True)
                else:
                    model.add_block(position, block, immediate=False)

            self.timestamp_print('Loading completed.')
            return True
        except:     # If loading fails for ANY reason, return False
            self.timestamp_print('Loading failed! Generating a new map.')
            return False

    def save_world(self, model):
        save_file = self.save_file.format(self.save_slot)
        save_file_path = os.path.join(self.save_path, save_file)
        self.timestamp_print('start saving...')

        # If the save directory doesn't exist, create it
        if not os.path.exists(self.save_path):
            self.timestamp_print('creating directory: {}'.format(self.save_path))
            os.mkdir(self.save_path)

        # Efficiently save the world to a binary file
        with open(save_file_path, 'wb') as file:
            pickle.dump(model.world, file)

        self.timestamp_print('saving completed')

    def __getitem__(self, item):
        return self._data.get(item)

    def __setitem__(self, key, item):
        self._data[key] = item

    def get(self, item, default):
        return self._data.get(item, default)

    def keys(self):
        return self._data.keys()
