---
title: Raise Specific Errors and Define Your Own If Needed
weight: 30
description: Use precise exception types to indicate error causes clearly; create custom exceptions when built-in ones don't fit.
---

## Raise Specific Errors and Define Your Own If Needed

The rule ***Raise specific errors and define your own if needed*** means that you should use the most appropriate exception type for each error situation, choosing from built-in exceptions when they fit, and creating custom exception classes when they don't.

**Why specific errors?** Specific exceptions precisely indicate what went wrong, making code more maintainable. When you catch a `ValueError`, you know the problem is with the value of the data. When you catch a `FileNotFoundError`, you know a file is missing. Generic exceptions like `Exception` or bare `except:` clauses hide the actual problem, making debugging and error handling much more difficult.

**Built-in exceptions to use:** Python provides many [specific exception types](https://docs.python.org/3/library/exceptions.html). Choose the most appropriate one:
- `ValueError` - often the most appropriate when called with "bad" data (wrong value, invalid format)
- `TypeError` - for unsupported types of data (wrong type passed to function)
- `FileNotFoundError` - when a file or directory cannot be found
- `PermissionError` - when an operation is not permitted due to insufficient permissions
- `KeyError` - when a dictionary key is missing
- `IndexError` - when a sequence index is out of range
- `AttributeError` - when an attribute (variable or function) doesn't exist on the object, e.g., calling `x.append('Bob')` but `x` is a dictionary. Dictionaries don't understand how to `append()` in Python.
- And many more specific exceptions for different scenarios

**When to create custom exceptions:** When built-in exceptions don't accurately represent your domain-specific errors, create your own exception classes. Custom exceptions make it clear that an error is specific to your application's domain, not a general programming error. For example, if you're building a payment system, a `PaymentProcessingError` or `InsufficientFundsError` is more meaningful than a generic `ValueError`.

**Benefits**
- Precise error identification: callers can catch specific exceptions and handle them appropriately
- Better maintainability: developers can quickly understand what went wrong
- Improved debugging: specific error types make it easier to locate and fix issues
- Clearer code intent: the exception type itself documents what can go wrong
- Enables selective error handling: callers can catch only the exceptions they know how to handle

**Red flags (violations):** 
- Raising generic `Exception` instead of specific exception types
- Using `ValueError` for everything, even when `TypeError` or other exceptions are more appropriate
- Catching all exceptions with bare `except:` or `except Exception:` without distinguishing types
<!-- - Not creating custom exceptions when built-in ones don't accurately represent the error -->
- Using string error messages instead of exceptions when an exception is more appropriate
- Creating custom exceptions that don't add meaningful information beyond built-in exceptions

## Example 1 - Using generic Exception instead of specific exceptions

### Problematic code

```python
def validate_age(age):
    if age < 0:
        raise Exception("Age cannot be negative")
    if not isinstance(age, int):
        raise Exception("Age must be an integer")
    return age

def process_user_data(user_id):
    try:
        user = fetch_user_from_database(user_id)
        return user
    except Exception:
        return None  # Caller doesn't know what went wrong
```

**Problem:** These functions use generic `Exception` instead of specific exceptions. Callers can't distinguish between different error types, making it impossible to handle specific errors appropriately. For example, a caller can't tell if `read_config_file` failed because the file was missing (`FileNotFoundError`) or because of a permission issue (`PermissionError`), so they can't respond appropriately.

### Fixed using specific exceptions

```python
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    if age < 0:
        raise ValueError(f"Age cannot be negative, got {age}")
    return age

def process_user_data(user_id):
    try:
        user = fetch_user_from_database(user_id)
        return user
    except ConnectionError:
        # Network issue - caller might want to retry
        raise ConnectionError("Could not connect to database.") from e
    except ValueError as e:
        # Invalid user ID format - different from network error
        raise ValueError(f"Invalid user_id format: {user_id}") from e
```

**Why this is better**: Specific exceptions allow callers to handle different error types appropriately. For example, a caller can catch `FileNotFoundError` to prompt for a different file, or catch `PermissionError` to display a permission-related message. The exception type itself communicates what went wrong.

## Example 2 - Creating custom exceptions for domain-specific errors

### Problematic code

```python
def process_payment(card_number: str, amount: float) -> bool:
    if not card_number or len(card_number) < 13:
        raise ValueError("Invalid card number")
    
    if amount <= 0:
        raise ValueError("Amount must be positive")
    
    if amount > 10000:
        raise ValueError("Amount exceeds daily limit")
    
    # Check if card is expired
    if is_card_expired(card_number):
        raise ValueError("Card is expired")
    
    # Check if insufficient funds
    balance = get_account_balance(card_number)
    if balance < amount:
        raise ValueError("Insufficient funds")
    
    # Process payment
    return True
```

**Problem:** All errors raise `ValueError`, even though they represent fundamentally different problems. A caller can't distinguish between "invalid card format", "card expired", "insufficient funds", and "amount exceeds limit" - all are treated as generic value errors. This makes it difficult to handle different payment errors appropriately (e.g., retry for insufficient funds vs. reject for expired card). You could inspect the error message, but that would be using a magic literal.

### Fixed by creating custom exceptions

```python
# Define custom exceptions for payment domain
class PaymentError(Exception):
    """Base exception for payment-related errors"""
    pass

class InvalidCardError(PaymentError):
    """Raised when card number format is invalid"""
    pass

class CardExpiredError(PaymentError):
    """Raised when card has expired"""
    pass

class InsufficientFundsError(PaymentError):
    """Raised when account has insufficient funds"""
    pass

class AmountExceedsLimitError(PaymentError):
    """Raised when payment amount exceeds allowed limit"""
    pass

def process_payment(card_number: str, amount: float) -> bool:
    if not card_number or len(card_number) < 13:
        raise InvalidCardError(f"Invalid card number format: {card_number}")
    
    if amount <= 0:
        raise ValueError("Amount must be positive")  # Still ValueError - general validation
    
    if amount > 10000:
        raise AmountExceedsLimitError(f"Amount {amount} exceeds daily limit of 10000")
    
    # Check if card is expired
    if is_card_expired(card_number):
        raise CardExpiredError("Card has expired")
    
    # Check if insufficient funds
    balance = get_account_balance(card_number)
    if balance < amount:
        raise InsufficientFundsError(f"Insufficient funds: balance {balance}, required {amount}")
    
    # Process payment
    return True

# Caller can now handle specific errors appropriately
def handle_payment_request(card_number: str, amount: float):
    try:
        process_payment(card_number, amount)
        print("Payment successful!")
    except CardExpiredError:
        print("Your card has expired. Please use a different card.")
    except InsufficientFundsError:
        print("Insufficient funds. Please try a smaller amount.")
    except AmountExceedsLimitError:
        print("Payment amount exceeds daily limit. Please contact support.")
    except InvalidCardError:
        print("Invalid card number. Please check and try again.")
    except PaymentError:
        # Catch any other payment-related errors
        print("Payment processing failed. Please try again later.")
```

**Why this is better**: Custom exceptions clearly communicate domain-specific errors. Callers can catch specific exceptions (`InsufficientFundsError`, `CardExpiredError`) and handle them appropriately, or catch the base `PaymentError` to handle any payment-related error. The exception hierarchy also allows for selective handling: catch `PaymentError` for all payment issues, or catch specific subclasses for granular control.

## How to apply this rule

1. **Choose the most appropriate built-in exception.** When raising an error, use the most specific built-in exception that accurately describes the problem:
   - Use `ValueError` for invalid values or data formats
   - Use `TypeError` for wrong types
   - Use `FileNotFoundError` for missing files
   - Use `PermissionError` for permission issues
   - Use `KeyError` for missing dictionary keys
   - Use `IndexError` for out-of-range indices
   - And so on...

2. **Create custom exceptions when built-in ones don't fit.** When your error is domain-specific and doesn't match any built-in exception, create your own:
   ```python
   class DataProcessError(Exception):
       pass
   ```
   Create a hierarchy if needed:
   ```python
   class PaymentError(Exception):
       pass
   class InsufficientFundsError(PaymentError):
       pass
   ```

3. **Don't use generic `Exception`.** Avoid raising `Exception` directly - it's too generic and doesn't help callers handle errors appropriately.

4. **Don't misuse `ValueError` for everything.** While `ValueError` is common, don't use it when `TypeError`, `FileNotFoundError`, or other exceptions are more appropriate.

5. **Catch specific exceptions when possible.** When catching exceptions, catch specific types rather than generic `Exception`:
   ```python
   try:
       process_data()
   except FileNotFoundError:
       # Handle missing file
   except ValueError:
       # Handle invalid data
   ```

6. **Use exception hierarchies for domain errors.** Create a base exception class for your domain, then subclass it for specific cases. This allows callers to catch either specific errors or all domain errors:
   ```python
   try:
       process_payment()
   except InsufficientFundsError:
       # Handle specific case
   except PaymentError:
       # Handle any payment error
   ```



## Knowledge Check
- You're writing a function that validates user input. The function receives a string when it expects an integer. What exception should you raise?
    1. `Exception("Expected integer")`
    2. `ValueError("Expected integer")`
    3. `TypeError("Expected integer")`
    4. `AttributeError("Expected integer")`
    <details><summary>Answer</summary>3 — <code>TypeError`</code> is the most appropriate exception for when the wrong type is passed to a function. <code>ValueError</code> would be for an integer with an invalid value (like a negative age), not for the wrong type entirely.</details>
- Your function reads a configuration file, but the file doesn't exist. What exception should you raise?
    1. `ValueError("File not found")`
    2. `FileNotFoundError("config.txt")`
    3. `Exception("File missing")`
    4. `KeyError("config.txt")`
    <details><summary>Answer</summary>2 — <code>FileNotFoundError</code> is the specific built-in exception for missing files. It's more precise than `ValueError` or generic `Exception`, and allows callers to handle file-not-found errors specifically.</details>
- You're building a payment processing system and need to indicate when a payment fails due to insufficient funds. The built-in exceptions don't accurately represent this domain-specific error. What should you do?
    1. Raise `ValueError("Insufficient funds")` since it's a value problem
    2. Create a custom exception class like `class InsufficientFundsError(Exception)`
    3. Raise `Exception("Payment failed")` to be generic
    4. Return `False` instead of raising an exception
    <details><summary>Answer</summary>2 — when built-in exceptions don't accurately represent your domain-specific errors, create custom exception classes. This makes the error type clear and allows callers to catch and handle <code>InsufficientFundsError</code> specifically, which is more meaningful than a generic <code>ValueError</code>.</details>
- Which of the following is a red flag that violates the "raise specific errors" principle?
    1. Using `TypeError` when a function receives the wrong type
    2. Creating a custom `DataProcessError` exception for data processing failures
    3. Raising `Exception` for all errors instead of specific exception types
    4. Using `FileNotFoundError` when a file is missing
    <details><summary>Answer</summary>3 — raising generic <code>Exception</code> for all errors violates the principle because it doesn't help callers distinguish between different error types. Specific exceptions like <code>ValueError</code>, <code>TypeError</code>, <code>FileNotFoundError</code>, or custom exceptions allow for precise error handling.</details>

