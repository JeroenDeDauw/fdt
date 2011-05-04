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
import fileinput

class DTFinder(object):
    """
    Class to find dead translation keys.
    """
    
    def __init__(self, directory, langfile):
        """
        Creates a new instance of DTFinder.
        
        Arguments:
        directory -- The directory in which to look for translation keys.
        langfile -- The file in which the translation key definitions can be found, relative to the directory argument.
        """
        
        self._directory = directory
        self._langfile = self._findLangFile( langfile )
        self._dts = []
        self._originalKeyCount = -1
        
    def find(self):
        """Find, store and return the Dead Translation keys."""
        keys = self._obtainKeysFromLangFile()
        self._originalKeyCount = len( keys )
        self._dts = self._findMissingKeysInDir( keys )
        return self._dts
    
    def fix(self):
        """Remove the Found Dead Translation keys from the i18n file."""
        isMessageContinuation = False

        for line in fileinput.input(self._langfile, inplace=1):
            hasKey = False

            if not isMessageContinuation:
                for key in self._dts:
                    if "'" + key + "' => " in line:
                        hasKey = True
                        break
            
            killLine = hasKey or isMessageContinuation
            isMessageContinuation = killLine and not line.endswith( ',\n' )
            
            sys.stdout.write( "" if killLine else line )
        
    def getOriginalKeyCount(self):
        """Returns the total amount of translation keys in the language file before any modifications where made to it."""
        if self._originalKeyCount == -1:
            self.find()
            
        return self._originalKeyCount
    
    def _findLangFile(self, langfile):
        return os.path.join(self._directory, langfile)
        
    def _obtainKeysFromLangFile(self):
        subProcess = Popen( ["php", "getKeys.php", self._langfile], stdout=PIPE, stderr=PIPE )
        crOut,crErr = subProcess.communicate()
        return crOut.split("\n")
        
    def _findMissingKeysInDir(self, keys):
        for subdir, dirs, files in os.walk(self._directory):
            for file in files:
                filePath = os.path.join(subdir, file)

                if filePath != self._langfile and filePath.endswith('.php') and not filePath.startswith('.') and not os.path.islink(filePath):
                    keys = self._findKeysInFile(keys, filePath)
                    
                    if len(keys) == 0:
                        return [] # If there are no more keys not accounted for, quite searching.
            
        return self._filterCommonConcats( keys )
    
    def _filterCommonConcats(self, keys):
        filtered = []
        
        for key in keys:
            if not key.startswith( 'right-' ):
                filtered.append( key )
            
        return filtered
    
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
fdt.py -d directory -l langfile [-? help]

Finds Dead Translations in a MediaWiki extension.

  -s, --directory directory
                The directory in which to work.
  -t --langfile langfile
                The name of the language (i18n) file.
  -?, --help
                Shows this help.
                
Example: python fdt.py -d ~/root/extensions/Maps -l Maps.i18n.php
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
        print "Missing directory option"
        show_help()
        sys.exit(1)

    if not langfile:
        print "Missing langfile option"
        show_help()
        sys.exit(1)
    
    finder = DTFinder( directory, langfile )
    fdts = finder.find()
    if ( len( fdts ) > 0 ):
        print "Found Dead Translation keys (%s of %s):\n\n" % ( len( fdts ), finder.getOriginalKeyCount() ) + "\n".join( fdts )
        
        if raw_input( "Remove the Found Dead Translation keys? (y/n) " ) == "y":
            finder.fix()
    else: 
        print "Did not Find Dead Translation keys! :)"
    
    print "Done."

if __name__ == '__main__':
    main()