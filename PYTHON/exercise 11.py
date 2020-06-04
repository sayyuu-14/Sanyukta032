1.Write a NumPy program to create a 3X4 array using and iterate over
it.

import numpy as np
array = np.arange(4,16).reshape((3, 4))
print(array)
for i in np.nditer(array):
  print(i)

  
2. Write a NumPy program to create a vector of length 10 with values
evenly distributed between 5 and 50.

import numpy as np
print(np.linspace(5,50,10))

3. Write a NumPy program to create a vector with values from 0 to 20 and
change the sign of the numbers in the range from 9 to 15.

import numpy as np
import numpy as np
arr = np.arange(0,21)
print(arr)
(arr[9:16]) *= -1
print(arr)


4.  Write a NumPy program to create a vector of length 5 filled with
arbitrary integers from 0 to 10.

import numpy as np
print(np.random.randint(0, 11, 5))


5. Write a NumPy program to multiply the values of two given vectors.

import numpy as np
a=np.array([8,3,9,2])
print(a)
b=np.array([4,2,9,1])
print(b)
print(a*b)

6. Write a NumPy program to create a 3x4 matrix filled with values from
10 to 21.
import numpy as np
print(np.arange(10,22).reshape((3, 4)))

7.  Write a NumPy program to find the number of rows and columns of a
given matrix.

import numpy as np
arr= np.arange(4,16).reshape((3, 4))
print(arr.shape)

8. Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal
elements are 1, the rest are 0.

import numpy as np
print(np.eye(3))

9.  Write a NumPy program to create a 10x10 matrix, in which the
elements on the borders will be equal to 1, and inside 0.

import numpy as np
arr = np.ones((10, 10))
arr[1:-1,1:-1] = 0
print(arr)


10. Write a NumPy program to create a 5x5 zero matrix with
elements on the main diagonal equal to 1, 2, 3, 4, 5.

import numpy as np
print(np.diag([1, 2, 3, 4, 5]))

11. Write a NumPy program to create a 4x4 matrix in which 0 and 1
are staggered, with zeros on the main diagonal.

import numpy as np
arr = np.diag([0,0,0,0])
arr[::2, 1::2] = 1
arr[1::2, ::2] = 1
print(arr)

12. Write a NumPy program to create a 3x3x3 array filled with
arbitrary values.


import numpy as np
print(np.random.random((3, 3, 3)))



13. Write a NumPy program to compute sum of all elements, sum of
each column and sum of each row of a given array. 

import numpy as np
arr = np.array([[8,9],[6,3]])
print(np.sum(arr))
print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))
    

14. Write a NumPy program to compute the inner product of two
given vectors.



import numpy as np
a1 = np.array([1,3])
a2 = np.array([7, 5])
print(np.dot(a1, a2))

15. Write a NumPy program to add a vector to each row of a given

import numpy as np
arr1 = np.array([[1,1,1], [0,9,0], [7,5,1], [1,9,0]])
arr2 = np.array([5,7,1])
for i in range(0,4):
  arr1[i, :] +=  arr2
print(arr1)
