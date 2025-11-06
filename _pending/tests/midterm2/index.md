---
title: Midterm Exam 2
weight: 25
description: Study guide and sample long-form problems for the second midterm exam
---



## Exam Format and Rules
- The exam is **in class**, Wednesday, April 2.
- A mix of multiple choice, fill-in-the-blank, and long answer questions.
- You will not be programming in PyCharm, but you may be asked to write or edit code snippets by hand.
- You may bring ***1 double-sided sheet of letter paper*** with your own ***hand-written*** notes. 
- Honor Code violations on the any exam result in a course grade of F.
- Failure to submit an exam results in a course grade of F.

## Content
- Study ***key terms*** from slides and labs. Look for <u><b>boldfaced, underlined terms</b></u> in slides and ***emphasized terms*** in labs.
- Study ***Knowledge Checks*** from labs.
- Code Conventions and Documentation: Week 8 on Canvas + [Labs](../../labs/style-and-documentation/).
   - Write a valid Python docstring for a provided function including the essential elements: description, parameters, return values, and exceptions. Syntax need not be perfect but needs to be very close.
   - Identify and correct violations of PEP8 coding conventions in provided Python code. Emphasis will be on naming conventions and whitespace within lines.
   - Given a Python function, be prepared to add type hints to function parameters and return values.
- 6 Low-level program design rules: (Weeks 9-10 + accompanying [Lab](../../labs/design/))
   - Be prepared to define and explain the importance of *understandability*, *maintainability*, *efficiency*, and *robustness*. These are the attributes a good design promotes.
   - Be prepared to define the 6 rules and explain them.
   - Be prepared to analyze a given block of Python code and identify design rule violations.
   - Be prepared to *fix* a block of Python code that violates a design rule.
- The follow topics from earlier in the semester are also on the table:
   - Describing the phases of the Software Lifecycle (week 3).
   - Testing concepts (terms) and application (weeks 5-6), including:
      - Writing or analyzing [unit tests](../../labs/testing/) for a given function
      - `assert` statements
      - computing line coverage by hand
      - testing if exceptions are raised using `pytest` functions


## Sample design problems

### Design sample problem 1

```python{linenos=true}
def process_order(order_amount):
    if order_amount < 0:
        raise Exception("Bad value!")

    if order_amount > 1000:
        shipping = 25
    else:
        shipping = 10
    
    tax = order_amount * 0.07
    return order_amount + shipping + tax
```
1. Identify which design rules are violated.
   {{< details "Answer">}}
   - `0.07`, `1000`, `25`, and `10` are magic literals, violating Rule #1: Avoid magic literals.
   - A generic Exception is raised without specifying what was wrong, violating Rule #6: Raise specific errors and define your own if needed.
   {{< /details >}}
1. Modify the code to bring it into compliance with the design rules.
   {{< details "Answer">}}
   - Assign the literals to "constant" variables, and use the variables in the computations, e.g., `SHIPPING_THRESHOLD = 1000`. Then later: `if order_amount > SHIPPING_THRESHOLD:`
   - Alternately, you could transform the literal values into function parameters, e.g., `def process_order(order_amount: float, shipping_threshold: int, low_ship: int, high_ship: int, tax_rate: float):`
   - Raise a more specific exception type with a better message, like `raise ValueError('order amount must be greater than 0')`. You could also define a custom error class and raise it.
   {{< /details >}}

```python{linenos=true}
def create_user_profile():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    
    with open("profiles.txt", "a") as file:  # append to the file.
        file.write(f"{name},{age}\n")
    
    print("Profile saved.")
```
1. Identify which design rules are violated.
   {{< details "Answer">}}
   - This function violates Rule #1: Avoid magic literals. The string literal `profiles.txt` is hardcoded.
   - This function performs input gathering, data formatting, file writing, and output display all at once. This is a violation of Rule #2: Functions should have a single responsibility.
   - This function also violates Rule #4: Separate input/output logic from business logic.
   - You could also make some argument that the function is violating Rule #5 by not handling errors at the lowest sensible level. Since the user interface is included in this code, it would be reasonable to check that you are able to append to the file.
   {{< /details >}}
1. Modify the code to bring it into compliance with the design rules.
   {{< details "Answer">}}
   - Make the filename to write to into a function parameter.
   - You should separate the code into at least two functions: a user interface and a function to write the data. Or, you could do three functions: one for input, one to write the data, and one to produce output. 
   - If you want to make the code more robust, you can add some error handling and retry for a FileNotFoundError.
   - Note: There is one more input error that can occur. Can you spot it? How would you handle it?
   ```python{linenos=true}
   def save_user_profile(name: str, age: int, filename: str):
       with open(filepath, "a") as file:  # open() will raise a FileNotFoundError if filepath doesn't exist.
           file.write(f"{name},{age}\n")

   def create_user_profile():
       name = input("Enter your name: ")
       age = int(input("Enter your age: "))

       filename = ''
       while filename == '':  # you could also say while not filename:
           try:
               filename = input("Enter the filename to append to: ")
               save_user_profile(name, age, filename)
           except FileNotFoundError:
               print("Could not find that file. Try again.")
    
       print("Profile saved.")
   ```
   {{< /details >}}


### Design sample problem 2

```python{linenos=true}
def process_order(order_amount):
    if order_amount < 0:
        raise Exception("Bad value!")

    if order_amount > 1000:
        shipping = 25
    else:
        shipping = 10
    
    tax = order_amount * 0.07
    return order_amount + shipping + tax
```
1. Identify which design rules are violated.
   {{< details "Answer">}}
   - `0.07`, `1000`, `25`, and `10` are magic literals, violating Rule #1: Avoid magic literals.
   - A generic Exception is raised without specifying what was wrong, violating Rule #6: Raise specific errors and define your own if needed.
   {{< /details >}}
1. Modify the code to bring it into compliance with the design rules.
   {{< details "Answer">}}
   - Assign the literals to "constant" variables, and use the variables in the computations, e.g., `SHIPPING_THRESHOLD = 1000`. Then later: `if order_amount > SHIPPING_THRESHOLD:`
   - Alternately, you could transform the literal values into function parameters, e.g., `def process_order(order_amount: float, shipping_threshold: int, low_ship: int, high_ship: int, tax_rate: float):`
   - Raise a more specific exception type with a better message, like `raise ValueError('order amount must be greater than 0')`. You could also define a custom error class and raise it.
   {{< /details >}}

### Design sample problem 3

```python{linenos=true}
def apply_clearance_discount(price: float) -> float:
    if price >= 100:
        discount = price * 0.40
    else:
        discount = price * 0.60
    return price - discount


def apply_loyalty_discount(price: float) -> float:
    if price >= 100:
        discount = price * 0.20
    else:
        discount = price * 0.10
    return price - discount


def run_discount_menu():
    while True:
        print("\n--- Discount Menu ---")
        print("1. Clearance Discount")
        print("2. Loyalty Discount")
        print("3. Exit")
        choice = input("Choose a discount type (1-3): ")

        if choice == "3":
            print("Goodbye!")
            break

        try:
            price = float(input("Enter the original price: $"))
        except ValueError:
            print("Invalid price. Please enter a number.")
            continue

        if choice == "1":
            final = apply_clearance_discount(price)
            print(f"Applying Clearance discount. Final price: ${final:.2f}")
        elif choice == "2":
            final = apply_loyalty_discount(price)
            print(f"Applying Loyalty discount. Final price: ${final:.2f}")
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    run_discount_menu()
```
1. Identify which design rules are violated.
   {{< details "Answer">}}
   - Again we violate Rule #1: Avoid magic literals. `100` and all the float values are magic literals.
   - Of course, there are many other string literals in the user prompts and user output messages. We generally ignore these as magic literals, until you care about internationalization (i18n) and accessibility (a11y) in production systems.
   - This code clearly violates Rule #3: Don't repeat yourself (DRY) as the functions `apply_clearance_discount` and `apply_loyalty_discount` are nearly identical.
   - You could make the argument that `run_discount_menu` is doing too much between showing the menu, getting user input, and displaying user output, possibly violating Rule #2: Functions should have a single responsibility. I think you could argue either way.
   {{< /details >}}
1. Modify the code to bring it into compliance with the design rules.
   {{< details "Answer">}}
   - In this case, we should provide "constant" variables for the literals in our calculation to solve #1.
   - To fix Rule #3, we should combine the two `discount` functions and parameterize the parts that vary.

   ```python{linenos=true}
    def apply_discount(price: float, discount_threshold: int, above_discount: float, below_discount: float) -> float:
        if price >= discount_threshold:
            discount = price * above_discount
        else:
            discount = price * below_discount
        return price - discount


    DISCOUNT_THRESHOLD = 100
    CLEARANCE_ABOVE = 0.4
    CLEARANCE_BELOW = 0.6
    LOYALTY_ABOVE = 0.2
    LOYALTY_BELOW = 0.1

    def run_discount_menu():
       while True:
          print("\n--- Discount Menu ---")
          print("1. Clearance Discount")
          print("2. Loyalty Discount")
          print("3. Exit")
          choice = input("Choose a discount type (1-3): ")

          if choice == "3":
              print("Goodbye!")
              break

          try:
              price = float(input("Enter the original price: $"))
          except ValueError:
              print("Invalid price. Please enter a number.")
              continue

          if choice == "1":
              final = apply_discount(price, DISCOUNT_THRESHOLD, CLEARANCE_ABOVE, CLEARANCE_BELOW)
              print(f"Applying Clearance discount. Final price: ${final:.2f}")
          elif choice == "2":
              final = apply_discount(price, DISCOUNT_THRESHOLD, LOYALTY_ABOVE, LOYALTY_BELOW)
              print(f"Applying Loyalty discount. Final price: ${final:.2f}")
          else:
              print("Invalid option. Try again.")

    if __name__ == "__main__":
        run_discount_menu()
   ```
   {{< /details >}}

## Sample Testing problems

These sample problems are the same as from Midterm 1. I will not ask you to write Control Flow Graphs for this exam, however, you may benefit from creating them to ensure you test all paths.


### Testing Sample Problem 1
```python{linenos=true}
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
```
1. List the unique program paths.
3. Add `assert` statements to the following test case that exercise all unique program paths.
   ```python
   def test_is_prime():
      # Your code here.
   ```

#### Solution


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

### Testing Sample Problem 2
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

1. List the unique program paths.
3. Add `assert` statements to the following test case that exercise all unique program paths.
   ```python
   def test_generate_fibonacci():
      # Your code here.
   ```


#### Solution


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


### Testing Sample Problem 3
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
1. List the unique program paths.
3. Add `assert` statements to the following test case that exercise all unique program paths.
   ```python
   def test_factorial():
      # Your code here.
   ```

#### Solution


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