---
title: Assignment 3 - Information Literacy
weight: 15
description: Putting your information literacy skills to the test.
---

## Accompanying video

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/-as1vM6Iv2E?si=L7BSmFJOBNYV0Xzf" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Objectives
- Write effective Internet search queries and use official documentation to research answers.
- Examine and compare information from various sources to evaluate its accuracy, authority, currency, and relevance.
- Properly cite and apply the researched information to help solve software engineering problems.

## Overview
Software engineers constantly use the Internet to learn how to achieve functionality and to help debug errors. 

You will find plenty of *wrong* or misleading answers on the Internet. Who has time for that? You need to be able to discern between good sources from time wasters.


## Instructions

Download and complete [`assignment_3.docx`](./assignment_3.docx). Complete it with a partner in class and submit to Canvas.


### Code for Task 1

Run the following Python code. You will get an error and stack trace:

```python{linenos=true}
def calculate_cart_total(cart_items, tax_rate):
    """Calculate total cart cost including tax."""
    subtotal = sum(item["price"] * item["quantity"] for item in cart_items)
    return subtotal + (subtotal * tax_rate)

def display_cart_summary(cart_items, tax_rate):
    """Display a summary of the cart."""
    total_cost = calculate_cart_total(cart_items, tax_rate)
    print(f"Total cost (including tax): ${total_cost:.2f}")

def main():
    """Main function to simulate a shopping cart."""
    cart = [
        {"name": "Laptop", "price": 1000.0, "quantity": 1.0},
        {"name": "Headphones", "price": 200.0, "quantity": 2.0},
        {"name": "Mouse", "price": 50.0, "quantity": 1.0},
        {"name": "Keyboard", "price": 150.0, "quantity": 1.0},
        {"name": "Monitor", "price": 300.0, "quantity": 1.0},
        {"name": "HDMI Cable", "price": 10.0, "quantity": 2.0},
        {"name": "USB Drive", "price": "20.0", "quantity": 3.0},
        {"name": "External Hard Drive", "price": 100.0, "quantity": 1.0},
    ]
    tax_rate = 0.07  # 7% sales tax
    display_cart_summary(cart, tax_rate)

if __name__ == "__main__":
    main()
```

## Submission due Friday Sep 26 @ 11:59pm via Canvas
Upload your completed `assignment_3.docx` to the [Canvas assignment page](https://uncw.instructure.com/courses/99267/assignments/1398307).

