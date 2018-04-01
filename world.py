'''
 _______              ______                       ______    __
/       \            /      \                     /      \  /  |
$$$$$$$  | __    __ /$$$$$$  |  ______   ______  /$$$$$$  |_$$ |
$$ |__$$ |/  |  /  |$$ |  $$/  /      \ /      \ $$ |_ $$// $$   |
$$    $$/ $$ |  $$ |$$ |      /$$$$$$  |$$$$$$  |$$   |   $$$$$$/
$$$$$$$/  $$ |  $$ |$$ |   __ $$ |  $$/ /    $$ |$$$$/      $$ |
$$ |      $$ \__$$ |$$ \__/  |$$ |     /$$$$$$$ |$$ |       $$ |/  |
$$ |      $$    $$ |$$    $$/ $$ |     $$    $$ |$$ |       $$  $$/
$$/        $$$$$$$ | $$$$$$/  $$/       $$$$$$$/ $$/         $$$$/
          /  \__$$ |
          $$    $$/
           $$$$$$/


Copyright (C) 2013 Michael Fogleman
Copyright (C) 2018 Stefano Peris <xenon77.dev@gmail.com>

Github repository: <https://github.com/XenonCoder/PyCraft>

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


import shutil
 
def do_e(startx,starth,starty,texture):
    """ draw the letter E """
    myletter = []
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+1,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+2,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+3,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+4,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+1,starth+2,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+2,starth+2,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+1,starth,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+2,starth,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+1,starth+4,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+2,starth+4,starty,texture))
    return(myletter)
def do_h(startx,starth,starty,texture):
    """ draw the letter H """
    myletter = []
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+1,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+2,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+3,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+4,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+1,starth+2,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+2,starth+2,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+3,starth,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+3,starth+1,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+3,starth+2,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+3,starth+3,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+3,starth+4,starty,texture))
    return(myletter)
def do_l(startx,starth,starty,texture):
    """ draw the letter L """
    myletter = []
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+1,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+2,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+3,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+4,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+1,starth,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+2,starth,starty,texture))
    return(myletter)
def do_o(startx,starth,starty,texture):
    """ draw the letter O """
    myletter = []
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+1,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+2,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+3,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+4,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+1,starth,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+2,starth,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+1,starth+4,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+2,starth+4,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+3,starth,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+3,starth+1,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+3,starth+2,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+3,starth+3,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+3,starth+4,starty,texture))
    return(myletter)
def do_w(startx,starth,starty,texture):
    """ draw the letter W """
    myletter = []
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+1,starth,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+3,starth,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+1,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+2,starth+1,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+4,starth+1,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+2,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+2,starth+2,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+4,starth+2,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+3,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+2,starth+3,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+4,starth+3,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+4,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+4,starth+4,starty,texture))
    return(myletter)
def do_r(startx,starth,starty,texture):
    """ draw the letter R """
    myletter = []
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+1,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+2,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+3,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+4,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+1,starth+4,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+2,starth+4,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+3,starth+3,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+2,starth+2,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+1,starth+2,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+3,starth+1,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+3,starth,starty,texture))
    return(myletter)
def do_d(startx,starth,starty,texture):
    """ draw the letter O """
    myletter = []
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+1,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+2,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+3,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx,starth+4,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+1,starth,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+2,starth,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+1,starth+4,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+2,starth+4,starty,texture))
    #myletter.append("[%d,%d,%d]=>%s\n" % (startx+3,starth,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+3,starth+1,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+3,starth+2,starty,texture))
    myletter.append("[%d,%d,%d]=>%s\n" % (startx+3,starth+3,starty,texture))
    return(myletter)
 
shutil.copyfile('savegame.bak','savegame.sav')
world=open('savegame.sav','a')
 
nextletter = do_h(20,4,-8,'BRICK')
for i in nextletter:
    world.write(i)
nextletter = do_e(25,4,-8,'BRICK')
for i in nextletter:
    world.write(i)
nextletter = do_l(29,4,-8,'BRICK')
for i in nextletter:
    world.write(i)
nextletter = do_l(33,4,-8,'BRICK')
for i in nextletter:
    world.write(i)
nextletter = do_o(37,4,-8,'BRICK')
for i in nextletter:
    world.write(i)
nextletter = do_w(43,4,-8,'BRICK')
for i in nextletter:
    world.write(i)
nextletter = do_o(49,4,-8,'BRICK')
for i in nextletter:
    world.write(i)
nextletter = do_r(54,4,-8,'BRICK')
for i in nextletter:
    world.write(i)
nextletter = do_l(59,4,-8,'BRICK')
for i in nextletter:
    world.write(i)
nextletter = do_d(63,4,-8,'BRICK')
for i in nextletter:
    world.write(i)
world.close()
