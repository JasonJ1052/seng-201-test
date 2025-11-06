---
title: Documenting code
description: Properly commenting your code goes a long way toward understandability.
weight: 10
---

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/d2jBemCqodo?si=IMP9klP1dgrpFVNn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Motivation

***Comments*** in code provide a way for you to leave notes to yourself and others about what your code does. These are very useful, if not essential, in a team setting. The term ***code documentation*** in general refers to the set of comments in source code that, hopefully, explain something about that code.

Code documentation is a double-edged sword. Done well, it helps you and others understand your code. Done poorly, it provides no value and can even mislead. Further, code documentation needs to be updated when the code is updated!


## Three simple rules
We want our code documentation to be clear and concise, just like the code itself. Here is what we will focus on documenting.

1. Code should be *self-documenting* to the greatest extent possible.
1. Document the purpose of classes and modules (files).
1. Document the purpose, parameters, return values, and exceptions of functions.

You can apply these rules to almost any language you encounter, and you will find that the recommendations for creating class and function comments different per language.

## Self-documenting code

Self-documenting code is a popular term for "I can look at the code and understand it's purpose." How do you achieve that?

### Naming
**Use descriptive variable, function, and class names** according to your team's [coding conventions](../conventions/).

Variables and classes should be **nouns** that describe the data.
- Keep them short and concise, say, 16 characters max. Shorter is better.
- Use plural nouns to represent lists, sets, and other collections.
- Do *not* use built-in names for variables, like `max`, `min`, `sum`. 
 - Examples:
   - `for name in birds:` where `birds` is a list of strings.
   - `total = sum(scores)`

Functions should be **verbs** or start with a verb. They should describe what the function does. 
  - Again, strive to be concise. 
  - If a phrase better describes the function, split the words with underscores (Python convention), such as `compute_average_score()`. In Java, you would use camelCase


### Comments
In-line comments are useful but should not be abused. Use in-line comments to:
1. Summarize a complex block of code.
2. Explain an implementation or design choice.

Do **not** write a comment for every line. A programmer proficient in the programming language should be able to understand your code if you use good variable names and your logic is clear. In cases where the logic is unclear or convoluted, a code comment is warranted to explain your implementation.

## Docstrings

In Python, we document modules (`.py` files), classes, and functions with [docstrings](https://peps.python.org/pep-0257/). Docstrings are part of the Python language syntax. 

IDEs like PyCharm and Visual Studio Code look for docstrings to provide information about a module, class, or function:

{{< figure src="popup.png" alt="An info popup showing function information" width="800">}}


### Creating docstrings for a module/file or a class

On the first line of the file, put something similar to the following:

`"""This module contains functions useful for counting birds."""`

That's it. You can add multi-line docstrings where needed like so:
```python{linenos=true}
"""
This module contains functions to load a bird observation file and count it.

It is used by the ornithologist package to load data for further processing.
"""
```

You do the same thing for classes. Provide a short summary just below the class name:

```python{linenos=true}
class Patient:
    """An object representing a Patient's vital information."""

    def __init__(self, name: str, age: int, weight: float, height: float):
        # More code here
```


### Creating docstrings for a function
Place a blank line below the function name and type `"""`. PyCharm will prepare a template for you.

```python
    def __init__(self, name: str, age: int, height: float, weight: float):
        """

        :param name:
        :param age:
        :param height:
        :param weight:
        """
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
```

PyCharm's docstring template understands the following:
- A blank area at the beginning to explain the purpose of the function. 
- (If present) `:param <name>` for you to describe purpose of each parameter if you have them. 
- (If present): `:return:` for you to describe what your function returns, if anything.
- (If present): `:raises <ErrorType>:` Where you can manually enter the various Exceptions your function might raise.

Fill in the contents like so.
```python
    def __init__(self, name, age, weight, height):
        """
        Class constructor.
        :param name: the patient's full name
        :param age: age in whole years
        :param height: height in inches
        :param weight: weight in pounds
        """
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
```

Now with your docstrings set up, you will see helpful pop-ups in your IDE when you type class and function names!

{{< figure src="constructor_popup.png" alt="Another info popup showing function information" width="400">}}

## Knowledge check
- When are the two cases where an in-line comment is appropriate?
- In Python, why is `sum` a bad variable name?
- Why is `doc()` a bad function name?
- For which *three* Python program elements do you write docstrings?
- What are the four possible elements of a *function* docstring?
- Does the docstring go inside or above the program element?
- Exercise: Fill in the docstring for the `compute_risk()` function.
- Exercise: Write a function called `calculate_area()` that takes a `list` of numbers as its only parameter. If there are three elements in the list, compute and return the area of a triangle (assume it is a right triangle). If there are two elements, return the area of a rectangle. Otherwise, raise a `ValueError`.
    - Enforce all coding conventions.
    - Provide the type hints for the function's parameters and return value.
    - Create a docstring containing a summary, all `param:` values, and a `raises:` value.
 
