Scenario 1: Sharing a new project
1. Do GitHub CLI setup
2. [WORKSHEET] run through 1-3
3. create remote-sample/ and open in Visual Studio Code
4. Create test.py. print("We are going to share our new repository")
5. git init
6. git add . + git commit
7. Create a "blank remote repo". Go to github.com, new, remote-sample as name
8. Show "success" page
9. Comment on public vs. private
10. copy the "...push an existing repository from the command line"
11. View the remote repo in the browser
12. [WORKSHEET] run through 4-6

Subsequent versions
1. test test.py
2. add and commit
3. git log. Point out local repo vs. remote repo
4. [WORKSHEET] add local main and remote main to pg 2 top picture
5. git push
6. [WORKSHEET] add 2nd version to remote, update main refs, label git push arrow
7. Refresh the browser. Show the history.
8. [WORKSHEET] fill bottom of page 2.

Scenario 2: Clone an existing project
1. [WORKSHEET] Walk through 1-3
2. Have students open https://github.com/llayman/git-remote-clone in browser.
3. Terminal, cd into seng-201
4. git clone https://github.com/llayman/git-remote-clone
5. [WORKSHEET] Fill in drawing
   1. Create workspace folder, then local repo.
   2. Right to left. Cloned version into local. Link remote main to local main.
   3. Clone Version into workspace.
6. [WORKSHEET] Fill in bottom.
7. DO NOT EDIT FILES YET.

Scenario 3: Retrieving changes.
1. [WORKSHEET] Explain the scenario at top.
2. Or, scenario where a teammate makes a change.
3. [YOU CODE] Edit git-remote-clone/hello.py and push a new version.
4. Have students refresh the repo in their browser.
5. [WORKSHEET] add main refs to the top.
6. Have everyone run git pull. Point out how the code changes.
7. Run git log
8. [WORKSHEET] Fill out the middle bullet points and the bottom diagram.