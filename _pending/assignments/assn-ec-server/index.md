---
title: Extra Credit Assignment - PyGame or Flask
weight: 60
description: Researching and implementing a PyGame or Flask application.
---

## Instructions
This is an **individual assignment**. You may not collaborate. You will need to do your own research for this, and you may use AI to assist you. You may not communicate or obtain human help.

You have two options:
1. Add more pages to the Flask app from [Lab: Flask server app](../../labs/client-server-sample/flask-server/) to create a browser-based quiz experience.
2. Add more functionality to the game from [Lab: Pygame client app](../../labs/client-server-sample/pygame-client/) and continue to interact with the question server. 

You may earn credit for either the Flask option or the PyGame option, but not both. 

## Citations
In your code, clearly indicate any code that you obtained from an external source. Put the URL of the source in your code. **Copying code without citing your source is plagiarism.**

## Option 1: Extend Flask

**To earn any credit**:
- You must have a total of 10 questions in the system. 
- You must use the Flask quizzer app from [Lab: Flask server app](../../labs/client-server-sample/flask-server/) and [Assignment 7](../../assignments/assn7-deployment/). Run the server app on your local machine, not `ada`.
- You must use the existing API and backend functions. You can extend those functions and add your own.

Each **item** below is worth points. You earn the points by fulfilling ***all*** the requirements of an item. Partial credit for an item will not be awarded. You deliver some or all of the items.

1. **(5pt item)**: Add a "Show All Questions" option to the homepage. This takes the user to a page where all of the questions are shown. The question test and choices must have separate HTML styles. The correct answer must be highlighted among the choices. No interactivity is required. 
2. **(5pt item)**: Add a "Random question" option to the homepage. This takes the user to a page where they a random question and the question choices. The user can select an answer and is told if they chose the correct answer or not.
3. **(5pt item)**: An anonymous user can "Start a Quiz" from the home page. The quiz is 10 *random* questions (sampling with replacement). The user is shown how many questions they answered correctly at the end. The user must be able to return to the homepage and start a new quiz after completing the previous one.
4. **(5-10pt item)**: You may propose an 1-2 additional features of your choosing to the instructor. You must receive approval for each feature beforehand to receive credit.
   
## Option 2: Extend Pygame app

**To earn any credit**:
- You must have a total of 10 questions in the system. 
- You must use the Flask quizzer app from [Lab: Flask server app](../../labs/client-server-sample/flask-server/) and [Assignment 7](../../assignments/assn7-deployment/). Run the server app on your local machine, *not* `ada`.
- You must use the existing API and backend functions. You can extend those functions and add your own.

Each **item** below is worth points. You earn the points by fulfilling ***all*** the requirements of an item. Partial credit for an item will not be awarded. You deliver some or all of the items.

1. **(5pt item)**: Fix the scorekeeping such that each question answered correctly is worth 2 points, and each incorrect choice deducts 1 point with no minimum. The score must be shown when the user quits the game, and on each question page (a running score).
1. **(5pt item)**: Add an "Incorrect" message, styled red at a minimum, when the user chooses the incorrect option for a question. Add a "Correct" message, styled green at a minimum, when the user chooses the correct option. When correct, either add a 2 second delay before showing the next question, or add a button on the screen the user must click to proceed. Do not allow the user to proceed to the next question until they get the current question correct.
2. **(5pt item)**: Add a main menu showing a Quit and Start Quiz option with instructions for how to choose each option. On Starting a Quiz, show 10 *random* questions (sampling with replacement). The user is shown their score at the end. The user must be able to return to the homepage and start a new quiz after completing the previous one.
3. **(5-10pt item)**: You may propose an 1-2 additional features of your choosing to the instructor. You must receive approval for each feature beforehand to receive credit.

## Final submission due Sunday, Dec 8
1. Indicate [on Canvas](https://uncw.instructure.com/courses/83039/quizzes/322664) which extra credit option you chose.
1. **For *both* Flask and PyGame**: Ensure that all of your changes are merged into the `main` branch.
3. **For *both* Flask and PyGame**: Push the latest version of your Flask server app to your [Assignment 7 GitHub repository](../assn7-deployment/).
4. **PyGame option only**: Push the latest version of your PyGame app to your PyGame GitHub Repo from [Lab: PyGame client app](../../labs/client-server-sample/pygame-client/).
