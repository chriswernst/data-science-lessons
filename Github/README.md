# How to Create a New Repository on Github

**1.** From your Github profile, navigate to the upper right hand corner, and click the '+' icon. Select new repository. Name it, and do not add a README.

**2.** Open a terminal, and set the directory to where the folder is located: `cd ~/path/to/folder/`

###

**3.** Type: `git init`
###
This initializes the repository
###

**4.** Type: `git add filename` OR `folder_name`
###
This adds the file to be uploaded
###

**5.** Type: `git commit -m "feat: meaningful message here"`
###
This commits the file and records the commit message
###

**6.** Type: `git remote add origin github_url_of_repository`
###
This syncs your local directory with the github repository
*Note: this only has to be done the first time you commit to a repository*
###

**7.** Type: `git remote -v`
###
This verifies the github repository
###

**8.** Type: `git push -u origin master`
###
This pushes the local files to the github repository
###
(Note: If this returns you an error, you may not have congruency between your local files, and those on your repo. Solve this with: `git pull origin master --allow-unrealted-histories`)

###

#### And that's it! The files should now be on your github repository.

