---
title: Quiz 2
weight: 15
description: Study guide and sample long-form problems for Quiz 2.
---



## Format and Rules
- The quiz is **in class**, Thursday, October 2.
- A mix of multiple choice, fill-in-the-blank, and long answer questions.
- You will not be programming in PyCharm, but you may be asked to write or edit code snippets by hand.
- You may bring ***1 side of 1 sheet of letter paper*** with your own ***hand-written*** notes. 
- An Honor Code violation on the any quiz or exam result in a course grade of F.
- Failure to submit a quiz or exam results in a course grade of F.

## Content
- Study ***key terms*** from slides and labs. Look for <u><b>boldfaced, underlined terms</b></u> in slides and ***emphasized terms*** in labs.
- Study ***Knowledge Checks*** from labs.
- Writing a good Problem Statement when provided a high-level description of the program goals. (week 4)
- Testing concepts (terms) and application (weeks 4-6), including:
   - Creating a [control flow graph](../../labs/cfg/) for a given function and identifying all ***unique program paths***.
   - Writing or analyzing [unit tests](../../labs/testing/) for a given function, including:
      - `assert` statements
      - testing if exceptions are raised using `pytest` functions
      - writing tests that cover all unique program paths from a CFG.


## Sample CFG and Testing problems
You will be asked to draw CFGs and write test cases that cover all program paths. 

**Disclaimer:** You will have other knowledge check questions beyond these types of questions.


### Sample 1
```python{linenos=true}
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
```
1. Draw the CFG for this code using the conventions from class.
2. List the unique program paths.
3. Add `assert` statements to the following test case that exercise all unique program paths.
   ```python
   def test_is_prime():
      # Your code here.
   ```

#### Solution

{{< details "CFG for is_prime()">}}
{{< figure src="is_prime.png" width="640">}}
{{< /details >}} 

{{< details "unique program paths">}}
The unique edges in the path are highlighted. You do not need to highlight the unique edges on the quiz.
1. (1, **2, 3**)
2. (1, 2, **4, 7**)
3. (1, 2, 4, **5, 6**)
4. (1, 2, 4, **5, 4**, 7) or (1, 2, 4, **5, 4**, 5, 6)
{{< /details >}} 

{{< details "test case">}}
```python
def test_is_prime():
   # Some paths can be exercised with multiple input values. 
   # The goal is to exercise all program paths.

   assert is_prime(1) == True  # tests path (1, 2, 3)
   assert is_prime(2) == True  # path (1, 2, 4, 7)
   assert is_prime(4) == False  # path (1, 2, 4, 5, 6)
   assert is_prime(5) == True  # path (1, 2, 4, 5, 4, 7)
```
{{< /details >}} 

### Sample 2
```python{linenos=true,linenostart=14}
def generate_fibonacci(n):
    if n <= 0:
        return "Error: Number of terms must be a positive integer"
    
    fibonacci_sequence = [1]
    a = 1
    b = 2
    count = 1
    
    while count < n:
        fibonacci_sequence.append(a)
        # Update values of a and b to the next numbers in the sequence
        a, b = b, a + b
        count += 1

    return fibonacci_sequence
```
1. Draw the CFG for this code using the conventions from class.
2. List the unique program paths.
3. Add `assert` statements to the following test case that exercise all unique program paths.
   ```python
   def test_generate_fibonacci():
      # Your code here.
   ```


#### Solution

{{< details "CFG for generate_fibonacci()">}}
{{< figure src="generate_fibonacci.png" width="640">}}
{{< /details >}} 

{{< details "unique program paths">}}
The unique edges in the path are highlighted. You do not need to highlight the unique edges on the quiz.
1. (14, **15, 16**)
1. (14, 15, 18-21, **23, 29**)
1. (14, 15, 18-21, **23, 24-27**, 23, 29)
{{< /details >}} 

{{< details "test case">}}
```python
def test_generate_fibonnaci():
   # Some paths can be exercised with multiple input values. 
   # The goal is to exercise all program paths.

   assert generate_fibonnaci(0) == "Error: Number of terms must be a positive integer"  # tests path (14, 15, 16)
   assert generate_fibonnaci(1) == [1]  # path (14, 15, 18-21, 23, 29)
   assert generate_fibonnaci(6) == [1, 1, 2, 3, 5, 8]  # path (14, 15, 18-21, 23, 24-27, 23, 29)
```
{{< /details >}} 


### Sample 3
```python{linenos=true,linenostart=36}
def factorial(n):
    # Input validation
    if not isinstance(n, int) or n < 0:
        return "Error: Input must be a non-negative integer"
    
    # Use iterative approach
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```
1. Draw the CFG for this code using the conventions from class.
2. List the unique program paths.
3. Add `assert` statements to the following test case that exercise all unique program paths.
   ```python
   def test_factorial():
      # Your code here.
   ```

#### Solution

{{< details "CFG for factorial()">}}
{{< figure src="factorial.png" width="640">}}
{{< /details >}} 

{{< details "unique program paths">}}
The unique edges in the path are highlighted. You do not need to highlight the unique edges on the quiz.
1. (36, **38, 39**)
1. (36, 38, 42, **43, 45**)
1. (36, 38, 42, **43, 44**, 43, 45)
{{< /details >}} 

{{< details "test case">}}
```python
def test_factorial():
   # Some paths can be exercised with multiple input values. 
   # The goal is to exercise all program paths.

   assert factorial("Alice") == "Error: Number of terms must be a positive integer"  # tests path(36, 38, 39)
   assert factorial(-1) == "Error: Number of terms must be a positive integer"  # also tests path(36, 38, 39)
   assert factorial(0) == 1  # tests path(36, 38, 42, 43, 45)
   assert factorial(5) == 120  # tests path(36, 38, 42, 43, 44, 43, 45)


```
{{< /details >}} 