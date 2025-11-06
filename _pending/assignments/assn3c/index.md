---
title: Assignment 3.c - Meteoric Maintenance
weight: 25
description: Extending code functionality.
---


## Part c - maintenance
***Software maintenance*** is the term for updating software code to provide new functionality, change existing functionality, fix bugs, or implement a better design. Good software design makes maintaining long-lived code easier.

You will work with your partner(s) update your `meteoric.py` implementation. Start with code you submitted for [Assignment 3.b](../assn3b/). Review the [collaboration, cheating, and personal proficiency section of the course syllabus](https://uncw.instructure.com/courses/83039).

## Instructions

You must design, implement, and test your expanded solution. Review the changes in this section, then look at the [rubric](#rubric) for what is expected.

<mark>**Clarification**:</mark> You do not use Git or GitHub with this assignment.

### a) Changing data

Researchers have been hard at work and added new information to the meteorite data. Download [meteorite_landings_full.csv](meteorite_landings_full.csv). 

New fields have been inserted for each meteorite:
<pre><code>name,id,<strong>nametype,recclass,mass (g),fall,</strong>year,reclat,reclong
Aachen,1,<strong>Valid,L5,21,Fell,</strong>1880,50.775,6.08333
Aarhus,2,<strong>Valid,H6,720,Fell,</strong>1951,56.18333,10.23333
Abee,6,<strong>Valid,EH4,107000,Fell,</strong>1952,54.21667,-113
Acapulco,10,<strong>Valid,Acapulcoite,1914,Fell,</strong>1976,16.88333,-99.9
</code></pre>


Alter `meteoric.py` so that it loads data from `meteorite_landings_full.csv`. You no longer use the old `meteorite_landings.csv`.


The `year` and `geopoint` commands must continue to work. Update these commands to print the new fields of `nametype`, `recclass`, `mass (g)`, and `fall`.

### b) New commands

Your `meteoric.py` must support the following new commands in addition to `year` and `geopoint`:
- `class <string>`: print all meteorites whose `recclass` matches the provided string. The match must be case insensitive: 
  - a search for `h6` will match all meteorites with type `H6` or `h6`
  - a search for `aCupuLCOITE` will match `Acapulcoite`.
- **(Extra Credit)**  `heaviest <n>`: print the top `<n>` heaviest meteorites according to their `mass (g)`. The list must be sorted so that the heaviest is printed first and the least heavy is printed last. `<n>` is an integer greater than 0. For example `heaviest 5`.
  - You need to implement the sorting logic, you cannot just hardcode a list of heaviest meteorites.
- **(Extra Credit)** `count-fall`: print the number of meteorites for each unique value of the `fall` field. The command ignores any arguments. 
  - There are only two values in the data: `Fell` and `Found`, but your algorithm **MUST** account for the possibility that new values will be added, so you cannot hardcode these values in your algorithm. Example output: 
  ```
    Fell 1107
    Found 44609
    ```

## Rubric

- (5pts) Update your problem statement in `spec.txt` to account for the new commands, including input samples, exceptional conditions. Update all output samples to include the new fields.
- (5pts) [PEP8 coding conventions](../../labs/style-and-documentation/conventions/) and [Docstring conventions](../../labs/style-and-documentation/documenting/) followed.
- (15pts) `class` command implemented and old commands are updated to correctly use the expanded CSV file, including exception handling of user input errors.
- (5pts) Adherence to our [6 low level design rules](../../labs/design/).
- (10pts) `pytest` branch coverage HTML report demonstrating 90% branch coverage of all source code except for `main()`.
- (10pts each) Correct implementation and test of `heaviest` and/or `fall` commands.


## Submission due Oct 27
Zip your project directory, including `spec.txt`, all Python files, and your coverage report. Upload the `.zip` file to [Assignment 3, Part C on Canvas](https://uncw.instructure.com/courses/83039/assignments/1247519).