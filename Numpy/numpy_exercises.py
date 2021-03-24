# -*- coding: utf-8 -*-
"""numpy-exercises.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11E0swhLp8T0OaJVR2JhvMnDRmCIjTwRS

# NumPy Practice

This notebook offers a set of exercises for different tasks with NumPy.

It should be noted there may be more than one different way to answer a question or complete an exercise.

Exercises are based off (and directly taken from) the quick introduction to NumPy notebook.

Different tasks will be detailed by comments or text.

For further reference and resources, it's advised to check out the [NumPy documentation](https://numpy.org/devdocs/user/index.html).

And if you get stuck, try searching for a question in the following format: "how to do XYZ with numpy", where XYZ is the function you want to leverage from NumPy.
"""

# Import NumPy as its abbreviation 'np'
import numpy as np

# Create a 1-dimensional NumPy array using np.array()
a1 = np.array([1,2,3])

# Create a 2-dimensional NumPy array using np.array()
a2 = np.array([[1,2,3],
               [4,5,6]])

# Create a 3-dimensional Numpy array using np.array()
a3 = np.array([[[1,2,3],
                [4,5,6],
                [7,8,9]],
                [[10,11,12],
                  [13,14,15],
                  [16,17,18]]] )

"""Now we've you've created 3 different arrays, let's find details about them.

Find the shape, number of dimensions, data type, size and type of each array.
"""

# Attributes of 1-dimensional array (shape, 
# number of dimensions, data type, size and type)
a1.shape,a1.ndim,a1.dtype,a1.size,type(a1)

# Attributes of 2-dimensional array
a2.shape,a2.ndim,a2.dtype,a2.size,type(a2)

# Attributes of 3-dimensional array
a3.shape, a3.ndim, a3.dtype, a3.size,type(a3)

# Import pandas and create a DataFrame out of one
import pandas as pd

# of the arrays you've created
df = pd.DataFrame(a2)
df

# Create an array of shape (10, 2) with only ones
ones = np.ones((10,2))
ones

# Create an array of shape (7, 2, 3) of only zeros
zeros = np.zeros((7,2,3))
zeros

# Create an array within a range of 0 and 100 with step 3
range_array = np.arange(0,100,3)
range_array

# Create a random array with numbers between 0 and 10 of size (7, 2)
random_array =np.random.randint(10,size=(7,2))
random_array

# Create a random array of floats between 0 & 1 of shape (3, 5)
np.random.random((3,5))

# Set the random seed to 42
np.random.seed(42)

# Create a random array of numbers between 0 & 10 of size (4, 6)
random_array_2 = np.random.randint(10,size=(4,6))
random_array_2

"""Run the cell above again, what happens?

Are the numbers in the array different or the same? Why do think this is?
"""

# Create an array of random numbers between 1 & 10 of size (3, 7)
random_array_3 = np.random.randint(10,size=(3,7))
# and save it to a variable


# Find the unique numbers in the array you just created
np.unique(random_array_3)

# Find the 0'th index of the latest array you created
random_array_3[0]

# Get the first 2 rows of latest array you created
random_array_3[:2]

# Get the first 2 values of the first 2 rows of the latest array
random_array_3[:2,:2]

# Create a random array of numbers between 0 & 10 and an array of ones
# both of size (3, 5), save them both to variables
a4 = np.random.randint(10,size=(3,5))
ones = np.ones((3,5))
a4

# Add the two arrays together
a4 + ones

# Create another array of ones of shape (5, 3)
ones = np.ones((5,3))
ones

# Try add the array of ones and the other most recent array together
a4 + ones.T

"""When you try the last cell, it produces an error. Why do think this is?

How would you fix it?
"""

# Create another array of ones of shape (3, 5)
ones = np.ones((3,5))

# Subtract the new array of ones from the other most recent array
a4 - ones

# Multiply the ones array with the latest array
a4 * ones

# Take the latest array to the power of 2 using '**'
a4 ** 2

# Do the same thing with np.square()
np.square(a4)

# Find the mean of the latest array using np.mean()
np.mean(a4)

# Find the maximum of the latest array using np.max()
np.max(a4)

# Find the minimum of the latest array using np.min()
np.min(a4)

# Find the standard deviation of the latest array
np.std(a4)

# Find the variance of the latest array
np.var(a4)

# Reshape the latest array to (3, 5, 1)
a4.reshape(3,5,1)

# Transpose the latest array
a4.T

"""What does the transpose do?"""

# Create two arrays of random integers between 0 to 10
# one of size (3, 3) the other of size (3, 2)
mat1 = np.random.randint(10,size=(3,2))
mat2 = np.random.randint(10,size=(3,2))

# Perform a dot product on the two newest arrays you created
np.dot(mat1,mat2.T)

# Create two arrays of random integers between 0 to 10
# both of size (4, 3)
mat3 = np.random.randint(10,size=(4,3))
mat4 = np.random.randint(10,size=(4,3))

# Perform a dot product on the two newest arrays you created
np.dot(mat3,mat4)

"""It doesn't work. How would you fix it?"""

# Take the latest two arrays, perform a transpose on one of them and then perform 
# a dot product on them both
np.dot(mat3,mat4.T)

"""Notice how performing a transpose allows the dot product to happen.

Why is this?

Checking out the documentation on [`np.dot()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html) may help, as well as reading [Math is Fun's guide on the dot product](https://www.mathsisfun.com/algebra/vectors-dot-product.html).

Let's now compare arrays.
"""

# Create two arrays of random integers between 0 & 10 of the same shape
# and save them to variables
mat5 = np.random.randint(10,size=(5,2))
mat6 = np.random.randint(10,size=(5,2))

# Compare the two arrays with '>'
mat5 > mat6

"""What happens when you compare the arrays with `>`?"""

# Compare the two arrays with '>='
mat5 >= mat6

# Find which elements of the first array are greater than 7
mat5 > 7

# Which parts of each array are equal? (try using '==')
mat5 == mat6

# Sort one of the arrays you just created in ascending order
np.sort(mat5)

# Sort the indexes of one of the arrays you just created
np.argsort(mat5)

# Find the index with the maximum value in one of the arrays you've created
np.argmax(mat5)

# Find the index with the minimum value in one of the arrays you've created
np.argmin(mat5)

# Find the indexes with the maximum values down the 1st axis (axis=1)
# of one of the arrays you created
np.argmax(mat6,axis=1)

# Find the indexes with the minimum values across the 0th axis (axis=0)
# of one of the arrays you created
np.argmax(mat6,axis=0)

# Create an array of normally distributed random numbers
np.random.randn(3,5)

# Create an array with 10 evenly spaced numbers between 1 and 100
np.linspace(1,100,10)

"""## Extensions

For more exercises, check out the [NumPy quickstart tutorial](https://numpy.org/doc/stable/user/quickstart.html). A good practice would be to read through it and for the parts you find interesting, add them into the end of this notebook.

Pay particular attention to the section on broadcasting. And most importantly, get hands-on with the code as much as possible. If in dobut, run the code, see what it does.

The next place you could go is the [Stack Overflow page for the top questions and answers for NumPy](https://stackoverflow.com/questions/tagged/numpy?sort=MostVotes&edited=true). Often, you'll find some of the most common and useful NumPy functions here. Don't forget to play around with the filters! You'll likely find something helpful here.

Finally, as always, remember, the best way to learn something new is to try it. And try it relentlessly. If you get interested in some kind of NumPy function, asking yourself, "I wonder if NumPy could do that?", go and find out.
"""