---
title: Flask server app
weight: 5
description: Installing and starting a sample Flask web app
---


## Intro
The Python web application above is written using the [Flask framework](https://flask.palletsprojects.com/en/stable/). Flask is used by companies including Netflix, Uber, and LinkedIn  to create web applications. It is installed as a Python library with the `pip` tool.

## Webapp setup
Deploying this Flask web application to `ada` is your Assignment #7. Follow these steps to check out and run the project on your computer:
1. Accept the GitHub Classroom assignment #7: <https://classroom.github.com/a/wbeITctx>. This is an individual assignment.
2. Clone the repo to your your local computer. This should create a project directory called  `assn7-<your_name>` or something similar.
3. Using your Terminal, `cd` into the project directory. 
4. Open Visual Studio Code in the working directory with `code .`. It is essential that your `assn7-<your-name>/` directory is the top-level of Visual Studio Code.
5. In the menu bar, select View &rarr; Command Palette
6. Search for "environment" and select **Python: Create Environment...**
7. Select **Venv**
8. Select a recent Python version.
9. On "Select dependencies to install", check the box next to `requirements.txt`. Click "Okay". 

It may take a minute. Visual Studio Code will create a copy of Python in the directory in the `.venv/` subdirectory. This is considered best practice in Python development when you need to install libraries, like Flask, so that you do not "pollute" the system Python directory with many libraries that are not needed for all your programs.

## Project structure
You will see several files in the project folder:
- `app.py`: This is the main Python file that defines the Flask application. It specifies what types of requests to respond to. It calls the other files to handle the logic. Think of it as the user interface of the application.
- `quizzer.py`: a plain Python file that has some functions related to quiz questions and answers. This functions are called by `app.py`.
- `questions.py`: contains a Python class definition for a `MultipleChoiceQuestion` and initializes a list of QUESTIONS the app serves.
- `test_quizzer.py`: unit tests for `quizzer.py`. You can run `pytest` in the Terminal to try them.
- `templates/`: website files go in here to be sent to a browser. For now, there is only `index.html`, which `app.py` sends back to clients that browser to the server's home page.
- Other things:
  - `.venv/`: the Python virtual environment used to run the app. Ignore this.
  - `.gitignore`: tells Git to ignore specific files.
  - `requirements.txt`: tells the virtual environment which `pip` libraries are needed to run the project.


## Running the webapp
We need to run the Flask web application from Visual Studio Code's integrated terminal. 

**Note:** Flask will only run with the "virtual environment" in `.venv/` active. Visual Studio Code will activate it for you automatically. If you want to run from your system Terminal, you will need to run `source .venv/bin/activate` first from your project directory.


Run `flask --app app run --debug` to start the Flask webapp. You should see output similar to the following in your Terminal:
{{< figure src="flask-run.png" alt="Console output of a successful Flask run" >}}


You may be prompted by your OS to allow connections. You do not need to allow external connections for it to work.

Open a web browser to <http://127.0.0.1:5000>

You should see the Welcome Page:
{{< figure src="quizzer-homepage.png" alt="Welcome screen for the Quizzer Flask project" width="720">}}

Great! You are now running a web application built in Python using the Flask library.


## Interacting with the web app
Your web browser is a client and the Flask app is a server. Web browsers issue HTTP requests to servers, and the servers send an HTTP response. 

Think of HTTP requests and responses as another envelope. The envelope is a merely a string of text in a particular format. The *contents* of the envelope are bits that can be strings, images, videos, audio, integers, floats, etc. 

This Flask web app is sending its contents as strings in JSON format. The JSON form is very similar to a Python dictionary: it has keys and values.


## Key commands
Make sure you have the project open in Visual Studio code and are using the Integrated Terminal.
- **To start**: `flask --app app run --debug` 
- **To stop**: Hit `CTRL+C` with the Terminal selected.