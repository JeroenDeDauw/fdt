#!/usr/bin/python2.6


'''
Created on May 3, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >
'''

from subprocess import Popen
from subprocess import PIPE
import getopt
import sys
import os

class DTFinder(object):
    '''
    Class to find dead translations.
    '''
    
    def __init__(self, directory, langfile):
        '''
        Constructor
        '''
        
        self._directory = directory
        self._langfile = langfile
        
    def find(self):
        langfile = self._findLangFile()
        keys = self._obtainKeysFromLangFile( langfile )
        return self._findMissingKeysInDir( keys, langfile )
        
    def _findLangFile(self):
        return os.path.join(self._directory, self._langfile)
        
    def _obtainKeysFromLangFile(self, langfile):
        subProcess = Popen( ["php", "getKeys.php", langfile], stdout=PIPE, stderr=PIPE )
        crOut,crErr = subProcess.communicate()
        return crOut.split("\n")
        
    def _findMissingKeysInDir(self, keys, langfile):
        for subdir, dirs, files in os.walk(self._directory):
            for file in files:
                filePath = os.path.join(subdir, file)

                if filePath != langfile and filePath.endswith('.php') and not filePath.startswith('.') and not os.path.islink(filePath):
                    keys = self._findKeysInFile(keys, filePath)
                    
                    if len(keys) == 0:
                        print "found all"
                        return [] # If there are no more keys not accounted for, quite searching.
            
        return keys
    
    def _findKeysInFile(self, keys, file):
        f = open(file, 'r')
        contents = f.read()
        remainingKeys=[]
        
        for key in keys:
            if not (key in contents):
                remainingKeys.append(key)
                
        return remainingKeys
            

def show_help():
    print """
fdt.py -d directory [-l langfile] [-? help]

Finds Dead Translations in a MediaWiki extension.

  -s, --directory directory
                The directory in which to work.
  -t --langfile langfile
                The name of the language (i18n) file.
  -?, --help
                Shows this help.
    """

def main():
    try:
        opts, a = getopt.getopt(sys.argv[1:], "d:l:?", ["directory=", "langfile=", "help"])
    except getopt.GetoptError, err:
        print str(err) 
        show_help()
        sys.exit(2)
    
    directory=None
    langfile=None
    
    for opt, arg in opts:
        if opt in ("-d", "--directory"):
            directory = arg        
        elif opt in ("-l", "--langfile"):
            langfile = arg
        elif opt in ("-?", "--help"):
            show_help()
            sys.exit()
        else:
            assert False, "unhandled option" 
    
    if not directory:
        directory = "/var/www/extensions/Maps"
#        print "Missing directory option"
#        show_help()
#        sys.exit(1)

    if not langfile:
        langfile = "Maps.i18n.php"
    
    finder = DTFinder( directory, langfile )
    fdts = finder.find()
    print "Found Dead Translation keys (" + str( len( fdts ) ) + "):\n\n" + "\n".join( fdts )

if __name__ == '__main__':
    main()