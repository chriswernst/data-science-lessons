# Terminal Notes

# Adopted from 0nn0's 'Terminal Cheatsheet for Mac':  https://github.com/0nn0/terminal-mac-cheatsheet
# These commands also work correctly on Linux

### CORE COMMANDS

cd
# Home directory
cd [folder]
# Change directory e.g. cd documents
# Selects a folder in the directory you're currently in
 
cd /
# Root of drive
cd ‐
# Previous directory
ls
# Short listing
ls ‐l
# Long listing
ls ‐a
# Listing incl. hidden files
ls ‐lh
# Long listing with Human readable file sizes
ls ‐R
# Entire content of folder recursively
sudo [command]
# Run command with the security privileges of the superuser (Super User DO)
open [file]
# Opens a file ( as if you double clicked it )
top
# Displays active processes. Press q to quit
nano [file]
# Opens the file using the nano editor
vim [file]
# Opens the file using the vim editor
clear
# Clear screen
reset
# Resets the terminal display


### FILE MANAGEMENT

touch [file]
# Create new file
pwd
# Full path to working directory
.
# Current folder, e.g. ls . 
..
# Parent/enclosing directory, e.g. ls ..
ls ‐l ..
# Long listing of parent directory
cd ../../
# Move 2 levels up
cat
# Concatenate to screen
rm [file]
# Remove a file, e.g. rm data.tmp
rm ‐i [file]
# Remove with confirmation
rm ‐r [dir]
# Remove a directory and contents
rm ‐f [file]
# Force removal without confirmation
cp [file] [newfile]
# Copy file to file
cp [file] [dir]
# Copy file to directory
mv [file] [new filename]
# Move/Rename, e.g. mv file1.ad /tmp
 pbcopy < [file]
# Copies file contents to clipboard
pbpaste
# Paste clipboard contents
pbpaste > [file]
# Paste clipboard contents into file, pbpaste > paste‐test.txt
which bash
#gives the correct bash
echo '#!/bin/bash' >> hello
# Adds a new line to the file 'hello'
chmod u+x hello
# Sets permissions for the file named 'hello'. r=read, w=write, x=execute, u=user, g=group, o=other
sudo crontab -e
# Opens the existing cron file if one exists
minute hour day-of-month month day-of-week command
# The cron time structure
minute (0-59), hour (0-23, 0 = midnight), day (1-31), month (1-12), weekday (0-6, 0 = Sunday)
01 04 * * * /usr/bin/somedirectory/somecommand
# Will run at 4:01 am everyday of every month
*/10 * * * * /usr/bin/somedirectory/somecommand
# Every ten minutes
# More at https://help.ubuntu.com/community/CronHowto
sudo crontab -l
# Lists the crontabs
diskutil list
# Lists the hard drives
sudo dd if=/dev/disk2 of=~/Desktop/raspberrypi.dmg
# Clones the sd card at 'disk2', and saves it as 'raspberrypi.dmg' on the desktop
hostname -I
# Gives the IP address on Linux
ssh pi@192.XXX.X.XX
# From a Mac/Linux machine, to create a secure shell login
scp UserName@192.XXX.X.XX:/User/Name/of/Host/Path/filename.py ~/Path/of/destination/
# To pull files from the host machine to the destination







### BASH PROFILE
echo $PATH
# returns the shell path
# Remember, directories are searched Left to Right
echo $PATH | tr ':' '\n'
# returns the shell path with line breaks
echo $SHELL 
# Gives the location of Shell profile script

ls -a ~
# Generates file listings
# Find .bash_profile, open in text editor
# This is ran each time a new shell (terminal) window is opened

export PATH="Users/ChrisErnst:$PATH"
# The above line could be added to the text file if that path contained executable files
# The command export PATH=/usr/local/bin:$PATH 
# prepends the directory /usr/local/bin to the current PATH, 
# so it becomes the first directory searched by the shell
echo 'export PATH=/usr/local/bin:$PATH' >>~/.bash_profile
# This gives the computer new places to search for executable files found Left to Right in order of priority


### SHORTCUTS
        
Ctrl + A
# Go to the beginning of the line you are currently typing on. This also works for most text input fields system wide. Netbeans being one exception
Ctrl + E
# Go to the end of the line you are currently typing on. This also works for most text input fields system wide. Netbeans being one exception
Ctrl + Q
# Clears everything on current line
Ctrl + L
# Clears the Screen
⌘Cmd + K
# Clears the Screen
Ctrl + U
# Cut everything backwards to beginning of line
Ctrl + K
# Cut everything forward to end of line
Ctrl + W
# Cut one word backwards using white space as delimiter
Ctrl + Y
# Paste whatever was cut by the last cut command
Ctrl + H
# Same as backspace
Ctrl + C
# Kill whatever you are running
Ctrl + D
# Exit the current shell when no process is running, or send EOF to a the running process
Ctrl + Z
# Puts whatever you are running into a suspended background process. fg restores it.
Ctrl + _
# Undo the last command. (Underscore. So it's actually Ctrl + Shift + minus)
Ctrl + T
# Swap the last two characters before the cursor
Ctrl + F
# Move cursor one character forward
Ctrl + B
# Move cursor one character backward
Esc + F
# Move cursor one word forward
Esc + B
# Move cursor one word backward
Esc + T
# Swap the last two words before the cursor
Tab


### DIRECTORY MANAGEMENT 

mkdir [dir]
# Create new directory
mkdir ‐p [dir]/[dir]
# Create nested directories
rmdir [dir]
# Remove directory ( only operates on empty directories )
rm ‐R [dir]
# Remove directory and contents
[command] | [command]
# Allows to combine multiple commands that generate output, e.g. `cat data.txt
less
# Output content delivered in screensize chunks
[command] > [file]
# Push output to file, keep in mind it will get overwritten
[command] >> [file]
# Append output to existing file
[command] < [file]
# Tell command to read content from a file


### CHAINING COMMANDS

[command‐a]; [command‐b]
# Run command A and then B, regardless of success of A
[command‐a] && [command‐b]
# Run command B if A succeeded
[command‐a]
[command‐a] &
# Run command A in background


### PIPING COMMANDS

[command‐a] | [command‐ b]
# Run command A and then pass the result to command B e.g ps auxwww | grep google


### COMMAND HISTORY

history n
# Shows the stuff typed – add a number to limit the last n items
Ctrl + r
# Interactively search through previously typed commands
![value]
# Execute the last command typed that starts with ‘value’
!!
# Execute the last command typed


### SEARCH

find [dir] ‐name [search_pattern]
# Search for files, e.g. find /Users ‐name "file.txt" 
grep [search_pattern] [file]
# Search for all lines that contain the pattern, e.g. grep "Tom" file.txt
grep ‐r [search_pattern] [file]
# Recursively search for all lines that do not contain the pattern
grep ‐v [search_pattern] [file]
# Search for all lines that do NOT contain the pattern


### HELP

[command] ‐h
# Offers help
[command] —help
# Offers help
info [command]
# Offers help
man [command]
# Show the help manual for [command]
whatis [command]
# Gives a one‐line description of [command]
apropos [search‐pattern]
# Searches for command with keywords in description






### EDITING IN TERMINAL

i #begins insertion of text
# make changes
# Press 'ESC' key
:w # then 'Enter' writes the file
:q # then 'Enter' quits the file


##### SPECIFIC APPLICATIONS


###  PYTHON

python scriptName.py 
python --version

### GIT

git init
git add *
git commit -m "First commit"
git remote add origin URLofRepo
git remote -v
git push -u origin master
# If the repo has files inconsistent to which you have, need to use pull, then push
git pull origin master --allow-unrelated-histories

###  ANACONDA
conda update conda



### HOMEBREW

brew update
brew install pyenv
brew upgrade pyenv
brew install awsebcli

# PYENV

pyenv which python
# Gives the current version of Python
pyenv versions
#Lists all versions installed
pyenv install -l
# Lists available versions
pyenv install 2.6.9
# Will install to ~/.pyenv/versions
pyenv global
# Lists the global current version used
pyenv global 3.1.5
# Sets the global current version to be Py 3.1.5
pyenv global system 2.7.12 3.1.5 3.2.6 3.3.6 3.4.5 3.5.2 2.6.9
# Load our python versions IN THIS ORDER
# Allows the above versions of Python to be concurrently ran in preference from Left to Right

# You can also switch the python version you want to use locally (per project) 
# by using a .python-version file at the root of your project.
# When you enter this directory, pyenv will load the python 
# version’s specified in your .python-version.

cd ~/Sites/some-project/
# set the directory that we want to use this verison of Python
pyenv local 3.2.6
# created a `.python-version` file with content:
# 3.2.6


# ELASTIC BEANSTALK (AMAZON WEB SERVICES) - AWS

eb --version
