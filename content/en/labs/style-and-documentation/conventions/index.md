---
title: Coding conventions
description: Readability is a function of names and style.
weight: 5
---

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/VwJdqH59ZN0?si=iPS277tngVA3ZQ28" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Motivation

> "Readability counts."
> 
> &ndash; Tim Peters, long-time Python contributor, *The Zen of Python*

You were probably taught to give your variables descriptive names, such as `total = price + tax`, as opposed to `t = p + tax`. But, sometimes, you are told there are traditional variable names, like 
```python
for i in range(1, 4):  # i is the outer loop index
    for j in range(1, 4):  # j is the inner loop index
        print(i, j)  
```

Consider the following code with poor variable names and improper spacing:
```python
def bs(a,x):
  there=False
  fst,lst = 0,len(a)-1
  while fst<=lst and not there:
    mid=(fst+lst)//2
  if x<a[mid]:
    lst=mid-1
  elif x>a[mid]:
    fst=mid+1
  else:
    return True
  return False
```
As a developer, it would certainly take me a minute to figure out what this function does. Better names would go a long way for sure. But also, the improper spacing makes it needlessly difficult to see what each line is doing. In Python, every operator should have a single space around it. For example, `lst=mid-1` should be `lst = mid - 1`.

Now compare to a properly named, properly spaced solution:

```python
def binary_search(lst, target):
    found = False
    first, last = 0, len(lst) - 1

    while first <= last and not found:
        mid = (first + last) // 2
    if x < lst[mid]:
        last = mid - 1
    elif x > lst[mid]:
        first = mid + 1
    else:
        return True

    return False
```

## Coding conventions in Python
***Coding conventions*** are the rules for naming, spacing, and commenting adopted by an organization. These conventions are often *language-specific*. Google has coding conventions for many languages that they expect their developers to follow, for example. Many organizations will use their own conventions. One of the nice things about coding conventions is that they can be checked by tools in the IDE to let you know if you're violating them.

The creators of Python have published a set of coding conventions for the whole language, called [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/), which we will follow in this class. 

The sections below are a subset of the rules that I consider the most impactful on readability.

### Naming rules
1. Variable and function names are `lowercase_with_underscores` only.
1. Function names are verbs or begin with a verb, e.g., `compute_risk()`
1. Variable and class names should be nouns, e.g., `body_mass_index = 20.0`
2. Class names are `PascalCase` beginning with an uppercase letter, e.g., `PatientRecord`
3. File names (modules) are `lowercase` letters. You may use `_` if it improves readability.

### Blank lines
1. Top-level function and class bodies are followed by two blank lines.
1. Method definitions inside a class are surrounded by a single blank line.
1. Use blank lines in functions, sparingly, to indicate logical sections.
1. Otherwise, avoid unnecessary blank lines!

### Whitespace within lines
1. Do *not* put whitespace immediately inside parentheses, brackets, or braces. 
    - Do: `spam(ham[1], {eggs: 2})`
    - No: `spam( ham[ 1 ] , { eggs: 2 } )`
1. Do *not* put whitespace immediately before a comma, semicolon, or colon:
    - Do: `if x == 4: print(x, y); x, y = y, x` 
    - No: `if x == 4 : print(x , y) ; x , y = y , x`
1. Most operators get one space around them.
1. Otherwise, avoid unnecessary whitespace!

### Other
1. Do not initialize multiple variables on one line unless necessary.
1. Use Python's [type hints](https://docs.python.org/3/library/typing.html) to indicate the intended type (if known) of class variables, function parameters, and function return types. Read the [official documentation](https://docs.python.org/3/library/typing.html) for examples.

## Summary
Consistently applying coding conventions makes your code easier to understand.

We can use tools to help enforce coding conventions, and we will do so soon. For now, concentrate on learning the Python naming and spacing conventions above.


## Knowledge check
- Define ***coding conventions***.
- What are the PEP8 violations in the following code block? How do you fix them?
  ```python
  class patient:

    def __init__(self,firstName,lastName,age):
      self.firstName=firstName
      self.lastName=lastName
      self.age=age


    def computeBill(self,fee,interest):
      return fee*(1+interest)
    def printRecord(self):
      print(f"{self.firstName} {self.lastName} {self.age}")
  
  if __name__ == "__main__":
    bob = patient('bob', 'bobberton', 55)
    bob.printRecord()
  ```

