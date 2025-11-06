---
title: Avoid magic literals
weight: 10
description: Best practices for organizing functionality.
---

## Class recording

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/7CLCNIzjtPo?si=C-XwSMmjOuAjKwnh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## What is a “magic literal”?

A ***magic literal*** is a raw value (number, string, `None`, etc.) that appears in code **without a name explaining its meaning or origin.** They harm readability, hide intent, and make changes risky—because the same value might be duplicated in many places.

**Rule of thumb:** If a value has domain meaning (tax rate, role name, error code, feature flag, file path, regex, etc.), name it once and reuse that name everywhere.

**Benefits**
- Clear intent (self-documenting)
- Single source of truth (change in one place)
- Fewer bugs during refactors
- Easier testing & configuration

## Example 1 - numeric literal

### Problematic code


```python
def final_price(subtotal):
    # Why 0.085? City tax? Promo? Future me has no idea.
    return subtotal * (1 + 0.085)
```

**Problem:** Where does the value `0.085` come from? Why is it there? Not knowing this harms maintainability. 

### Fixed with a constant that conveys intent
Constants are variables that don't vary. They are set once and not changed. In Python, the convention is to name Python constants as ALL_UPPERCASE_AND_UNDERSCORES.

```python
CITY_SALES_TAX_RATE = 0.085  # 8.5% city sales tax

def final_price(subtotal: float) -> float:
    return subtotal * (1 + CITY_SALES_TAX_RATE)
```

**Why this is better**: The constant gives the number meaning, centralizes the value, and invites documentation and tests around that concept. Keep constants close to where they’re used (module-level), or in a dedicated `constants.py` if shared broadly.

## Example 2 - String literals

### Problematic code

```python
def get_discount(category):
    if category == "student":
        return 0.10
    elif category == "veteran":
        return 0.15
    elif category == "employee":
        return 0.20
    else:
        return 0.0

```
Again, the meaning of each string is hidden. *Typos* ("vetran") will silently break the logic. And, finally, if category labels change, you must update multiple places.

### Fixed using named constants
```python
CATEGORY_STUDENT = "student"
CATEGORY_VETERAN = "veteran"
CATEGORY_EMPLOYEE = "employee"

DISCOUNT_STUDENT = 0.10
DISCOUNT_VETERAN = 0.15
DISCOUNT_EMPLOYEE = 0.20
DISCOUNT_DEFAULT = 0.0

def get_discount(category):
    if category == CATEGORY_STUDENT:
        return DISCOUNT_STUDENT
    elif category == CATEGORY_VETERAN:
        return DISCOUNT_VETERAN
    elif category == CATEGORY_EMPLOYEE:
        return DISCOUNT_EMPLOYEE
    else:
        return DISCOUNT_DEFAULT
```

The constants clearly express intent and centralize both string values and their corresponding numeric meanings. If a new category or discount rate is added, it only needs to be defined once.

For larger systems, consider moving these constants to a separate `constants.py` module to avoid duplication across files.

## When a literal is not magic

- **Sentinel/obvious values**: `0`, `1`, `-1`, `True`, `False`, `""` used in generic math or indexing (e.g., `arr[-1]`) are usually fine.
- **Short-lived throwaway code/tests:** Inline values in extremely small, clear scopes can be acceptable.
- **Data structure examples:** Literals inside illustrative examples or test fixtures are usually okay unless they are likely to change.

## Knowledge Check
- Question: Why are magic literals risky in larger code bases?
    <details><summary>Answer</summary>Because you need to update the literal values everywhere they appear in code if the value needs to change.</details>
- Question: Which of the following is *least likely* to be a magic literal?
    1. `"admin"`
    2. `0.075`
    3. `arr[-1]`
    4. `"https://api.example.com/v1"`
    <details><summary>Answer</summary>3 — Sentinel and language-specific values like 0, 1, True, False, and -1 are not considered magic literals. In Python, <code>arr[-1]</code> is a shortcut to get the last element of a list.</details>
- Question: Spot and fix the magic literal(s):
    ```python
    def greet_user(role):
        if role == "admin":
            print("Welcome back, administrator!")
        elif role == "guest":
            print("Hello, guest user.")
        else:
            print("Access restricted.")
    ```
    <details><summary>Answer</summary>The <code>"admin"</code> and <code>"guest"</code> strings are magic literals. The messages themselves are probably not magic literals since they are likely used only once. However, if your app had internationalization where it supports multiple languages, you would replace those messages with variables.</details>
- Question: True or False: It’s acceptable to use a literal directly in code when its meaning is obvious and universally understood, such as `0` in `range(0, 10)` or True in a simple condition.
    <details><summary>Answer</summary>This is True, similar to the answer of Question 2.</details>


## Next up
Up next is the [SRP principle](../srp/).