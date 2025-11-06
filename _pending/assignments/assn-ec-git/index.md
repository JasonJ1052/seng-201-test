---
title: Extra Credit Assignment - More Git/GitHub Flow
weight: 45
description: More practice with Git and GitHub
---

## Instructions
This is an **individual assignment**. You may not collaborate. 

I will not grade incomplete Extra Credit, so you must complete all steps below at a minimum. You may earn partial extra credit if something is incorrect.

You may find it useful to refer to Scenario 1 of the [lab on remote repos](../../labs/version-control/remote/).

1. Make a new **public** GitHub repository.
2. Create a new Python project with the file `math_ops.py` containing the following:
    ```Python
    # math_operations.py

    def divide_numbers(a, b):
        """Divides two numbers and returns the result."""
        return a / b  # Potential division by zero error

    if __name__ == "__main__":
        x = 10
        y = 0
        result = divide_numbers(x, y)
        print(f"The result of division is: {result}")
    ```
3. Connect your project to your GitHub repository. Add, commit, and push the first version to the `main` branch.
4. Create two branches off the first version: `bug-fix` and `new-feature`.
5. In `bug-fix`: make it so that an attempt to call `divide_numbers` with a 0 in the denominator results in a nice message printed to the screen saying "Cannot divide by 0" rather than throwing an exception.
    - Commit and push your changes to the `bug-fix` branch.
6. In `new-feature`: add a function of your choice to the program and call it from the main block. 
   - Commit and push your changes to the `new-feature` branch.
7. Merge `bug-fix` into `main` first.
8. Merge `new-feature` into `main` second. Follow the Git Flow.
9. Ensure that `main` correctly incorporates both branches and push it to your remote repository.

## Rubric
- 15pts total:
  - All branches are created, committed to, and pushed as specified above. 
  - Functionality is implemented as specified above.
  - Feature branches are merged into main following the Git Flow, and merged functionality works correctly in `main`.

## Final submission due Sunday, Nov 17
Two items:
1. Push all your branches and finished code to GitHub.
2. Enter the URL to your public GitHub repository containing the assignment on the [Canvas assignment page](https://uncw.instructure.com/courses/83039/assignments/1255027).