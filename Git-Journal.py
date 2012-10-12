#!/usr/bin/python

import sys, getopt
from time import localtime, strftime
from git import *

def main(argv):
    gitFolder = ''
    gitEmail = ''
    markdown = False
    date = strftime("%d/%m/%Y", localtime())
    try:
        opts, args = getopt.getopt(argv,"mhf:e:d:",["gfold=","gemail=","ddate="])
    except getopt.GetoptError:
        print 'Git-Journal.py -f <gitFolder> -e <gitEmail> -d <date DD/MM/YYYY e.g. 01/01/2012>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'Git-Journal.py -f <gitFolder> -e <gitEmail> -d <date DD/MM/YYYY e.g. 01/01/2012>'
        elif opt == '-m':
            markdown = True
        elif opt in ("-f", "--gfold"):
            gitFolder = arg
            #print 'Git Folder is "',gitFolder,'"'
        elif opt in ("-e", "--gemail"):
            gitEmail = arg
            #print 'Git Email is "',gitEmail,'"'
        elif opt in ("-d", "--ddate"):
            date = arg
    
    #Set repository
    try:
        repo = Repo(gitFolder)
    except InvalidGitRepositoryError:
        print "The Git folder you entered is not a valid Git repository"
        sys.exit(2)

    if markdown:
        print "**Today in Git!** \n"
    
    for x in repo.iter_commits('master'):
        if x.author.email == gitEmail:
            commitDate = strftime("%d/%m/%Y", localtime(x.committed_date))
            if commitDate == date:
                commitMsg = ""
                for line in x.message.split('\n'):
                    if line != "": #Remove lines that are empty
                        if markdown:
                            commitMsg += "*" + line + "*" + "\n"
                        else:
                            commitMsg += line + "\n"
                print commitMsg
                if markdown:
                    print "***"

if __name__ == "__main__":
   main(sys.argv[1:])
