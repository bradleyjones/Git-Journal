Git-Journal
===========

Get Git commits from today and put them into a markdown format for day one journal

**Requirements**
***
GitPython library - `easy_install gitpython`


**Syntax**
***
`Git-Journal.py -m -f <gitFolder> -e <gitEmail> -d <date DD/MM/YYYY e.g. 01/01/2012>`

`-m` : Sets whether markdown should be used to format the result 

`-f <gitFolder>` : The location of the git repository on your local machine

`-e <gitEmail>` : The email address of the account you want to get commit messages from

`-d <date>` : The date you want the commit messages from
