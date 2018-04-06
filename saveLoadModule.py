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
'''


import main # we need the blocktypes from the main program
import json
import os
from time import gmtime, strftime

class saveModule(object):
    def __init__(self):
        # "tarnslate" the block texture tuples into readable words for saving
        self.coordDictSave = { str(main.DIRT):'DIRT', str(main.GRASS):'GRASS', str(main.SNOW):'SNOW',
        str(main.SAND):'SAND', str(main.BRICK):'BRICK', str(main.TREE):'TREE', str(main.LEAVES):'LEAVES',
        str(main.WOODEN_PLANKS):'WOODEN_PLANKS', str(main.BADSTONE):'BADSTONE'}
        # "tarnslate" the words back into tuples for loading
        self.coordDictLoad = { 'DIRT':main.DIRT, 'GRASS':main.GRASS, 'SNOW':main.SNOW, 'SAND':main.SAND,
        'BRICK':main.BRICK, 'TREE':main.TREE, 'LEAVES':main.LEAVES, 'WOODEN_PLANKS':main.WOODEN_PLANKS,
        'BADSTONE': main.BADSTONE}
        
        self.saveGameFile = 'saveworld.sav'
        
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
