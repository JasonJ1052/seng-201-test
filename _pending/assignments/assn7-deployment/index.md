---
title: Assignment 7 - Deployment
weight: 50
description: Deploying a simple webapp to a remote server
---

## Objectives
- More practice working with remote servers.
- Practicing extending an existing application, albeit simply.

## Setup
1. If not done already, complete the [Labs on working with remote servers](../../labs/remote-server/) so that you can connect to the `ada.cis.uncw.edu` server.
2. If not done already, complete [Lab: Flask server app](../../labs/client-server-sample/flask-server/) to sign-up for, check out, and run the assignment.

## Part A - extend the web app
Work on **your computer** to extend and test the `assn7` app.
1. Create and work in a new branch.
2. Open the file `templates/index.html` and the header line to `<h1>Welcome to [YOUR_NAME]'s Flask Quizzer!</h1>`
3. Add ***at least*** three more `MultipleChoiceQuestion`s to the list in `questions.py`.
4. Start the server app on your computer using `flask --app app run --debug`. Full setup and running instructions are in [Lab: Flask server app](../../labs/client-server-sample/flask-server/).
5. (See note below) Test your changes using a web browser as a client, i.e., navigate to <http://127.0.0.1:5000>. 
6. Commit and push your branch.
7. Merge your branch into `main`. Commit and push `main` to GitHub.

### Testing the server app locally
You test your app by calling the API endpoints. Do this by putting an endpoint URL into the address bar of your browser. 

You will need to get the unique id (UUID) of the question you want to check. The UUIDs will change every time you start your server. You can get them by trying random questions, like in the video below, or (even better) you can add a `print()` statement to the loop in `questions.py` to print them out when they're made.

Like below:
<video controls autoplay playsinline muted loop>
<source src="app-testing.mp4" type="video/mp4">  
</video>

## Part B - deploy and run your app on `ada`
You must be on the `hawkwifi`, a UNCW lab computer, or the VPN to connect to `ada.cis.uncw.edu`.

### Setup on `ada`
1. Connect to the `ada` server and clone your `assn7` GitHub repo there as described in [Lab: Working on `ada`](../../labs/remote-server/working-on-ada/).
2. `cd` into your project directory
3. Create the virtual environment needed to run flask with the following commands:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
   You should see several libraries install.

### Running on `ada`
1. Make sure you are in the project directory.
1. Your `ada` Terminal must show the text `(.venv)` before you can run the server. If you **do not** see `(.venv)`, run `source .venv/bin/activate` to activate the virtual environment.
2. ```bash
   flask --app app run -h 0.0.0.0 -p [5-digit]  # put a number between 20000-50000
   ```
   Use a different port number if you see an error like `Port 23456 is in use by another program. Either identify and stop that program, or start the server with a different port.`

### Updating your code on `ada`
If you find a bug, or want to change something in your code, work on it on your local computer first. Commit and push to GitHub. Then connect to `ada`, pull your changes, and try them there.

## Submission due Monday, December 2
1. Commit and push all your changes to GitHub.
2. Permanently run your server on `ada` by doing the following:
   ```bash
   nohup flask --app app run -h 0.0.0.0 -p [5-digit port number]
   ```
   You will see different output.
3. Hit `CTRL-Z` to suspend the server
4. Run the command `bg` to put the server in the background.
5. Run `cat nohup.out`. Note the URL in that file. 
6. Open a browser and put in your URL address to verify that can accessing the app remotely.
7. Submit your server's URL including the port on the Canvas assignment page: <https://uncw.instructure.com/courses/83039/assignments/1258974>


## Assignment 7 Rubric
- (10pts) `git log` history shows commits to a feature branch and merge into `main` with required changed to the app.
- (15pts) Final version deployed, accessible, and functional on `ada` with URL submitted to the Canvas assignment.