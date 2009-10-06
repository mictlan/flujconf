#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (C) 2009  Kevin Brown

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, os
from time import sleep
import string

version = '0.4'


def main():
 
    if len(sys.argv) < 2:
        print "no arguments given on the command line"
        #pconf = homedir+ "/.darkice.cfg"
        #music_lib = homedir+ "/Musica"
    for arg in sys.argv[1:]:
        if arg.startswith('-'):
            # fetch sys.argv[1] but without the first character
            option = arg[1:]
            if option == 'v':
                print 'version: ', version 
            elif option == 'help' or option == 'ayuda':
                print '''\
Esta Programa Incuye los siguintes opciones:
  -v:       Imprime el numero de version
  -help:    Ver esta ayuda
  -ayuda:   Ver esta ayuda
  -c:       Especificar la ruta a un configuracion de darkice'''
#  -d:       Specify (mpd) musica library path
            elif option == 'c':
                pconf = string.strip(sys.argv[2])
                from lib.shout import shout
                shout = shout(pconf)
                shout.start()
#            elif option == 'd':
#                music_dir = string.strip(arg[2:])    
            else:
                print 'Unknown option.'
            sys.exit()
    from lib.shout import shout
    shout = shout()
    shout.start()
        
if __name__ == '__main__':
            main()

