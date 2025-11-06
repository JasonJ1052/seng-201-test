---
title: DRY and the Rule of Three
weight: 20
description: Functions should have a single, simple goal.
---

## Class recording

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/gLTJaDcHmLI?si=fZclBQogzPYamovp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Rule #3: DRY — Don’t Repeat Yourself (and the Rule of Three)

Don't Repeat Yourself! Commonly called the DRY rule, it simply means don't write the same code in multiple places.

Why not? Because when you must fix or update the logic, you have to do it **everywhere** it’s copied—this multiplies effort and risk of bugs.

The **Rule of Three** is helpful to identify when DRY is being violated. If the same (or nearly the same) code shows up in *three or more places*, extract it into a function (or module). Two copies feels suspicious, but three is definitely an indicator to refactor.

If the copies differ slightly, *find the part that varies* and *control that via a parameter*. 

**Benefits**

- One place to fix or improve.
- Fewer missed patches and inconsistent behaviors.
- Less surface area to understand/review.
- Better-named functions document intent.

## Example 1 — Obvious repetition → function

### Problematic code
```python
# apply discounts in three places
total_a = subtotal_a - (subtotal_a * 0.10)  # 10% off
taxed_a = total_a * 1.07

total_b = subtotal_b - (subtotal_b * 0.10)  # 10% off
taxed_b = total_b * 1.07

total_c = subtotal_c - (subtotal_c * 0.10)  # 10% off
taxed_c = total_c * 1.07
```

The only thing that changes here is the variable acted upon. This is a clear call for a function. There are also magic literals here.


### Better code (extract once)

```python
# Note the use of default parameters below. These should 
DEFAULT_DISCOUNT = 0.10
DEFAULT_TAX_RATE = 0.07

def apply_discount_and_tax(subtotal, discount=DEFAULT_DISCOUNT, tax_rate=DEFAULT_TAX_RATE):
    discounted = subtotal * (1 - discount)
    return discounted * (1 + tax_rate)

taxed_a = apply_discount_and_tax(subtotal_a)
taxed_b = apply_discount_and_tax(subtotal_b)
taxed_c = apply_discount_and_tax(subtotal_c)
```

Now we have one function and the repeated code is gone. Even better, that function is now flexible by taking the discount amount and tax rate as parameters. We also cleaned up magic literals!

## Example 2 - Hidden duplication (structure, not lines)

### Problematic code
```python
def send_welcome_email(user):
    msg = f"Welcome {user.name}!"
    smtp = SMTP("smtp.example.com")
    smtp.send(user.email, msg)
    smtp.close()

def send_password_reset_email(user, token):
    msg = f"Reset link: https://x/reset/{token}"
    smtp = SMTP("smtp.example.com")
    smtp.send(user.email, msg)
    smtp.close()
```

Duplication isn’t always copy-paste; sometimes two blocks share a shape. Do you see the similarities and differences? We should refactor the common elements into a reusable helper function, and then create additional functions to provide the specifics to that helper (this will help with SRP too)!

### Better code (extract shared steps)
```python
SMTP_SERVER = "smtp.example.com"

def send_email(user, msg):
    smtp = SMTP(SMTP_SERVER)
    try:
        smtp.send(user.email, msg)
    finally:
        smtp.close()

def send_welcome_email(user):
    send_email(user, f"Welcome {user.name}!")

def send_password_reset_email(user, token):
    send_email(user, f"Reset link: https://x/reset/{token}")

```

We extracted the common logic of sending the SMTP mail but parameterized the message. Now the `send_welcome_email` and `send_password_reset_email` use the helper.

## Common Pitfalls
- **Parameter bloat.** Too many knobs can make the function unclear. If it grows unwieldy, split into cohesive variants or use a small strategy object.
- **Premature abstraction.** Don’t over-abstract on the first duplication. Two copies are a smell, the third justifies the refactor.
- **Duplicating data transformations.** Push conversions (e.g., parsing, formatting) to the boundaries. Write functions that work with one canonical representation internally, and make other functions for dealing with particular formats (like in Example 2).


## Knowledge Check
- What’s the best trigger to refactor for DRY?
    1. The very first time code is written.
    2. When you see two copies anywhere.
    3. When substantially the same code appears three or more times.
    4. Only when performance suffers.
        <details><summary>Answer</summary> C — Use the **Rule of Three** as a practical trigger (two is a smell, three is a must). </details>
- You find three similar blocks differing only in a constant (e.g., a rate). What’s the cleanest DRY fix?
    1. Copy the block and change the constant.
    2. Extract a function and make the constant a parameter.
    3. Add three separate functions.
    4. Inline everything into one giant function.
        <details><summary>Answer</summary> B — Extract and parameterize the variation. </details>
- Two blocks share setup/teardown but build different messages. Best approach?
    1. Leave as is; they’re “not identical.”
    2. Extract just the setup/teardown into a helper and pass the message (or a small builder) as the parameter.
    3. Merge both into one if/else ladder in-place.
    4. Use copy-paste with a TODO.
        <details><summary>Answer</summary> B — Extract the shared structure; parameterize the varying message. </details>
- Your new helper now takes 7 parameters and is hard to read. What next?
    1. Add more parameters.
    2. Revert to duplication.
    3. Split the helper along cohesive responsibilities.
    4. Ignore it.
        <details><summary>Answer</summary> C — Avoid parameter bloat by grouping or splitting to maintain cohesion. </details>

## Next up
Up next is [handling exceptions at the lowest sensible level](../except-lowlvl/).