---
title: Control Flow Graphs
weight: 18
math: true
description: A simple but powerful analysis technique for understanding execution paths through source code.
---

## Class video
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/sypa49qL6FI?si=FCETklCTCowaD9Is" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Setup
1. Download both [`cfg_examples.py`](cfg_examples.py) and [`test_cfg_examples.py`](test_cfg_examples.py). Place them in your `testing-lab/` directory.

## Motivation
In the previous lab, we briefly mentioned that your tests need to exercise the [program's different behaviors](../organizing/#your-testing-strategy). 

One approach to systematically exercise the behavior of the system is through ***basis path testing***: identify all ***program paths*** in the code and make sure we have at least one test case that exercises every path.

How do we identify all program paths? That is exactly what the ***control flow graph*** helps us to do. These graphs can help us to understand what our code does, and also gives us a powerful analysis tool for designing ***test cases*** as well as many other applications in computer science.

## Definition and uses
A ***control-flow graph (CFG)*** is a representation of *all* program paths that might be traversed through a program during its execution. A ***program path*** is a sequence of execution steps like we learned about in [debugging](../debugging/).

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/b/bd/Rust_MIR_CFG.svg" width="256" alt="An example control flow graph from the Rust project">}}
<small><a href="https://commons.wikimedia.org/wiki/File:Rust_MIR_CFG.svg">The Rust Project Developers</a> (<a href="http://www.apache.org/licenses/LICENSE-2.0">Apache License 2.0</a> or <a href="http://opensource.org/licenses/mit-license.php">MIT</a>), via Wikimedia Commons</small>

[Frances (Fran) Allen](https://en.wikipedia.org/wiki/Frances_Allen) was an IBM Fellow who devised the concept of control flow graphs in the 1960s. In 2006, she became the first woman to receive the Turing Award for her contributions to computer science.

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/1/15/Allen_mg_2528-3750K-b.jpg" alt="Photograph of Fran Allen" width="256">}}
<small><a href="https://commons.wikimedia.org/wiki/File:Allen_mg_2528-3750K-b.jpg">Rama</a>, <a href="https://creativecommons.org/licenses/by-sa/2.0/fr/deed.en">CC BY-SA 2.0 FR</a>, via Wikimedia Commons</small>

### Formal definition
(Credit to [David Liu and Mario Badr](https://www.cs.toronto.edu/~david/course-notes/csc110-111/17-graphs/08-control-flow-graphs.html) for this section's content).

Control flow graphs represent different blocks of code. A ***basic block*** is a sequence of non-compound statements and expressions in a program's code that are guaranteed to execute together, one after the other.

Here are some examples and non-examples of basic blocks:
```python
# A single statement is a basic block.
x = 1

# A sequence of multiple statements and function calls is a basic block.
x = 5
y = x + 2
z = f(x, y)
print(x + y + z)

# A basic block can end with a return or raise statement.
x = 5
y = x + 2
return f(x, y)

# But a sequence of statements with a return/raise in the middle is
# NOT a basic block, since the statements after the return/raise aren't
# going to execute.
x = 5
return x
y = x + 2  # Will never execute!

# An if statement is not a basic block, since it is a compound statement.
# The statements it contains aren't guaranteed to execute one after the other.
if x > 5:
    y = 3
else:
    y = 4
```

Typically we treat basic blocks as being maximal, i.e., as large as possible. So if we have a sequence of assignment statements (`x = 5`, `y = x + 2`, etc.), we treat them as one big block rather than consisting of multiple single-statement blocks.

Now let’s look at that if statement example in more detail. We can divide it up into three basic blocks: one for the condition (`x > 5`), then one for the if branch (`y = 3`) and one for the else branch (`y = 4`). We can now formalize this idea, and extend it to other kinds of control flow statements like loop.

Formally, a ***control flow graph (CFG) of a program*** is a graph \\(G = (V,E)\\) where:
- \\(V\\) is the set of all (maximal) basic blocks in the program code, plus one special element represent the \\(end\\) of a program.
- \\(E\\) is the set of edges, where:
  - There is an edge from block \\(b_1\\) to block \\(b_2\\) if and only if the code in \\(b_2\\) can be executed immediately after the code in \\(b_1\\).
  - There is an edge from block \\(b\\) to the special \\(end\\) block if and only if the the program can stop immediately after executing the code in block \\(b\\). This occurs if there is no code written after \\(b\\), or if \\(b\\) ends in a `return` or `raise` statement.



## Building a CFG

Here are the rules:
1. When you draw a node, you will write either the actual statements or the line numbers inside the rectangle.
2. ***Decision nodes***: Draw as a diamond or a highlighted rectangle. These are blocks that either (a) transfer control by performing a `function_call()`, or (b) make a decision with `if-else`, `try-except` `for`, or `while`. You do not create a decision nodes for built-in functions like `print()` or `input()`. A `try-except` block is a decision node on the `try`; the `except` blocks are regular nodes (usually).
3. ***Regular nodes***: Draw as a rectangle. These are blocks code that executes *in sequence **without** jumping*. You group multiple lines of code together into one regular node when they execute in sequence.
4. ***End node***: Draw two concentric circles with the inner one filled-in. This represents the "end" of the control flow that you are modeling. It *does not* represent a line of code. 

5. ***Edges***: Draw a line with an arrow at the end to represent the control flow passing from one node to another. 
   - Regular nodes will have a single *incoming* edge and a single *outgoing* edge indicating program control flows in and out of the code block.
   - Decision nodes will have a single *incoming* edge. They will have either two *outgoing* edges in the case of `if-else`, `for`, and `while` statements or one *outgoing* edge if a `function_call()` that activates a new function. **Label** the outgoing edge(s) of the decision node with the function_call() or the condition, e.g., `x < 0` or `x >= 0`.
   - For `try` nodes, you have a single incoming edge. You have one outgoing edge to the internal nodes of the `try`, and one outgoing edge to each `except` and `finally` block.
   - The end node can have many *incoming* edges, and will have *no* outgoing edges.


We can model a CFG for an entire program, a selected block, or individual functions. CFGs can get lengthy quickly, so you are best off working with separate, small functions. 

## Example

Let's start with a simple code snippet:
```python{linenos=true}
def check_number(x):
    if x > 0:
        return "Positive"
    else:
        return "Non-positive"
```

1. We will use line 1 `def check_number(x):` as our start point. It is a **regular node** because no decision is made. Draw a rectangle at the top of a sheet of paper. Write ether the line number or the entire line of code inside the node. 
   {{< figure src="IMG_7038.JPG" alt="CFG Example - step 1" width="256">}}

2. Below the first node, draw a diamond or highlighted rectangle box to represent a **decision node** for line 2. Decision nodes are used when you encounter `if-else`, `for`, or `while` loops or a call to a user-defined `function()`. Draw an **edge** connecting the first node to the second.
   {{< figure src="IMG_7039.JPG" alt="CFG Example - step 2" width="256">}}

4. Draw a **regular node** for line 3 as a rectangle next to the line 2 node. Regular nodes represent blocks of code (in this case only one line) that executes *in sequence* with no decisions or calls to other functions. Draw an **edge** from line 2 to line 3 and label it with the condition that transfers control to line 3.
   {{< figure src="IMG_7043.JPG" alt="CFG Example - step 3" width="256">}}
5. Draw another **regular node** representing line 5 below the line 2 node. Draw an **edge** from line 2 to 5 and label it with the condition that transfers control to line 5.
   {{< figure src="IMG_7044.JPG" alt="CFG Example - step 4" width="256">}}
   Note that we DO NOT draw a node for the `else` on line 4. It is a part of the `if` decision node on line 2. However, if we have `if-elif`, we would draw another decision node. We are just capturing the `if` comparisons in our graph.
7. Finally, we need an ***end node*** to indicate the end of the program paths. Draw two concentric circles below the other nodes. Connect lines 3 and 5 to this end node. This node does not represent a line of code, but indicates the end of the execution we care about.  
      {{< figure src="IMG_7047.JPG" alt="CFG Example - step 5" width="256">}}

Now we have a CFG for a very simple block of code. Tracing the execution of the program becomes a matter of tracing your pen through the nodes and, when you reach decision nodes, determining how the variables values determine the flow of control. 


## Identifying unique program paths

One of the most important uses of a CFG is that it enables us to identify all the **unique program paths** in the code. Again, a ***program path*** is a sequence of execution steps like we learned about in [debugging](../debugging/). 



**Question**: Can how many unique program paths are indicated by the CFG? What are they?

To answer this question, you trace the set of nodes executed during a single "run" of the code block. A **path** is the set of nodes executed. Note that we have a decision node (line 2). So when the program executes, we have to choose a path, either going through 3 or 5 because the program makes a choice based on the value of `x`. 

So the answer, then, is there are two unique **program paths**:
1. The path (1,2,3)
2. The path (1,2,5)

Now, in ***basis path testing*** we will write test code (assertions) with values that exercise *all paths* at a minimum. So for the above simple example:
```python
def test_check_number():
    assert examples.check_number(5) == "Positive"  # tests path (1,2,3)
    assert examples.check_number(-1) == "Non-Positive"  # tests path (1,2,5)
```

Why do we care about the unique program paths? Because we can measure *how good* our unit tests are based on the number of unique program paths covered. So, our goal becomes to **design our test cases** so that the set of tests hits every unique program path. Sometimes this is easier said than done.  **Test coverage** is a measure of how many program paths are covered by a test of test cases, and test coverage is used throughout the industry as a measure of test *quality*. We will use a tool to calculate the test coverage in a future lab.

## Exercise: Multiple return paths

The following example has multiple ways to return out of the code block. You would treat raising an exception as returning.

```python{linenos=true}
def classify_number(x):
    if x < 0:
        return "Negative"
    elif x == 0:
        return "Zero"
    else:
        return "Positive"
```
Try to draw the CFG for this example. Some pointers:
- Lines 2 and 4 are both decision nodes.
- `return` statements are treated as regular nodes, but they all go to the end node.
- Make sure to label your decision nodes' outgoing edges with the condition.



## Exercise: Loop example

Consider the following code that includes a loop.

```python{linenos=true}
def process_numbers(nums):
    evens = 0
    odds = 0
    for num in nums:
        if num % 2 == 0:
            print(f"{num} is even")
            evens += 1
        else:
            print(f"{num} is odd")
            odds += 1
    return evens, odds
```

Try to draw the CFG for this example. Some pointers:
- A loop is a decision node. In the case of this `for` loop, if there are still `num` remaining in the list, you go to 3. Otherwise, the program block is *ended* because there is nothing left after the for loop.
- Where do you go after lines 4 and 6? Back to the `for` loop.




## Knowledge Check
- Question: What is a program path, and how is a CFG related to program paths?
- Question: What do you label the *outgoing* edges of a decision node with?
- Question: How many unique program paths exist in the [Loop example](#exercise-loop-example)? What are they?
- Question: Write one or more test cases that exercise all unique paths in the [Loop example](#exercise-loop-example).
- Question: How many unique program paths exist in the [Multiple return paths example](#exercise-multiple-return-paths)? What are they?
- Question: Write a test case that exercises all the unique program paths the [Multiple return paths example](#exercise-multiple-return-paths)? What are they?
- Question: We didn't model an exception scenario. Apply your critical thinking and the rules at the top of this lab to create a CFG for the following function:
```python{linenos=true}
def analyze_data(data):
    evens = 0
    odds = 0
    for item in data:
        if isinstance(item, int):
            if item % 2 == 0:
                evens += 1
            else:
                odds += 1
        else: 
            raise ValueError("Invalid data type")
    return evens, odds
```
