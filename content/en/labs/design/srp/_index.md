---
title: Single Responsibility Principle
weight: 15
description: Functions should have a single, simple goal.
---

## Class recording

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Q_4zr0SVhxE?si=wbMUc0sC2Mw-Ee1C" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## The Single Responsibility Principle

The ***Single Responsibility Principle*** is that functions should have a single responsibility—i.e., they should be cohesive. Group together into a function statements and logic that have a single, simple goal.

The Single Responsibility Principle is often stated as "each function has one clear reason to change." 


**Benefits**
- Each function has a clear purpose and answers one “what does this do?” question.
- Narrow behaviors are easier to unit test.
- A change to that single purpose only affects one function rather than requiring changes across unrelated code.
- Small, focused functions are easier to compose to solve bigger problems.

**Red flags (violations):** 
- The function name needs “and” to describe it.
- It touches multiple domains (I/O, parsing, business rules, UI) at once.
- It has many parameters or returns mixed/compound results that signal different concerns.
- It has multiple try/except blocks for different activities.
- It both decides and acts (e.g., computes a result and prints/saves/sends it).

## Example 1 - Decision logic mixed with formatting
### Problematic code


```python
def describe_temperature(celsius: float) -> str:
    if celsius < 0:
        color = "blue"
        label = "Freezing"
    elif celsius < 20:
        color = "green"
        label = "Cool"
    else:
        color = "red"
        label = "Hot"

    # Mixing presentation logic here
    return f"{label} ({celsius}°C) shown in {color.upper()}"
```

**Problem:** This function both *categorizes* a temperature and *formats* a human-readable message. If we change color conventions or output format, unrelated logic breaks.

### Fixed to separate out unrelated purposes

```python
def classify_temperature(celsius: float) -> str:
    if celsius < 0:
        return "Freezing"
    elif celsius < 20:
        return "Cool"
    return "Hot"

def color_for_temperature(label: str) -> str:
    return {"Freezing": "blue", "Cool": "green", "Hot": "red"}[label]

def format_temperature_message(label: str, celsius: float, color: str) -> str:
    return f"{label} ({celsius}°C) shown in {color.upper()}"

def describe_temperature(celsius: float) -> str:
    label = classify_temperature(celsius)
    color = color_for_temperature(label)
    return format_temperature_message(label, celsius, color)
```

**Why this is better**: Each helper has a single reason to change — classification rules, color mapping, or formatting.

## Example 2 - Data validation mixed with transformation

### Problematic code

```python
def normalize_user_input(data: dict) -> dict:
    if "name" not in data or "email" not in data:
        raise ValueError("Missing fields")

    data["name"] = data["name"].strip().title()
    data["email"] = data["email"].lower()

    return data
```
Validation and transformation responsibilities are blended. Changing validation rules would risk altering transformation behavior.

### Fixed by splitting the function
```python
def validate_user_input(data: dict) -> None:
    if "name" not in data or "email" not in data:
        raise ValueError("Missing fields")

def normalize_user_fields(data: dict) -> dict:
    return {
        "name": data["name"].strip().title(),
        "email": data["email"].lower(),
    }

def process_user_input(data: dict) -> dict:
    validate_user_input(data)
    return normalize_user_fields(data)
```

Each function has one clear reason to change — validation rules vs. formatting rules.

## How to refactor toward SRP

1. **Name first.** Write a function name that states a single outcome; split if you need “and.”
1. **Separate concerns.** Isolate I/O, parsing, validation, business rules, formatting, and presentation.
1. **Extract functions.** Pull distinct blocks into helpers with clear inputs/outputs.
1. **Push side effects outward.** Keep core logic pure; print/save at the edges.



## Knowledge Check
- Which function best follows SRP?
    1. `process_and_save_and_print_order()`
    2. `compute_total(items, tax_rate)`
    3. `read_validate_compute()`
    4. `do_everything()`
    <details><summary>Answer</summary>2 — the names of the others all imply that they have multiple responsibilities.</details>
- A common SRP smell is:
    1. One return statement
    2. Short parameter list
    3. A function that both validates input and writes files
    4. A pure function with docstring
    <details><summary>Answer</summary>3 — Validating input (from a user, from a file) and writing data to a file are distinct responsibilities within a program.</details>
- A good SRP-based refactor typically involves:
    1. Extracting cohesive operations into new functions.
    2. Reducing the number of function calls.
    3. Merging similar code into a single larger function.
    4. Avoiding helper functions.
    <details><summary>Answer</summary>1 — refactoring an SRP problem almost always will result in more functions in the program.</details>
- The SRP is violated when a function changes for more than one reason. “Reason” here refers to:
    1. Multiple developers editing the same code.
    2. Multiple sources of change tied to distinct responsibilities.
    3. The number of commits per week.
    4. The number of test cases.
    <details><summary>Answer</summary>2 — thinking of "responsibility" as "one task the program performs", if something about that task changes (e.g., getting input, validating input is correct, writing output) it should ideally only affect one function in the code that is separate from the other tasks.</details>

## Next up
Up next is the [DRY principle and the Rule of Three](../dry/).