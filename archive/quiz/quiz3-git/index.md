---
title: Quiz 3 - Design Rules and Version Control
weight: 20
description: Study guide for Quiz 3
---


## In class November 19

- Study <u>***key terms***</u> from slides and labs.
- Study your notes, the examples, and the slides (Weeks 7-9 on Canvas) about the [Low-Level Design Rules](https://llayman.github.io/seng-201/labs/design/). You will be asked to critique code for design rule violations.
- Study Knowledge Checks from all the [Version Control labs](../../labs/version-control/).
  - [Git basics](../../labs/version-control/git-concepts/#knowledge-check)
  - [Undoing mistakes with Git](../../labs/version-control/git-undo/#knowledge-check)
  - [Branching and Merging](../../labs/version-control/git-branching/#knowledge-check)
  - [Merge Conflicts](../../labs/version-control/merge-conflicts/#knowledge-check)
  - Remote repos
    - [Sharing a new project](../../labs/version-control/remote/new-project/#knowledge-check)
    - [`git push`](../../labs/version-control/remote/push/#knowledge-check)
    - [Clone an existing project](../../labs/version-control/remote/clone-existing/#knowledge-check)
    - [Retrieving changes](../../labs/version-control/remote/pull/#knowledge-check)
- Sample questions for examining a Git Repo's state or critiquing code for design rule violations are provided below.
- You may use your own ***written*** notes during the quiz.
- Multiple choice, fill-in-the-blank, long answer.

## Sample Git Repo state questions

### Git analysis - sample 1
Consider the following depictions of a Git repository's state:

**Repo state**
{{<figure src="../../labs/version-control/git-branching/feature-1-v3-repo.jpg">}}

**Conceptual branch history**
{{<figure src="../../labs/version-control/git-branching/feature-1-v3-concept.jpg">}}

1. What is the current *active branch*?
2. How many versions will running the command `git log` show?
3. How many versions will running the command `git log` show after running `git checkout main`?
4. Suppose the following changes and commands are made *in order*:
   1. `git checkout main`
   2. Add some lines to `app.py`.
   3. `git add .`
   4. `git commit -m "added new functions"`
   Update both the Repo state diagram and the Conceptual branch history diagram to reflect the changes. 

{{< details "Solution for Git sample 1">}}
1. The current active branch is `feature-1`, as indicated by the `HEAD`
2. `git log` runs in the active branch by default, and `feature-1` has 3 versions.
3. `git log` in the `main` branch will shown only the first version.
4. 
{{<figure src="quiz3-question-repo.jpg" alt="Repo state diagram after adding the new version to main" width="600">}}
{{<figure src="quiz3-question-concept.jpg" alt="Branch history diagram after adding the new version to main" width="400">}}
{{< /details >}}

### Git analysis - sample 2

{{<figure src="../../labs/version-control/git-undo/hello-staged.jpg">}}
Consider the repo state above as **the starting point for each question**. Briefly explain the impact of running the following commands in terms of the versions, head, and the workspace files.
   1. `git reset .`
   2. `git reset --hard HEAD`.
   3. `git reset --hard HEAD~1`.



{{< details "Solution for Git sample 2">}}
1. The changes to `main.py` and `hello.py` will be unstaged (removed from the Index), but will still be present in the workspace.
2. We discard any changes since the most recent version:
   - All changes will be unstaged. 
   - `main.py` will be replaced with its version from `b424cc`. 
   - `hello.py` will be as-is in the workspace because it is *untracked*, meaning it has not yet been added to version control. You can tell that `hello.py` is untracked because it does not exist in any version. Running `git status` would tell you that it is untracked.
   - The `HEAD` will continue to point to version `b424cc`.
3. All tracked files in the workspace and the local repository are reset to version `8356ea`. Essentially, we are resetting to the point *before* the most recent version.
   - `README.md` will be removed from the workspace.
   - `main.py` will be replaced with its version from `8356ea`. 
   - Version `b424cc` will be deleted from the Local Repository.
   - `hello.py` will be as-is in the workspace because it is *untracked*.
   - The `HEAD` will now point to version `8356ea`.
{{< /details >}}




## Sample low-level design rule questions

### Design critique - sample 1
Consider this simple Python program:
```python{linenos=true}
def process_order(product, quantity):
    if product == "apple":
        price = 1.0
    elif product == "banana":
        price = 0.5
    else:
        price = 2.0

    if quantity > 0:
        total_cost = price * quantity
        print(f"The total cost for {quantity} {product}(s) is ${total_cost}")
    else:
        print("Quantity must be positive")
```
Identify which of the 6 low-level design rules this program violates and why. Suggest how these violations might be addressed.

{{< details "Solution for Sample 1">}}
You could potentially argue for other design rule violations, or a violation in rule of the ones below. In my mind, the rules below are clearly violated.


1. Violation of "Separate input/output logic from business logic":
    - **Issue**: The function `process_order` mixes calculating the total cost with printing output directly to the console.
    - **Solution**: Separate the calculation logic into a distinct function and handle input/output operations elsewhere.
2. Violation of "Avoid magic literals":
    - **Issue**: The prices 1.0, 0.5, and 2.0 are hardcoded directly into the function, making them "magic" numbers without context.
    - **Solution**: Use named constants for these values. They could be placed into a dictionary, for example.
3. Violation of "Handle errors at the lowest sensible level, and re-raise/re-throw them otherwise":
    - **Issue**: The function checks for positive quantities but does not raise a specific error.
    - **Solution**: Use exception handling to raise a specific error when quantity is non-positive.
{{< /details >}} 

### Design critique - sample 2

Consider this Python code:
```python{linenos=true}
class OrderProcessor:
    def __init__(self):
        self.orders = []

    def add_order(self, product, quantity, price):
        self.orders.append({"product": product, "quantity": quantity, "price": price})

    def remove_order(self, product):
        for order in self.orders:
            if order["product"] == product:
                self.orders.remove(order)
                print(f"Order for {product} removed.")
                return
        print(f"No order found for {product}.")

    def process_orders(self):
        total_cost = 0
        for order in self.orders:
            total = order["quantity"] * order["price"]
            total_cost += total
            print(f"Processing order for {order['quantity']} {order['product']}(s) at ${order['price']} each. Total: ${total}")
        print(f"Total cost of all orders: ${total_cost}")

    def print_summary(self):
        print("Order Summary:")
        for order in self.orders:
            total = order["quantity"] * order["price"]
            print(f"{order['quantity']} {order['product']}(s) - ${order['price']} each - Total: ${total}")

    def find_order(self, product):
        for order in self.orders:
            if order["product"] == product:
                total = order["quantity"] * order["price"]
                print(f"Found order: {order['quantity']} {order['product']}(s) at ${order['price']} each. Total: ${total}")
                return
        print(f"No order found for {product}.")

    def update_order(self, product, new_quantity, new_price):
        for order in self.orders:
            if order["product"] == product:
                order["quantity"] = new_quantity
                order["price"] = new_price
                total = new_quantity * new_price
                print(f"Updated order for {product}: {new_quantity} units at ${new_price} each. New total: ${total}")
                return
        print(f"No order found for {product}.")
```

{{< details "Solution for sample 2">}}
You could potentially argue for other design rule violations, or a violation in rule of the ones below. In my mind, the rules below are clearly violated.

1. Violation of "Single Responsibility Rule":
    - **Issue**: The OrderProcessor class handles multiple responsibilities: it maintains the list of orders, processes them, and prints order summaries.
    - **Solution**: Split responsibilities into dedicated classes, such as `OrderManager` for managing orders, `OrderProcessor` for processing, etc.
2. Violation of "DRY (Don't Repeat Yourself)":
    - **Issue**: The calculation `total = order["quantity"] * order["price"]` is repeated across multiple methods (`process_orders`, `print_summary`, `find_order`, and `update_order`).
    - **Solution**: Create a helper method to calculate the total for a given order to avoid repeating this logic.
3. Violation of "Avoid Magic Literals":
    - **Issue**: The product-related attributes such as "product", "quantity", and "price" are string literals used throughout the class. If any of these strings are mistyped, or if there is a change in the attribute names, the program may fail without easy traceability.
    - **Solution**: Use constants or, better yet, use a dedicated Order class with attributes for product, quantity, and price to encapsulate these values.
4. Violation of "Handle errors at the lowest sensible level, and re-raise/re-throw them otherwise":
    - **Issue**: When removing or updating orders, the methods simply print messages if the order is not found rather than handling the error in a structured manner (e.g., raising an exception or returning an error code).
    - **Solution**: Raise specific exceptions like OrderNotFoundError if an order is not found, and allow higher-level methods to decide how to handle them.
5. Violation of "Raise specific errors and define custom errors if needed":
    - **Issue**: No custom error handling is used for operations that could logically fail (e.g., removing or finding non-existent orders). The use of print statements for error messages is not a robust approach.
    - **Solution**: Define custom exceptions such as OrderNotFoundError or InvalidOrderError to handle various conditions gracefully.
{{< /details >}}
