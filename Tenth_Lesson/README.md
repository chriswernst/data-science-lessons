
# Most Used Python Functions, Keywords, & Modules
##### November 15, 2017
###### by Chris Ernst
###
This list is not comprehensive

***Listed in Prioritized Order***
### Built in Functions
https://docs.python.org/3.5/library/functions.html
```
len()
print()
range()
type()
sum()
round()
pow()
abs()
dir()
float()
enumerate()
format()
help()
int()
list()
max()
min()
set()
str()
locals()
zip()
```

### Keywords
###
```
import
from
as
for
if
elif
else
def
return
while
or
and
del
try
False
True
None
break
class
continue
except
global
in
is
not
pass
```



### Modules
1. numpy
2. os
3. matplotlib
4. Pandas
###
##### numpy
###
https://docs.scipy.org/doc/numpy/reference/routines.html
Commonly called as `import numpy as np`

![alt text](https://galeascience.files.wordpress.com/2016/08/popular_numpy_functions1.png)

```
import numpy as np

# Square Root
np.sqrt(25)

# Pi
np.pi

# Sum
np.sum([3,5,8,20])

# Size
a=[12,15,0,9,8]
np.size(a, axis=0)

# Mean (Average)
np.mean(a)

# Exponential
np.exp(1)

# Arange
theRange = np.arange(3,300,5)

# linspace
np.linspace(3,5,10)

# Array
b = np.array([0,3,4])
type(b)

# Recast as Array
a=np.asarray(a)

# Matrix
matA = np.matrix([[0,1],[3,2]])
matB = np.matrix('0 1; 3 2')

# Shape
np.shape(matA)
np.shape(matB)

# Reshape
a=[12,15,0,9]
np.reshape(a, (2,2))

# NonZero
np.nonzero(a)

# Insert
newMatA = np.insert(matA, 2, [2,4], axis=1)

# Ones and Zeros Matrices
allOnesMatrix = np.ones([5,5])

allZerosMatrix = np.zeros([200,20])

# 'Empty'
np.empty([20,20])

# Append
a=[12,15,0,9]
a=np.append(a, [3,5,8,1,22,36,4])

# Where
a=a[0:5]
np.where(a>8)
a=np.where(a>8,-66,a)
```