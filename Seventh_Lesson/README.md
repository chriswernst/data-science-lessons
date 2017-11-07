
### Lesson for November 7, 2017
###

### Agenda
###
##### **1.** Git fetch latest repository (the proper way)
###
`$ git remote add upstream URL_of_REPO`
`$ git fetch upstream`

[Cheat Link -  Sync the forked Repository](https://help.github.com/articles/syncing-a-fork/)
###
###

##### **2.** Review - Operators, Variables, Keywords & Built-ins
###

**Operators:** 
```
+ Addition
- Subtraction
/ Division
// Floor Division (Returns division without a decimal)
* Multiplication
** Exponentiation
% Modulus (Returns the remainer of the division)
== 'is equal to'
```
###
**Variables:** 
Single Variable Assignment:
c = 12
###
###
Define the Function:
```
def pythagoreanTheorem(a,b):
    c = a**2 + b**2
    print("The hypoteneuse is: ", c)
    return c
```
Call the Function:
```
hypoteneuse = pythagoreanTheorem(3,8)
```
Define a new multi-output function:
```
def thisNewFunction(a=10,m=3):
    b = a**m
    c = a//m
    return b,c
```
Call the function, and assign both outputs variable names:
```
exponentiation, division = thisNewFunction(a=323, m=13)
```

**Keywords:**
```
import keyword
keywords = keyword.kwlist
len(keywords)
```
There are 33 keywords

```
allBuiltins = dir(__builtins__)
errors = allBuiltins[:70]
builtins = allBuiltins[79:]

```
*keywords* should turn **blue**, and *functions* should turn **purple** when typed into **Spyder.**
###
Remember, you ***can not*** assign variables the names of keywords or built in functions!

**Built-ins:**
Examples:
```
abs()
len()
dir()
help()
min()
max()
pow()
```

