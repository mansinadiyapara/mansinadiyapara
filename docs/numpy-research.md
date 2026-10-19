# NumPy Research

## 1. What is NumPy?

NumPy stands for Numerical Python. It is a Python library used for numerical calculations and working with arrays.

It solves the problem of performing mathematical operations on large collections of numerical data efficiently. It provides multidimensional arrays and operations that work directly on those arrays.

## 2. NumPy Arrays

A NumPy array stores a collection of values in a structured format.

Example:

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])
print(numbers)
```

Output:

```text
[10 20 30 40]
```

## 3. Dimensions

Dimensions represent the number of axes in an array. A one-dimensional array has one axis, and a two-dimensional array has two axes.

Example:

```python
a = np.array([1, 2, 3])
print(a.ndim)
```

Output: `1`

## 4. Shape

Shape describes the size of an array along each axis.

Example:

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)
```

Output: `(2, 3)`

This means the array has two rows and three columns.

## 5. dtype

The `dtype` attribute tells us the data type of the array elements.

Example:

```python
a = np.array([10, 20, 30])
print(a.dtype)
```

The output is typically `int64` on a 64-bit NumPy installation.

## 6. Indexing

Indexing is used to access a specific element by its position.

Example:

```python
a = np.array([10, 20, 30, 40])
print(a[2])
```

Output: `30`

## 7. Slicing

Slicing selects a range of elements from an array.

Example:

```python
a = np.array([10, 20, 30, 40, 50])
print(a[1:4])
```

Output: `[20 30 40]`

The start index is included, and the stop index is excluded.

## 8. Mathematical Operations

NumPy supports element-wise arithmetic without requiring an explicit Python loop.

Example:

```python
a = np.array([10, 20, 30])
print(a * 2)
```

Output: `[20 40 60]`

## 9. Boolean Conditions

Boolean conditions allow us to select elements that satisfy a condition.

Example:

```python
a = np.array([10, 20, 30, 40])
print(a[a > 20])
```

Output: `[30 40]`

## 10. Aggregation

Aggregation calculates summary values from an array, such as the sum, average, minimum, and maximum.

Example:

```python
a = np.array([10, 20, 30, 40])

print(a.sum())
print(a.mean())
print(a.min())
print(a.max())
```

Output:

```text
100
25.0
10
40
```

## 11. Broadcasting

Broadcasting allows NumPy to perform operations between compatible arrays of different shapes.

Example:

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])

print(a + b)
```

Output:

```text
[[11 22 33]
 [14 25 36]]
```

## 12. Why Use NumPy Instead of a Python List?

Python lists are useful for general-purpose collections, but numerical operations on lists often require explicit loops.

NumPy arrays support element-wise arithmetic, multidimensional data, Boolean filtering, and aggregation directly. They can also use memory more efficiently and perform many numerical operations faster, especially on large datasets.

## 13. Conclusion

NumPy makes numerical data easier to store, process, and analyze. Understanding arrays, dimensions, shape, data types, indexing, slicing, arithmetic, Boolean conditions, aggregation, and broadcasting provides a foundation for data analysis and machine learning.