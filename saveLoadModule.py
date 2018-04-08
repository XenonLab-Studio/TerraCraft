#!/bin/python3

'''
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
Copyright (C) 2018 Stefano Peris <xenon77.dev@gmail.com>

Github repository: <https://github.com/XenonCoder/Terracraft>

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
'''


import main # we need the blocktypes from the main program
import json
import os
from time import gmtime, strftime

class saveModule(object):
    def __init__(self):
        # "tarnslate" the block texture tuples into readable words for saving
        self.coordDictSave = { str(main.DIRT):'DIRT', str(main.DIRT_WITH_GRASS):'DIRT_WITH_GRASS', str(main.SNOW):'SNOW',
        str(main.SAND):'SAND', str(main.COBBLESTONE):'COBBLESTONE', str(main.BRICK_COBBLESTONE):'BRICK_COBBLESTONE',
        str(main.BRICK):'BRICK', str(main.TREE):'TREE', str(main.LEAVES):'LEAVES',
        str(main.WOODEN_PLANKS):'WOODEN_PLANKS', str(main.BADSTONE):'BADSTONE'}
        # "tarnslate" the words back into tuples for loading
        self.coordDictLoad = { 'DIRT':main.DIRT, 'DIRT_WITH_GRASS':main.DIRT_WITH_GRASS, 'SNOW':main.SNOW, 'SAND':main.SAND,
        'COBBLESTONE':main.COBBLESTONE, 'BRICK_COBBLESTONE':main.BRICK_COBBLESTONE, 'BRICK':main.BRICK,
        'TREE':main.TREE, 'LEAVES':main.LEAVES, 'WOODEN_PLANKS':main.WOODEN_PLANKS, 'BADSTONE': main.BADSTONE}
        
        self.saveGameFile = 'saveworld.json'
        
    def printStuff(self, txt):
        print((strftime("%d-%m-%Y %H:%M:%S|", gmtime()) + str(txt)))
    
    def hasSaveGame(self):
        if os.path.exists(self.saveGameFile):
            return True
        else:
            return False
    
    def loadWorld(self, model):
        self.printStuff('start loading...') 
        fh = open(self.saveGameFile, 'r')
        world_mod = fh.read()
        fh.close()
        
        world_mod = world_mod.split('\n')
        
        for blockLine in world_mod:
            # remove the last empty line
            if blockLine != '':
                coords, blockType = blockLine.split(' => ')
                # convert the json list into tuple; json ONLY get lists but we need tuples
                # translate the readable word back into the texture coords
                model.add_block(tuple(json.loads(coords)), self.coordDictLoad[blockType], False)
        
        self.printStuff('loading completed')
        
    def saveWorld(self, model):
        self.printStuff('start saving...')
        fh = open(self.saveGameFile, 'w')
        
        # build a string to save it in one action
        worldString = ''
        
        for block in model.world:
            # convert the block coords into json
            # convert with the translation dictionary the block type into a readable word
            worldString += json.dumps(block) + ' => ' + self.coordDictSave[str(model.world[block])] + '\n'

        fh.write(worldString)
        fh.close()
        self.printStuff('saving completed')
