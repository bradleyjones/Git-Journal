#!/usr/bin/python

import sys, getopt
from time import localtime, strftime
from git import *

def main(argv):
    gitFolder = ''
    gitEmail = ''
    try:
        opts, args = getopt.getopt(argv,"hf:e:",["gfold=","gemail"])
    except getopt.GetoptError:
        print 'Git-Journal.py -f <gitFolder> -e <gitEmail>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'Git-Journal.py -f <gitFolder> -e <gitEmail>'
            sys.exit()
        elif opt in ("-f", "--gfold"):
            gitFolder = arg
            #print 'Git Folder is "',gitFolder,'"'
        elif opt in ("-e", "--gemail"):
            gitEmail = arg
            #print 'Git Email is "',gitEmail,'"'
    
    #Set repository
    repo = Repo(gitFolder)

    for x in repo.iter_commits('master'):
        if x.author.email == gitEmail:
            commitDate = strftime("%d %b %Y", localtime(x.committed_date)) 
            today = strftime("%d %b %Y", localtime()) 
            if commitDate != today:
                break
            commitMsg = x.message
            if commitMsg.endswith("\n"):
                print commitMsg
            else:
                print commitMsg + "\n"

if __name__ == "__main__":
   main(sys.argv[1:])
