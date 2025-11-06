---
title: pytest
description: Use a test framework, pytest, to run tests and collect results.
weight: 20
---
<!-- 
## <mark>Updated instructions for WSL users only</mark>
This lab uses Python virtual environments. Apparently, PyCharm requires much configuration to synchronize with Python virtual environments on WSL. Open an Ubuntu terminal and run:
```bash
sudo apt update -y && sudo apt upgrade -y
sudo apt install python3-pip python3-venv
```

Follow the instructions below. Here is a video of the process.

   <video controls playsinline width="800">
   <source src="wsl-pycharm-small.mp4" type="video/mp4">  
   </video>

1. Open an Ubuntu terminal and run:
    ```bash
    sudo apt update -y && sudo apt upgrade -y
    sudo apt install python3-pip python3-venv
    ```
1. Open PyCharm and select the `File` menu, then `Close Project`.
1. Select `WSL` on the left, then the `+` button to create a new project. Do this even if you already have a `testing-lab/` directory.
1. Select the `...` button to pick the Projcet directory. 
1. Pick your Ubuntu instance at the top, then navigate to `home/<your_id>/seng-201/` and create a new folder (icon at the top) for `testing-lab/`. If you have `testing-lab/`, create a new `testing-lab2/` directory. Select the new directory and hit `OK`.
    {{<figure src="pycharm-wsl-project.png" width="400">}}
1. Click `Start IDE and Connect` on the screen. PyCharm will take a minute to finish configuring. It should open a new window with a `main.py` file showing some boilerplate code.
1. Select the `File` menu, then `Settings`.
1. Select `Project: testing-lab` in the left pane, then click the `Python Interpreter` link.
1. Select the `Add Interpreter` link near the top right, then `Add Local Interpreter`. 
1. Leave the default options selected and hit `OK`. If you see a red error message, contact the instructor.
1. `OK` out of the settings screen.
1. Finally, open a ***new*** Terminal within PyCharm. Type `which pip`. You should see something like 
    - `/home/<your_id>/seng-201/testing-lab/.venv/bin/pip`, or;
    - `/home/<your_id>/virtualenvs/testing-lab/bin/pip`
    - but ***not*** `/usr/bin/python`
7. **You will run all subsequent Terminal commands from the integrated Terminal in PyCharm.**

WSL users are now ready to move on. -->


    
## Test frameworks
We developed [organized](../organizing/), [thorough](../cfg/) unit tests in in previous labs.. Our test code is looking good, but we still need to address two issues for it to be truly useful:
1. We would like to know if multiple test cases are failing.
2. We would like to collect our test results in a human-friendly format. 

***Automated test frameworks*** address these find and execute test code (often through naming conventions like `test_*`), capture assertion exceptions (test case failures), and generate summaries of which tests pass and fail.

Automated test frameworks are an integral part of modern software engineering.


## Introducing `pytest`
We will use an automated test framework for Python called [pytest](https://docs.pytest.org/en/stable/index.html). Test frameworks are language-specific. Java has JUnit, C++ has CPPUnit, JavaScript has multiple options, etc. Automated test frameworks exist for nearly every programming language and do largely the same things.

`pytest` is a ***library***. ***Libraries*** are source code or compiled binaries that provide useful functions. They are almost always written in the same programming language as the program code. Professional software engineers use third-party libraries, often open source, to provide functions that they would otherwise have to write themselves. 

In our case, we could write some `try-except` blocks to catch our assertion exceptions, create counters to track the number of tests passed or failed, and then print out the results. But why do that when we can use a ***library***?  No sense in reinventing the wheel.

### Installing `pytest` with `pip`

We install `pytest` and another tool we will use later from the CLI. Choose your operating system below and follow the instructions:

{{< tabpane lang="bash" >}}
  {{< tab header="MacOS" >}}
pip3 install -U pytest pytest-cov
  {{< /tab >}}
  
    {{< tab header="Windows" >}}
    # Run in the PyCharm integrated Terminal
    pip install pytest pytest-cov
  {{< /tab >}}
 
{{< /tabpane >}}


What is `pip`? It is basically the App Store for Python *packages*. A package contains one or more *libraries* or executable tools. `pip` was included when you installed Python on your computer. We will use `pip` again to install useful packages in future labs.


## Running test code with `pytest`

Open your `testing-lab/` directory as the top-level project in PyCharm. If you need them, grab [`sample.py`](../organizing/sample.py) and [`test_sample.py`](../organizing/test_sample.py) and put them in that directory.


Run `pytest test_sample.py` in the PyCharm integrated terminal. You should see console output similar to the following:
```bash
collected 3 items                                  

test_sample.py ...                           [100%]

================ 3 passed in 0.01s =================
```

`pytest` scans your test file looking for functions that follow the naming convention `test_<function_name>` and "collects" them. I had three test case functions in my code, but you may have more or less, so your "collected" number may be different. **Test case function names *must* start with `test_` for `pytest` to run them.**

`pytest` then calls each test case separately and checks to see if the test case throws an `AssertionError`. If so, the test case fails. If not, the test case passes

Let's introduce errors in our program code `sample.py` to show `pytest` collecting multiple test case failures, which is one of our improvements needed for automated unit testing.

Open `sample.py` and make the following changes:
```python {linenos=true}
def palindrome_check(s):
    # cleaned_str = ''.join(s.lower()) 
    cleaned_str = ''.join(s)  # this makes "Kayak" no longer a palindrome because of different case 
    return cleaned_str == cleaned_str[::-1]

def is_prime(n):
    # if n <= 1:
    if n <= 0:  # the algorithm will now say that 1 is prime, which is incorrect by definition
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
Now run `pytest test_sample.py` again. Your output should now look something like this:
```
collected 3 items                                                                                                                                      

test_sample.py FF.                                                                                                                               [100%]

======================================================================= FAILURES =======================================================================
___________________________________________________________________ test_palindrome ____________________________________________________________________

    def test_palindrome():
        assert sample.palindrome_check("kayak")  # the function should return True, giving "assert True"
>       assert sample.palindrome_check("Kayak")
E       AssertionError: assert False
E        +  where False = <function palindrome_check at 0x1023494e0>('Kayak')
E        +    where <function palindrome_check at 0x1023494e0> = sample.palindrome_check

test_sample.py:5: AssertionError
____________________________________________________________________ test_is_prime _____________________________________________________________________

    def test_is_prime():
>       assert sample.is_prime(1) is False
E       assert True is False
E        +  where True = <function is_prime at 0x1023493a0>(1)
E        +    where <function is_prime at 0x1023493a0> = sample.is_prime

test_sample.py:9: AssertionError
=============================================================== short test summary info ================================================================
FAILED test_sample.py::test_palindrome - AssertionError: assert False
FAILED test_sample.py::test_is_prime - assert True is False
============================================================= 2 failed, 1 passed in 0.03s ==============================================================
```

We can see at the nice human-friendly summary at the end that 2 failed and 1 passed. The names of the test cases that failed are printed, as are the exact `assert` calls that failed. 


### Other ways of running `pytest`
1. You can run `pytest` without giving it a target file. `pytest` will scan the working directory looking for *files* with the naming convention `test_<file>.py`. It will collect and run test cases from all `test_<file>.py` it finds.
2. Try running `pytest --tb=line` to get a condensed version of the results if you find the output to be overwhelming.

## Recap
We accomplished a couple significant things in this lab:
1. We installed the `pytest` package using `pip`. Again, you only need to do this once.
2. We ran `pytest`, which scans for files and functions named `test_*` and runs them.
3. `pytest` collects test case successes and failures independently from one another, allowing us to get more information with each run of our test code.
4. `pytest` displays a summary of the results in human-friendly format.
5. All popular programming languages have a test framework. You will need to seek out one for the language you are working in.




## Knowledge check
- Question: The Python tool we run to install Python packages is called _______.
- Question: For `pytest` to find and execute tests automatically, the test files and test cases must begin with __________.
- Question: (True/False) You can have multiple `assert` statements in a single test case?
- Question: Create a file called `math.py` with the following function:
    ```python
    def compute_factorial(n):
        if n < 0:
            return "Factorial is not defined for negative numbers."
        elif n == 0 or n == 1:
            return 1
        else:
            factorial = 1
            for i in range(2, n + 1):
                factorial *= i
            return factorial
    ```
    1. Create a new, appropriately-named test file for `math.py`.
    1. Implement one or more test cases that cover all **program paths** in the function.
    1. Use `pytest` to execute your test code.

