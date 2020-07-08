### Data Analysis with Python Certification (300 hours)

#### Data Analysis with Python Course


[Introduction to the Data Analysis with Python Course Lectures](#Introduction-to-the-Data-Analysis-with-Python-Course-Lectures)  
[1 Introduction to Data Analysis](#1-Introduction-to-Data-Analysis)  
[2 Data Analysis Example A](#2-Data-Analysis-Example-A)  
[3 Data Analysis Example B](#3-Data-Analysis-Example-B)  
[4 How to use Jupyter Notebooks Intro](#4-How-to-use-Jupyter-Notebooks-Intro)  
[5 Jupyter Notebooks Cells](#5-Jupyter-Notebooks-Cells)  
[6 Jupyter Notebooks Importing and Exporting Data](#6-Jupyter-Notebooks-Importing-and-Exporting-Data)  
[7 Numpy Introduction A](#7-Numpy-Introduction-A)  
[8 Numpy Introduction B](#8-Numpy-Introduction-B)  
[9 Numpy Arrays](#9-Numpy-Arrays)  
[10 Numpy Operations](#10-Numpy-Operations)  
[11 Numpy Boolean Arrays](#11-Numpy-Boolean-Arrays)  
[12 Numpy Algebra and Size](#12-Numpy-Algebra-and-Size)  
[13 Pandas Introduction](#13-Pandas-Introduction)  
[14 Pandas Indexing and Conditional Selection](#14-Pandas-Indexing-and-Conditional-Selection)  
[15 Pandas DataFrames](#15-Pandas-DataFrames)  
[16 Pandas Condtitional Selection and Modifying DataFrames](#16-Pandas-Condtitional-Selection-and-Modifying-DataFrames)  
[17 Pandas Creating Columns](#17-Pandas-Creating-Columns)  
[18 Data Cleaning Introduction](#18-Data-Cleaning-Introduction)  
[19 Data Cleaning with DataFrames](#19-Data-Cleaning-with-DataFrames)  
[20 Data Cleaning Duplicates](#20-Data-Cleaning-Duplicates)  
[21 Data Cleaning and Visualizations](#21-Data-Cleaning-and-Visualizations)  
[22 Reading Data Introduction](#22-Reading-Data-Introduction)  
[23 Reading Data CSV and TXT](#23-Reading-Data-CSV-and-TXT)  
[24 Reading Data from Databases](#24-Reading-Data-from-Databases)  
[25 Parsing HTML and Saving Data](#25-Parsing-HTML-and-Saving-Data)  
[26 Python Introduction](#26-Python-Introduction)  
[27 Python Functions and Collections](#27-Python-Functions-and-Collections)  
[28 Python Iteration and Modules](#28-Python-Iteration-and-Modules)  


#### Numpy




#### Data Analysis with Python Projects




#### Machine Learning with Python Certification (300 hours)




### Machine Learning with Python Certification (300 hours)

#### TensorFlow






#### How Neural Networks Work





#### Machine Learning with Python Projects



### Data Analysis with Python Certification (300 hours)

#### Data Analysis with Python Course

#### Introduction to the Data Analysis with Python Course Lectures
[youtube](https://www.youtube.com/watch?v=r-uOLxNrNk8&feature=youtu.be)  
[Interactive Notebooks Tutorial](https://notebooks.ai/mlapin/interactive-jupyterlab-tutorial-4606e21c/lab)  
[https://github.com/notebooks-ai](https://github.com/notebooks-ai)  
[]()  
[]()  
[Interactive JupyterLab Tutorial](https://notebooks.ai/rmotr-curriculum/interactive-jupyterlab-tutorial-ac5fa63f)  

```
```
#### 1 Introduction to Data Analysis
```
Why should you choose R over Python for data analysis?

It's better at dealing with advanced statistical methods.
```


#### 2 Data Analysis Example A
```
What does the shape of our dataframe tell us?

How many rows and columns our dataframe has.
```



#### 3 Data Analysis Example B
```
What does the loc method allow you to do?

Access a group of rows and columns by supplying label(s) arguments.
```



#### 4 How to use Jupyter Notebooks Intro
```
```


What is not allowed in a Jupyter Notebook's cell?
An Excel sheet

#### 5 Jupyter Notebooks Cells
```
Which cells are responsible for rich display?

Code Cells
```




#### 6 Jupyter Notebooks Importing and Exporting Data
```
What kind of data can you import and work with in a Jupyter Notebook?
All of the above.
```


#### 7 Numpy Introduction A
[Part 4: Intro to NumPy (01:04:58)](https://notebooks.ai/rmotr-curriculum/freecodecamp-intro-to-numpy-6c285b74)  
[]()  
[]()  
[]()  
[]()  
[]()  

```
Why is Numpy an important, but unpopular Python library?


*Often you won't work directly with Numpy.


It's is extremely slow.


Working with Numpy is difficult.
```



```python
import numpy as np

a = np.array([1, 2, 3, 4])
print(a, a.dtype, a[0:2], a[::2])
# [1 2 3 4] int32 [1 2] [1 3]
c = np.array(['a', 'b', 'c'])
print(c, c.dtype)
d = np.array([{'a': 1}, 'sys'])
print(d)
np.array([1, 2, 3, 4], dtype=np.int8)

```

    [1 2 3 4] int32 [1 2] [1 3]
    ['a' 'b' 'c'] <U1
    [{'a': 1} 'sys']
    




    array([1, 2, 3, 4], dtype=int8)




```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(A.shape, A.ndim, A.size)
```

    (2, 3) 2 6
    



#### 8 Numpy Introduction B
```
About how much memory does the integer 5 consume in plain Python?


32 bits


*20 bytes


16 bytes


8 bits```


#### 9 Numpy Arrays
```
```



```python
A = np.array([
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
])
print(A[:, :2])
# [['a' 'b']
#  ['d' 'e']
#  ['g' 'h']]
```

    [['a' 'b']
     ['d' 'e']
     ['g' 'h']]
    

#### 10 Numpy Operations
```
```


```python
a = np.arange(5)
a + 20
print(a, a + 20)
# [0 1 2 3 4] [20 21 22 23 24]
```

    [0 1 2 3 4] [20 21 22 23 24]
    

#### 11 Numpy Boolean Arrays
```
```


```python
a = np.arange(5)

print(a <= 3)
```

    [ True  True  True  True False]
    

#### 12 Numpy Algebra and Size
```
What is the relationship between size of objects (such as lists and datatypes) in memory in Python's standard library and the NumPy library? Knowing this, what are the implications for performance?

Standard Python objects take up more memory than NumPy objects; operations on NumPy objects complete very quickly compared to comparable objects in standard Python.
]```


#### 13 Pandas Introduction
[]()  
[]()  
[]()  

```
```



```python
import pandas as pd

certificates_earned = pd.Series(
    [8, 2, 5, 6],
    index=['Tom', 'Kris', 'Ahmad', 'Beau']
)

print(certificates_earned)
```

    Tom      8
    Kris     2
    Ahmad    5
    Beau     6
    dtype: int64
    



#### 14 Pandas Indexing and Conditional Selection
```
```



```python
import pandas as pd

certificates_earned = pd.Series(
    [8, 2, 5, 6],
    index=['Tom', 'Kris', 'Ahmad', 'Beau']
)

print(certificates_earned[certificates_earned > 5])
```

    Tom     8
    Beau    6
    dtype: int64
    

#### 15 Pandas DataFrames
```
```



```python
import pandas as pd

certificates_earned = pd.DataFrame({
    'Certificates': [8, 2, 5, 6],
    'Time (in months)': [16, 5, 9, 12]
})

certificates_earned.index = ['Tom', 'Kris', 'Ahmad', 'Beau']

print(certificates_earned.iloc[2])
```

    Certificates        5
    Time (in months)    9
    Name: Ahmad, dtype: int64
    

#### 16 Pandas Condtitional Selection and Modifying DataFrames
```
```



```python
import pandas as pd

certificates_earned = pd.DataFrame({
    'Certificates': [8, 2, 5, 6],
    'Time (in months)': [16, 5, 9, 12]
})
names = ['Tom', 'Kris', 'Ahmad', 'Beau']

certificates_earned.index = names
longest_streak = pd.Series([13, 11, 9, 7], index=names)
certificates_earned['Longest streak'] = longest_streak

print(certificates_earned)

```

           Certificates  Time (in months)  Longest streak
    Tom               8                16              13
    Kris              2                 5              11
    Ahmad             5                 9               9
    Beau              6                12               7
    

#### 17 Pandas Creating Columns
```
```



```python
import pandas as pd

certificates_earned = pd.DataFrame({
    'Certificates': [8, 2, 5, 6],
    'Time (in months)': [16, 5, 9, 12]
})
names = ['Tom', 'Kris', 'Ahmad', 'Beau']

certificates_earned.index = names


certificates_earned['Certificates per month'] = round(
    certificates_earned['Certificates'] /
    certificates_earned['Time (in months)'],2
)


print(certificates_earned)

```

           Certificates  Time (in months)  Certificates per month
    Tom               8                16                    0.50
    Kris              2                 5                    0.40
    Ahmad             5                 9                    0.56
    Beau              6                12                    0.50
    

#### 18 Data Cleaning Introduction
[Data Cleaning RMOTR - FreeCodeCamp](https://notebooks.ai/rmotr-curriculum/data-cleaning-rmotr-freecodecamp-fd76fa59)   
```
```



```python
import numpy as np
a = np.array([1, 2, 3, np.nan, np.nan, 4])
print(a, a.sum(), a.mean(), 3+np.nan)
```

    [ 1.  2.  3. nan nan  4.] nan nan nan
    


```python
print(3+np.inf)
b = np.array([1, 2, 3, np.inf, np.nan, 4], dtype=np.float)
print(b, b.sum())
```

    inf
    [ 1.  2.  3. inf nan  4.] nan
    


```python

```


```python

```


```python

```


```python
import pandas as pd
import numpy as np

s = pd.Series(['a', 3, np.nan, 1, np.nan])

print(s.notnull().sum())
```

    3
    

#### 19 Data Cleaning with DataFrames
```
```



```python
import pandas as pd
import numpy as np

s = pd.Series([np.nan, 1, 2, np.nan, 3])
s = s.fillna(method='ffill')

print(s)
```

    0    NaN
    1    1.0
    2    2.0
    3    2.0
    4    3.0
    dtype: float64
    

#### 20 Data Cleaning Duplicates
```
The Python method .duplicated() returns a boolean Series for your DataFrame. True is the return value for rows that:


contain a duplicate, where the value for the row contains the first occurrence of that value.


===contain a duplicate, where the value for the row is at least the second occurrence of that value.


contain a duplicate, where the value for the row contains either the first or second occurrence.
```



```python
import pandas as pd
import numpy as np

s = pd.Series([np.nan, 1, 2, np.nan, 3])
s = s.duplicated()

print(s)
```

    0    False
    1    False
    2    False
    3     True
    4    False
    dtype: bool
    

#### 21 Data Cleaning and Visualizations
```
When using Matplotlib's global API, what does the order of numbers mean here?: plt.subplot(1, 2, 1)


My figure will have one column, two rows, and I am going to start drawing in the first (left) plot.


I am going to start drawing in the first (left) plot, my figure will have two rows, and my figure will have one column.


My figure will have one row, two columns, and I am going to start drawing in the first (left) plot.
```



```python

```

#### 22 Reading Data Introduction
```
```


#### 23 Reading Data CSV and TXT
```
```


#### 24 Reading Data from Databases
```
```


#### 25 Parsing HTML and Saving Data
```
```


#### 26 Python Introduction
```
```




### 27 Python Functions and Collections
```
```






#### 28 Python Iteration and Modules
```
```

#### Numpy



#### Data Analysis with Python Projects



#### Machine Learning with Python Certification (300 hours)



### Machine Learning with Python Certification (300 hours)

#### TensorFlow



#### How Neural Networks Work



#### Machine Learning with Python Projects






