---
title: Assignment 4 - Meteoric Design, Implementation, and Test
weight: 20
description: Apply low-level design rules to implement and test your application.
---

## Code resources
**Submitting code or other solutions** from anywhere other than your own brains is cheating. 
- Can you research how to use a particular function or library such as pytest? Yes. 
- Can you get code that solves all or part of your homework? No.
- When in doubt, *ask*. I will not be upset if you ask.

Refer to the full details in the [Syllabus on Canvas](https://uncw.instructure.com/courses/90540#honor-code).



## Setup
You will complete a program to analyze the NASA Meteorite Landings dataset: https://data.nasa.gov/widgets/gh4g-9sfh.
Setup

1. Download [`assignment4.zip`](assignment4.zip) and unzip it. It contains three files:
    - `meteorite_landings.csv`
    - `meteoric.py`
    - `test_meteoric.py`
2. Place these files in an `assignment4/` directory if not done for you.
3. Open the `assignment4` directory as a PyCharm project.
4. Configure `pytest`:
    - **Mac and Ubuntu on VirtualBox users**: Open that directory using PyCharm as usual.
    - **Windows users**: You can use either native Windows or WSL.
        - If using WSL, follow the setup process [at the bottom of this page](#setup-for-wsl-users). 
        - If you prefer to use native Windows, run the command `pip install pytest pytest-cov` from the PyCharm Terminal. Let me know if you get errors and I will help.

## Implementation
1. Implement a solution in `meteoric.py` to the Problem Statement below.
1. Put your name at the top of `meteoric.py` in the module docstring.
1. You may create classes and files and use imported libraries, but these things are not necessary.
2. Your solution must adhere to the [6 rules of low-level program design](../../labs//design/). Ask if you have any questions!
3. You are free to modify the provided code, including `load_data()` code. 
4. You will need to implement the [haversine formula](https://en.wikipedia.org/wiki/Haversine_formula). You may use code from the web, but include the link to the source website in a code comment.
5. Add docstrings following our [conventions](../../labs/style-and-documentation/documenting/) to any functions, classes, and files you create.
6. The code must adhere to the [PEP8 coding conventions](../../labs/style-and-documentation/conventions/) discussed in class.


## Testing
1. Add test cases to `test_meteoric.py`. Any additional source files you create must also have a `test_*.py` test.
3. All test cases must run from the CLI with `pytest`.
4. Use `pytest --cov --cov-branch --cov-report=html` to [generate a branch coverage HTML report](../../labs/testing/coverage/) in your project directory.
5. You must achieve 90% branch coverage in all *source* files ***except*** for the `main()` function.


## Rubric
- (5pts) [PEP8 coding conventions](../../labs/style-and-documentation/conventions/) followed
- (5pts) [Docstring conventions](../../labs/style-and-documentation/documenting/) followed for modules (files), classes (if any), and functions.
- (25pts) User commands are correctly implemented, including exception handling of user input errors.
- (10pts) Adherence to our [6 low level design rules](../../labs/design/).
- (15pts) Multiple test cases with proper [test structure](../../labs/testing/organizing/) for your source code. `pytest` branch coverage HTML report demonstrating &ge;90% branch coverage of all source code except for `main()`.

## Problem Statement

### Problem outline
Write a program the analyzes the NASA Meteorite Landings dataset available at https://data.nasa.gov/widgets/gh4g-9sfh. The program runs from the Terminal/CLI. The program will have two primary capabilities. The first is to display all meteorites discovered in a given year. The second is to display the meteorite geographically closest to a provided latitude and longitude. 

The program must run from the CLI as `python meteoric.py <command> <argument>`. See the input format and sample inputs for examples of running the program.

### Input format
The program must understand the following commands:
- `year <integer>`: Print out the meteorite name, latitude, and longitude for all meteorites discovered in the `<integer>` year. It is possible that no meteorites were discovered in a given year. Example usage: `python meteoric.py year 1999`
- `geopoint <latitude,longitude>`: Print out the meteorite name, latitude, and longitude for the meteorite with the closest [great-circle distance](https://en.wikipedia.org/wiki/Haversine_formula) to the coordinates. Latitude is a float in the range [-90.0, 90.0]. Longitude is a float in the range [-180.0, 180.0]. Example usage: `python meteoric.py geopoint 34.2257,-77.9447`
  
The data in `meteorite_landings.csv` looks like this:
```
name,id,year,reclat,reclong
Aachen,1,1880,50.775,6.08333
Aarhus,2,1951,56.18333,10.23333
Abee,6,1952,54.21667,-113
Acapulco,10,1976,16.88333,-99.9
...
```

|Field|Description|
|-----|-----|
|`name`|A name for the specific meteorite.|
|`id`|A unique integer identifier for the meteorite.|
|`year`|The year the meteorite was found or observed. Years are positive 4-digit integers.|
|`reclat`|The latitude at which the meteorite was found. Latitudes are floats in the range [-90.0,90.0].|
|`reclong`|The longitude at which the meteorite was found. Longitudes are floats in the range [-180.0,180.0].|

<mark>**Important:**</mark> a `load_data()` function is provided in `meteoric.py` that loads the data from `meteorite_landings.csv` into a list of lists. You do not need to validate the data in the CSV file, however, some fields may be blank if the information is missing. 

### Output format
- Print meteorite data to the console in a human-friendly format.
- When searching for all meteorites that were discovered in a given year the program will either: (a) display a list of meteorites discovered, or (b) display a message stating no meteorites were found for the given year. 
- When searching for the closest meteorite landing from a specific location, the program will display the name (or names if two or more meteorites have an equal distance from the specified location) of the meteorite closest to the location given by the user. 
- If the user fails to provide a valid command or valid arguments, the console displays an error message indicating what the user did incorrectly.

### Exceptional conditions
Do not assume the `<command>` or `<argument>` are present or valid. The program must print an error message, not an exception or stack trace, if given bad arguments. 
- user can put in an invalid command keyword
- user does not give an argument
- user gives an invalid data type with the year keyword
- user enters a year with no meteorite
- user inputs latitude and longitude incorrectly
- user enters multiple arguments
- user gives an out of range latitude or longitude


### Sample input
1. `python meteoric.py test`: invalid command
2. `python meteoric.py year`: missing argument
3. `python meteoric.py geopoint`: missing argument
3. `python meteoric.py year s`: invalid argument
3. `python meteoric.py geopoint abcdef`: invalid argument
3. `python meteoric.py year 1999 2001 asd`: invalid arguments
3. `python meteoric.py geopoint 120.884,300.475`: invalid latitude and longitude
3. `python meteoric.py geopoint 32.558,78.854`: valid search by geopoint
3. `python meteoric.py year 1818`: valid search by year
3. `python meteoric.py year 55`: valid search by year,  no meteorites match that year

### Sample output
You may change these to be more precised if you like, but not less precise.
1. `Invalid command and argument. Correct format is python meteoric.py <command> <argument>.`
1. `Invalid command and argument. Correct format is python meteoric.py <command> <argument>.`
1. `Invalid command and argument. Correct format is python meteoric.py <command> <argument>.`
1. `Invalid argument. year argument must be an integer.`
1. `Invalid argument. geopoint argument must be latitude,longitude.`
1. `Invalid command and argument. Correct format is python meteoric.py <command> <argument>.`
1. `Invalid argument. geopoint latitude or longitude out of range.`

8. 
    ```
    Meteorite(s) discovered closest to 32.4, 103.92:
        Guangyuan, latitude: 32.4, longitude: 105.9
    ```
9.
    ```
    Meteorite(s) discovered in 1818: 
        Seres, latitude: 41.05, longitude: 23.56667
        Slobodka, latitude: 55, longitude: 35
        Zaborzika, latitude: 50.28333, longitude: 27.68333
        Cambria, latitude: 43.2, longitude: -78.8
        Cape York, latitude: 76.13333, longitude: -64.93333
    ```
10. `No meteorites found for the year 55.`


## Submission due Sunday, March 30
Upload all `.py` files from your project directory to [Assignment 4 on Canvas](https://uncw.instructure.com/courses/90540/assignments/1268128).



## Setup for WSL Users
1. Open PyCharm and select the `File` menu, then `Close Project`.
1. Select `WSL` on the left, then the `+` button to create a new project. 
1. Select the `...` button to pick the Project directory. 
1. Pick your Ubuntu instance at the top, then navigate to `home/<your_id>/seng-201/` and create a new folder (icon at the top) for `assignment4`. 
1. Select the new directory and hit `OK`.   
1. Click `Start IDE and Connect` on the screen. PyCharm will take a minute to finish configuring. It should open a new window with a `main.py` file showing some boilerplate code.
1. Select the `File` menu, then `Settings`.
1. Select `Project: assignment4` in the left pane, then click the `Python Interpreter` link.
1. Select the `Add Interpreter` link near the top right, then `Add Local Interpreter`. 
1. Leave the default options selected and hit `OK`. If you see a red error message, contact the instructor.
1. `OK` out of the settings screen.
1. Finally, open a ***new*** Terminal within PyCharm. Type `which pip`. You should see something like 
    - `/home/<your_id>/seng-201/assignment4/.venv/bin/pip`, or;
    - `/home/<your_id>/virtualenvs/assignment4/bin/pip`
    - but ***not*** `/usr/bin/python`
7. **You will run all subsequent Terminal commands from the integrated Terminal in PyCharm.**
1. run the following in the integrated Terminal:
    ```bash
    pip install pytest pytest-cov
    ```
1. Complete the setup instructions at the [top of this lab](#setup).