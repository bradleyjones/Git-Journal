#!/usr/bin/python

import sys, getopt
from git import *

def main(argv):
    gitFolder = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["gfold="])
    except getopt.GetoptError:
        print 'test.py -l <gitFolder>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -l <gitFolder>'
            sys.exit()
        elif opt in ("-l", "--gfold"):
            gitFolder = arg
            print 'Git Folder is "',gitFolder,'"'
    
    if len(sys.argv) == 1:
        print 'Please pass the folder of the Git repo'
        print 'test.py -l <gitFolder>'
        sys.exit(2)
    
    repo = Repo(gitFolder)
    print repo
    print repo.commits()

if __name__ == "__main__":
   main(sys.argv[1:])
