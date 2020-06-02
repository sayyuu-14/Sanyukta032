
# Write a NumPy program to get the numpy version and show numpy build configuration.

import numpy

print(numpy.show_config(),"\n","version : ",numpy.__version__)


# Write a NumPy program to test element-wise for complex number, real number of a given array. Also test whether a given number is a scalar type or not.

import numpy as np
x = np.array([1+9j, 8+0j, 6585, 0.3, 2, 4j])
print(x)
print(np.iscomplex(x))
print(np.isreal(x))
for i in x:
    print(np.isscalar(i),end=" ")
print(np.isscalar(x))



# Write a NumPy program to test whether none of the elements of a given array is zero.

import numpy as np

array=([1,0,9,10])
print(array)

if np.all(array) == False:
    print("coontains zeros")
else :
    print("array has no zero")


# Write a NumPy program to test whether any of the elements of a given array is non-zero.

import numpy as np

array=([1,0,9,10])
print(array)

if np.any(array) == True:
    print("coontains zeros")
else :
    print("array has no zero")


# Write a NumPy program to test element-wise for NaN of a given array.


import numpy as np
array=([2,46,np.nan,325])
a=np.isnan(array)

if np.any(a) == True:
    print("nan exists")
else:
    print("nan does not exist")


#   Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.

import numpy as np
a=np.array([1,5])
b=np.array([3,4])
print("greater array :",np.greater(a,b))
print("greater_eqaual array :",np.greater_equal(a,b))
print("less array :",np.less(a,b))
print("less_equal :",np.less_equal(a,b))

#   Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.
#Input:
x = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])


import numpy as np

x = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
print("equal:",np.greater(a,b))
print("tollerance array :",np.allclose(a,b))

#   Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array.

import numpy as np
x=np.array([1,7,13,105])
size=x.size * x.itemsize
print(size)



#   Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives.

import numpy as np

print(np.zeros(10))
print(np.ones(10))
print(np.ones(10)*5)

#   Write a NumPy program to create an array of the integers from 30 to 70.

import numpy as np
print(np.arange(30,71))



#   Write a NumPy program to create an array of all the even integers from 30 to 70.

import numpy as np

arr = np.arange(30,71)

print(arr[::2])


#   Write a NumPy program to create a 3x3 identity matrix.

import numpy as np

print(np.identity(3))
print(np.eye(3))

#   Write a NumPy program to generate a random number between 0 and 1.

import numpy as np

print(np.random.rand()



#   Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution.

import numpy as np
      
print(np.random.normal(0,1,15))

# Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.

import numpy as np
a=np.arange(15,56)
print(a[1:-1])
