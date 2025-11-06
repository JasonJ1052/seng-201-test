---
title: Handle Errors at the Lowest Sensible Level
weight: 25
description: Handle errors where they can be meaningfully addressed; otherwise, re-raise them.
---

## Handle Errors at the Lowest Sensible Level

The rule ***Handle errors at the lowest sensible level, and re-raise/re-throw them otherwise*** means that you should catch and handle exceptions where you can meaningfully address them, and let them propagate upward when you cannot.

**What is sensible?** Do not gobble up errors just to hide problems. Catch and fix them if you can, otherwise, raise the error and let the calling function deal with it.

**What does it mean to meaningfully address or fix an error?** A function can meaningfully address an error when it has the context and capability to either resolve the issue or convert it into a recoverable state. For example, a function that reads user input can handle a `ValueError` by prompting for valid input again, or a network function can retry a failed connection. However, if a function encounters an error it cannot resolve (like a missing configuration file that the function doesn't have permission to create, or a badly-formatted input file  in a function that only processes data), it should re-raise the exception so a higher-level function with more context can handle it appropriately. The key is: if you can fix it or work around it meaningfully at your level, do so; otherwise, let it propagate.

**Benefits**
- Functions become more robust and clearly defined: "I handle these situations, but not these."
- Error-handling logic is simplified because you only handle what you can fix.
- Errors are not hidden; they propagate to where they can be properly addressed.
- The user interface layer is responsible for displaying error messages, keeping business logic separate from presentation.

**Red flags (violations):** 
- Functions that catch all exceptions and silently return `None` or default values, hiding real problems.
- Catching exceptions at too high a level when they could be handled more specifically at a lower level.
- Swallowing exceptions with empty `except:` blocks or `except: pass`.
- Functions that catch exceptions only to re-raise them without adding context or handling.
- Mixing error handling with business logic instead of handling errors where they occur.
- Displaying error messages or logging from deep within business logic functions.

## Example 1 - Swallowing errors to hide problems

### Problematic code

```python
def read_config_file(filename: str) -> dict:
    try:
        config = {}
        with open(filename, 'r') as f:
            for line in f:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    config[key] = value
        return config
    except:
        return {}  # Silently fails, caller doesn't know what went wrong

def process_user_data(config: dict) -> list:
    users = []
    for user_id in config.get("user_ids", []):
        try:
            user = fetch_user_from_database(user_id)
            users.append(user)
        except:
            pass  # Silently skips users, no indication of failure
    return users
```

**Problem:** These functions swallow errors, hiding real problems. The caller has no way to know if the config file was missing, corrupted, or if the database call failed. Errors are hidden rather than being handled or propagated.

### Fixed to handle or re-raise appropriately

```python
def read_config_file(filename: str) -> dict:
    try:
        config = {}
        with open(filename, 'r') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' not in line:
                    raise ValueError(f"Invalid format in {filename} at line {line_num}: missing '='")
                key, value = line.split('=', 1)
                config[key.strip()] = value.strip()
        return config
    except FileNotFoundError:
        # Can't handle this at this level - file missing is a real problem
        raise
    except ValueError as e:
        # Could provide more context, but still re-raise
        raise ValueError(f"Invalid config format in {filename}: {e}") from e

def process_user_data(config: dict) -> list:
    users = []
    failed_ids = []
    for user_id in config.get("user_ids", []):
        try:
            user = fetch_user_from_database(user_id)
            users.append(user)
        except ConnectionError:
            # Network error - can't fix here, but we can track it
            failed_ids.append(user_id)
        except ValueError as e:
            # Invalid user ID format - can't fix here
            raise ValueError(f"Invalid user_id {user_id}: {e}") from e
    
    if failed_ids:
        # Re-raise with context about what failed
        raise ConnectionError(f"Failed to fetch users: {failed_ids}")
    return users
```

**Why this is better**: Errors are either handled meaningfully (with context added) or re-raised so callers can decide how to respond. No errors are silently swallowed.

## Example 2 - Handling errors at too high a level

### Problematic code

```python
def process_order(order_data: dict) -> bool:
    try:
        # All errors handled at top level
        validate_order(order_data)
        calculate_total(order_data)
        charge_card(order_data)
        send_confirmation(order_data)
        return True
    except Exception as e:
        print(f"Error: {e}")  # UI concern in business logic!
        return False
```

**Problem:** All errors are caught at the top level, mixing UI concerns (printing) with business logic. The function can't distinguish between different types of errors, and the caller gets no information about what went wrong. Different errors might need different handling.

### Fixed by handling at appropriate levels

```python
def validate_order(order_data: dict) -> None:
    if "items" not in order_data or len(order_data["items"]) == 0:
        raise ValueError("Order must contain at least one item")
    if "card_number" not in order_data:
        raise ValueError("Card number is required")
    # Validation errors are handled here, but they're fixable at input level

def calculate_total(order_data: dict) -> float:
    total = 0.0
    for item in order_data["items"]:
        if "price" not in item or "quantity" not in item:
            raise ValueError(f"Invalid item data: {item}")
        total += item["price"] * item["quantity"]
    return total
    # Calculation errors handled here - data problems are fixable

def charge_card(order_data: dict, amount: float) -> None:
    try:
        # Payment gateway call
        payment_api.charge(order_data["card_number"], amount)
    except payment_api.InsufficientFundsError as e:
        # Can't fix this here, but we communicate what happened
        raise ValueError("Insufficient funds to complete the transaction") from e
    except payment_api.InvalidCardError as e:
        # Can't fix this here either
        raise ValueError(f"Payment failed: {e}") from e
    # Network errors, etc. - let them propagate

def process_order(order_data: dict) -> None:
    # There are no try-except blocks in this function, so it re-raises errors by default. Let the caller handle them. 
    validate_order(order_data)
    total = calculate_total(order_data)
    charge_card(order_data, total)
    # Only send confirmation if everything succeeded
    send_confirmation(order_data)
```

**Why this is better**: Each function handles errors it can meaningfully address (validation, calculation) and re-raises errors it cannot fix (payment failures, network issues). The UI layer can then catch these and display appropriate messages to the user.

## How to apply this rule

1. **Handle what you can fix.** If you can meaningfully recover from an error at a specific level, handle it there.
2. **Re-raise what you can't.** If you can't fix the problem, re-raise the exception (possibly with added context) so a caller can handle it.
3. **Don't swallow errors.** Never use bare `except:` or `except: pass` unless you're at the absolute top level (like a main event loop).
4. **Add context when re-raising.** Use exception chaining (`raise ... from e`) to preserve the original error while adding useful context.
5. **Keep UI concerns separate.** Displaying error messages or re-prompting the user to enter "good" input are the UI layer's responsibilities, not the business logic layer's.
6. **Handle at the lowest level.** If a low-level function can fix a specific error (e.g., retry a network call), handle it there rather than letting it bubble up unnecessarily.



## Knowledge Check
- A function that reads user input encounters a `ValueError` when parsing a number. The function can prompt the user to re-enter valid input. What should this function do?
    1. Catch the exception and return `None` to indicate failure
    2. Catch the exception, prompt the user for valid input, and retry the operation
    3. Let the exception propagate to the caller without handling it
    4. Catch the exception and print an error message to the console
    <details><summary>Answer</summary>2 — since the function can meaningfully address the error by prompting for valid input, it should handle it at this level rather than propagating it upward.</details>
- You're writing a function that processes data from a configuration file. The function encounters a `FileNotFoundError` but doesn't have permission to create files. What should it do?
    1. Catch the exception and return an empty dictionary as a default
    2. Catch the exception and print "File not found" to the console
    3. Re-raise the exception (possibly with added context) so a higher-level function can handle it
    4. Use `except: pass` to silently ignore the error
    <details><summary>Answer</summary>3 — since the function cannot meaningfully fix this error (it can't create the missing file), it should re-raise the exception so a caller with more context (like the UI layer) can handle it appropriately.</details>
- When re-raising an exception with added context, what is the best practice?
    1. Use `raise ValueError("New message")` to replace the original exception completely
    2. Use `raise ValueError("New message") from e` to preserve the original exception chain
    3. Only re-raise the original exception without any modifications
    4. Catch and log the exception, then return `None`
    <details><summary>Answer</summary>2 — using `raise ... from e` preserves the original exception chain, which helps with debugging by showing both the original error and the added context.</details>
- Which of the following is a red flag that violates the "lowest sensible level" principle?
    1. A validation function that raises `ValueError` when input is invalid
    2. A payment processing function that catches `InsufficientFundsError` and re-raises it as `ValueError` with a user-friendly message
    3. A data processing function that catches all exceptions and returns an empty list
    4. A function that lets network exceptions propagate to the caller when it can't retry the connection
    <details><summary>Answer</summary>3 — catching all exceptions and returning a default value (like an empty list) hides errors and prevents callers from knowing what went wrong. This violates the principle by swallowing errors that should be handled or propagated.</details>

## Next up
Up next is our final rule: [raise specific errors and define your own if needed.
](../except-specific)