#!/usr/bin/python2.6


'''
Created on May 3, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >
'''

import os
import sys
import getopt

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
        keys = self.obtainLangKeysFromFile(self.findLangFile())
        
    def findLangFile(self):
        return self._langfile
        
    def obtainKeysFromLangFile(self, langfile):
        print os.system( "php getKeys.php" )
        
    def findKeysInDir(self, keys):    
        self.findKeysinFile( keys )
    
    def findKeysinFile(self, keys):
        pass # f = open('demo.ics', 'r')
            


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
        print "Missing directory option"
        show_help()
        sys.exit(1)
    
    finder = DTFinder( directory, langfile )
    print finder.find().__repr__()

if __name__ == '__main__':
    main()