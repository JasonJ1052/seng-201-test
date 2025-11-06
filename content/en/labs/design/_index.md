---
title: 10. Low-level Design
weight: 50
description: Best practices for organizing functionality.
---


## Motivation
We make references to "writing code *the right way*", but that is secondary to getting the correct answer. After all, how can you get a good grade if it doesn't work?

In software engineering, everything needs to work, but doing it *the right way* is equally important. Why? 
- Because you are on a team, and someone else may have to understand and edit your code. Including your future self. We call this ***understandability***.
- Poorly-implemented solutions are more difficult to change without introducing bugs. We call this ***maintainability***.
- Poorly-implemented solutions may work with small data, but become intolerable with millions of records. We call this ***efficiency***.
- Overly-specific solutions that make assumptions about the data will break when encountering "the real world". Avoiding this is called ***robustness***.

## The Rules

These characteristics are the result of your *code design*. The labs in these sections will go through code-level design principles that you, the developer, are responsible for when writing code. 

The rules are:

1. [Avoid magic literals](./magic-literals/).
6. [Functions should have a single responsibility](./srp/).
5. [DRY (Don't Repeat Yourself) and the Rule of Three](./dry/).
2. [Handle errors at the lowest sensible level, and re-raise/re-throw them otherwise](./except-lowlvl/).
3. [Raise specific errors and define your own if needed](./except-specific/).


**Write these down!** We will explore them in-depth in turn. We will start by creating a simple game, then applying design rules to it.

Click below to get started.