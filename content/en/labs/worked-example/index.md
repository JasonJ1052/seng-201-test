---
title: 07. Comprehensive example 
weight: 25
description: A working example of that touches every topic so far.
---

We have covered quite a bit. Let's go through an example from problem statement to implementation to test using what we've learned so far.

## Class recording
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/8ed1NgBFECw?si=F8eWhCBzPFO6fntM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Setup
1. Create a new project directory named `comp-example/` or something similar. Open that directory using PyCharm as usual.

2. Download each of the sample input files below and place them in the project directory:
    - [birds_small.txt](birds_small.txt)
    - [birds_large.txt](birds_large.txt)
    - [birds_empty.txt](birds_empty.txt)
    - [bad.txt](bad.txt)
    - [problem_statement.txt](problem_statement.txt)


## Problem Description

We'll start with this high-level description of the problem:

>You are tasked with writing a program that can read in a text file where each line has the name of a species of bird. Your program needs to count the number of times each species appears. An example of the input is below. Ask the user to type in the name of the file they wish to be processed.
> ```
> White-eared Hummingbird
> Townsend's Solitaire
> Townsend's Solitaire
> Yellow-fronted Canary
> Chestnut-fronted Macaw
> ```
> Your program must handle any text file in this format.

<!-- ## Crafting a problem statement 
An ounce of planning is worth a pound of programming.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/LcdEywgLFaA?si=pVkX12Or-ig_gssU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe> -->


## Implementation

We'll start by doing the simplest thing that meets the requirements of the problem description. 


<!-- <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/5PiApbBOfuM?si=FuRsm9Jtx-w1ceDe" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe> -->


<!-- ## Testing
Time to test using `pytest` using what we learned from the [pytest lab](../testing/pytest/) and [testing for exceptions](../testing/test-exceptions/).

### Reworking the code to be testable
We cannot test our code as it. We need to reorganize for testability. User interface code is difficult to unit test.


<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Zy5hhs92Oeg?si=eY9y6VyCiNDXLYaW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe> -->

## Writing pytest code
Finally time to test. When you write test cases and assertions, you are checking the ***actual*** computed result against the ***expected*** result for a ***given input***.

<!-- <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ahv9zZM9Ado?si=kNM1y7FMd9gcexQ6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>  -->
<!-- 
## Recap
We went from high level problem description, to problem statement, to an initial implementation, to reorganizing our code to be testable, to finally writing our tests.

You need to become comfortable with all these steps!

Ending files:
- [`problem_statement.txt`](problem_statement.txt)
- [`birds_counter.py` - first attempt](birds_counter_first_attempt.py)
- [`birds_counter.py` - after rework](birds_counter.py)
- [`test_birds_counter.py`](test_birds_counter.py) -->

 <!-- ## Setup for WSL Users
 You will follow this process for every project on WSL from now on.

 1. Open PyCharm and select the `File` menu, then `Close Project`.
1. Select `WSL` on the left, then the `+` button to create a new project. Do this even if you already have a `testing-lab/` directory.
1. Select the `...` button to pick the Projcet directory. 
1. Pick your Ubuntu instance at the top, then navigate to `home/<your_id>/seng-201/` and create a new folder (icon at the top) for `comp-example/`. 
1. Select the new directory and hit `OK`.   
1. Click `Start IDE and Connect` on the screen. PyCharm will take a minute to finish configuring. It should open a new window with a `main.py` file showing some boilerplate code.
1. Select the `File` menu, then `Settings`.
1. Select `Project: comp-example` in the left pane, then click the `Python Interpreter` link.
1. Select the `Add Interpreter` link near the top right, then `Add Local Interpreter`. 
1. Leave the default options selected and hit `OK`. If you see a red error message, contact the instructor.
1. `OK` out of the settings screen.
1. Finally, open a ***new*** Terminal within PyCharm. Type `which pip`. You should see something like 
    - `/home/<your_id>/seng-201/comp-example/.venv/bin/pip`, or;
    - `/home/<your_id>/virtualenvs/comp-example/bin/pip`
    - but ***not*** `/usr/bin/python`
7. **You will run all subsequent Terminal commands from the integrated Terminal in PyCharm.**
1. run the following in the integrated Terminal:
    ```bash
    pip install pytest pytest-cov
    ```
1. Complete the setup instructions at the [top of this lab](#setup). -->
