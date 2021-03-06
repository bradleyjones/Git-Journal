#!/usr/bin/env python

import sys, getopt
from time import localtime, strftime
from git import *

def main(argv):
    gitFolder = ''
    gitEmail = ''
    markdown = False
    numberMessages = 0
    numberSelected = False
    date = strftime("%d/%m/%Y", localtime())
    recentFirst = False

    try:
        opts, args = getopt.getopt(argv,"mrhf:e:d:n:",["gfold=","gemail=","ddate=","msgNum"])
    except getopt.GetoptError:
        print 'Git-Journal.py -f <gitFolder> -e <gitEmail> -d <date DD/MM/YYYY e.g. 01/01/2012>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'Git-Journal.py -f <gitFolder> -e <gitEmail> -d <date DD/MM/YYYY e.g. 01/01/2012>'
        elif opt == '-m':
            markdown = True
        elif opt == '-r':
            recentFirst = True
        elif opt in ("-f", "--gfold"):
            gitFolder = arg
            #print 'Git Folder is "',gitFolder,'"'
        elif opt in ("-e", "--gemail"):
            gitEmail = arg
            #print 'Git Email is "',gitEmail,'"'
        elif opt in ("-d", "--ddate"):
            date = arg
        elif opt in("-n", "--msgNum"):
            numberMessages = int(arg)
            numberSelected = True

    #Set repository
    try:
        repo = Repo(gitFolder)
    except InvalidGitRepositoryError:
        print "The Git folder you entered is not a valid Git repository"
        sys.exit(2)
    
    messages = []

    #Get the commit messages for the selected date looking at the most recent first (more efficient)
    for x in repo.iter_commits('master'):
        commitDate = strftime("%d/%m/%Y", localtime(x.committed_date))
        if commitDate == date:
            if gitEmail == '':
                    messages.append(getMessage(x, markdown, True))
            elif x.author.email == gitEmail:
                    messages.append(getMessage(x, markdown, False))
    
    if len(messages) != 0:
        listFolder = repo.working_dir.split('/')
        if listFolder[len(listFolder) - 1] == '':
            repoName = listFolder[len(listFolder) - 2] 
        else:
            repoName = listFolder[len(listFolder) - 1] 

        if markdown:
            print "\n**Today in " + repoName + "!**\n"
        else:
            print "\nToday in " + repoName + "!\n"

    if recentFirst == False:
        msgs = reversed(messages)
    elif recentFirst == True:
        msgs = messages

    #Print the messages in chronological order
    for x in msgs:
        if numberSelected == False:
            print x
            if markdown:
                print "***"
        elif (numberMessages != 0):
            print x
            if markdown:
                print "***"
            numberMessages -= 1

def getMessage(x, markdown, user):
    commitTime = strftime("%H:%M", localtime(x.committed_date))
    if user:
        commitMsg = commitTime + " - " + x.author.name + "\n"
    else:
        commitMsg = commitTime + "\n"

    for line in x.message.split('\n'):
        if line != "": #Remove lines that are empty
            if markdown:
                commitMsg += "*" + line + "*" + "\n"
            else:
                commitMsg += line + "\n"
    return commitMsg

if __name__ == "__main__":
   main(sys.argv[1:])
