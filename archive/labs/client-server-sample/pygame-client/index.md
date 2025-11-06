---
title: PyGame client app
weight: 10
description: Running a game that talks to the Flask server
---


## Intro
[In the previous lab](../flask-server/), we checked out and ran a Flask web app.

We saw that a web browser can work as a function for the Flask web app. Let's use another client that is a game. After all, the Flask app is just sending JSON data, which is basically a dictionary. Python can handle dictionaries.

The app below is a game with minimal functionality that enables you to answer quiz questions.

## Pygame app setup

1. Accept the PyGame Quizzer assignment: <https://classroom.github.com/a/dPKVKNki>. 
2. Clone the repo to your your local computer. This should create a project directory called  `pygame-quizzer-<your_name>` or something similar.
3. Using your Terminal, `cd` into the project directory. 
4. Open Visual Studio Code in the working directory with `code .`. It is essential that your `pygame-quizzer-<your-name>/` directory is the top-level of Visual Studio Code.
5. In the menu bar, select View &rarr; Command Palette
6. Search for "environment" and select **Python: Create Environment...**
7. Select **Venv**
8. Select a recent Python version.
9. On "Select dependencies to install", check the box next to `requirements.txt`. Click "Okay". 

Visual Studio Code will take a minute to create a `.venv/` subdirectory and install all the pygame libraries to it. 

### WSL users
You need to have WSL2 for GUI applications to work from WSL. On the Windows side, open a Command Prompt or PowerShell (**not** Ubuntu)

1.
    ```bash
    wsl --list --verbose
    ```

    You will see something like:
    ```bash
    NAME            STATE            VERSION
    * Ubuntu-24.04    Running          1
    ```
    If you see VERSION 2, you are good.
2. If you see VERSION 1, run
    ```bash
    wsl --set-version <Ubuntu name> 2  # e.g., wsl --set-version Ubuntu-24.04 2
    wsl --update
    ```
    This will take some time.
3. Finally, open a new **Ubuntu** terminal and run 
    ```bash
    sudo apt update
    sudo apt install libsdl2-2.0-0 libsdl2-dev libsdl2-image-2.0-0 libsdl2-image-dev
    ```
## Project structure
You will see a few files in the project folder:
- `quiz_game.py`: The only actual Python file. You will run this.
- Other things:
  - `.venv/`: the Python virtual environment used to run the app. Ignore this.
  - `.gitignore`: tells Git to ignore specific files.
  - `requirements.txt`: tells the virtual environment which `pip` libraries are needed to run the project.

## Running the game
We need to run the game from Visual Studio Code's integrated terminal. 

**Note:** The game will only run with the "virtual environment" in `.venv/` active. Visual Studio Code will activate it for you automatically. If you want to run from your system Terminal, you will need to run `source .venv/bin/activate` first from your project directory.

To run the game:
1. First, make sure your Flask webserver is also running. You will need to have two Visual Studio Codes running (or system Terminals with the virtual environments activated). To open a second Visual Studio Code:
   - In Code, File &rarr; New Window will open a second IDE. From second IDE, you can do File &rarr; Open Folder to open the server project directory.
   - You can also type `code .` in each of the game and server directories to open a separate IDE for each project. 
1. From the client game's IDE terminal, run `python quizzer_game.py`

You should see a screen like this:
{{<figure src="pygame.png" alt="pygame window" width="640">}}

- Use the arrow keys to make a choice.
- Hit enter to check the answer:
  - The app will do nothing if you are wrong.
  - The game will display a new question if you are right. There are only two questions, so 50/50 that you will see something different.
- Hit `q` or close the window to quit the game. Your score will always be 0.
  
