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

from .savemanager import SaveManager
from .scenes import *


class SceneManager:
    """A class to handle switching between Scenes instances."""
    def __init__(self, window):
        self.window = window

        # Save data is accessible from all Scenes
        self.save = SaveManager()

        # A dictionary of available Scenes
        self.scenes = {}
        self.current_scene = None

        # All Scenes will have a reference to the manager
        Scene.scene_manager = self

        # Add the defaults Scenes to the manager
        self.add_scene(MenuScene(self.window))
        self.add_scene(HelpScene(self.window))
        self.add_scene(GameScene(self.window))
        # Activate the Menu Scene
        self.change_scene("MenuScene")

    def add_scene(self, scene_instance):
        """Add a Scene instance to the manager.

        :param scene_instance: An instace of a `Scene`.
        """
        self.scenes[scene_instance.__class__.__name__] = scene_instance

    def change_scene(self, scene_name):
        """Change to a specific Scene, by it's class name.

        When changing to a new Scene, any Window event handlers that
        are defined on the new Scene will be added. Any handlers on
        the previously active Scene will be removed.

        :param scene_name: A `str` of the desired Scene class name.
        """
        assert scene_name in self.scenes, "Requested scene not found: {}".format(scene_name)
        if self.current_scene:
            self.window.remove_handlers(self.current_scene)
        self.current_scene = self.scenes[scene_name]
        self.window.push_handlers(self.current_scene)

    def update(self, dt):
        """Update the currently set Scene.

        This method should be scheduled to be called repeatedly by
        the pyglet clock.

        :param dt: float: The change in time since the last call.
        """
        self.current_scene.update(dt)
