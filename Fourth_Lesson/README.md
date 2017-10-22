# Lesson for October 18, 2017

###
###

### Agenda
###
##### **1.** Git fetch latest repository (the proper way)
###
Fork Repository (if not done already)
Update fork -> in Google: `How do you update a forked repository on Github?`
###
`$ git remote add upstream URL_of_REPO`
`$ git fetch upstream`
If this doesn't work, how do we make it work?
###
StackOverflow / Google 

[Cheat Link 1 -  Configure the remote](https://help.github.com/articles/configuring-a-remote-for-a-fork/)
[Cheat Link 2 -  Sync the forked Repository](https://help.github.com/articles/syncing-a-fork/)
###
###

##### **2.** Review 
###
Functions can be thought of as subprograms
```
def myPythonFunction(requirement1,requirement2):
	req3=requirement1+requirement2
	return req3
```
###
- Set the directory in Python
###
- Libraries and their relation to functions
###
- Referencing Functions in libraries: `import ____________` & `from ______ import *` & `import _______ as ___`
###
- Imitate the above to write your own
###
- Comments/ Documentation
###
- camelCase
###
- THIS_IS_A_CONSTANT
###
- thisIsAVariable
###
###

###### A mention of defining entire programs in functions

###
###

##### **3.** Python Loops
###
**Definite Loops - for**

###
```
for i in range(10):
	print(i)
```
###

**Indefinite Loops - while**

###

Remember, you must alter the condition at some point in the loop, or it will run forever!
```
import time
x=20
while x>10:
    time.sleep(0.25)
    print(x)
    x=x-1

```



###
##### **4.** Your First Program - *Hello World*
###
- Pseudocode
###
- Readability, Spacing, Comments
###
- Program Development Process
###
- Reference a function in another python file (Remember directory management)
### 
- Use the `requests` and `bs4` libraries to create a script

