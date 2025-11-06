---
title: pygame setup
weight: 5
description: Getting started with a game.
---

## Example event-driven program using `pygame`

We'll have some fun by creating a very simple game using the [`pygame`](https://www.pygame.org/docs/) library. Our example program comes from a very excellent YouTube tutorial called ["The Ultimate introduction to Pygame"](https://www.youtube.com/watch?v=AY9MnQ4x3zk&ab_channel=ClearCode) by [Clear Code](https://www.youtube.com/@ClearCode). I highly recommend his channel as his tutorials are clear and to the point.


<video controls autoplay playsinline muted loop width="800">
<source src="pixelrunner.webm" type="video/webm">  
</video>

We will implement the code as in his tutorial, but we will re-design the code by applying the rules above. His code works just fine, but our re-design will help improve the ***understandability***, ***maintainability***, ***efficiency***, and ***robustness*** of the software.

## Setup
1. Open a Terminal and use `cd` to get into your `seng-201` directory.
1. Run the command `git clone https://github.com/UNCW-SENG/pygame-design`. This will create a subdirectory named `pygame-design`.
1. Open PyCharm. Go through the menus: `File -> Open`. Find and open the `pygame-design/` folder, then hit the `Open` button. You should see the following structure:
    {{<figure src="project-start.png">}}
    It is essential that the root folder is `pygame-design/`
3. Click in the bottom right of your PyCharm window where it either says `Add interpreter...` or `Python 3.x (something)`. 
4. Then select `Add Interpreter -> Add Local Interpreter`. You should see something similar to the following:
        {{<figure src="add-interpreter.png" width="800">}}
5. Make sure `Generate New` is selected. The pre-populated location should be fine. Then hit `OK`.
6. Open the Integrated Terminal in PyCharm. Type the command `pip install pygame` to download the `pygame` library.
7. Open `runner.py` and run it. A black screen should pop-up and you should see `Hello from the pygame community` in the integrated Terminal.
        {{<figure src="game-launched.png" width="800">}}

You should now be good to go.


## Class recording

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/r9kRLCIr8ow?si=oRAOnf6TT2YPWJ51" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Code at the end

You must have cloned the project from the setup section. Here is the code at the end of class: 
- [`runner.py`](./runner.py)


## Next up
Up next is our first principle: [avoid magic literals](../magic-literals/). 

<!-- 
## Lesson 1: More pygame, Rules 1-2

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/eaB6jYa4A0s?si=kg7avzWnhSj-a_OD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Lesson 2: Rules 1-2 again

Grab the following files:

- [`enemies.py`](enemies.py): place it at the top level next to `runner.py` and `splash.py`
- [`beetle1.png`](beetle1.png) and [`beetle2.png`](beetle2.png): create a new subdirectory `graphics/beetle/` and place both files inside.
- **(Only if you're not caught up from last time)**: [`runner.py`](end-day-2/runner.py) and [`splash.py`](end-day-2/splash.py)

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/LQvFshmDyJQ?si=pnd5jhVdFwpq5HO3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Code at the end of Lesson 2
- [`player.py`](end-day-3/player.py)
- [`runner.py`](end-day-3/runner.py)

## Lesson 3: Rules 3-4 + refactoring an existing application

Do the following:
- Make sure you are up-to-date and have all files from Lesson 2.
- Download [`bank-accounts.zip`](bank-accounts.zip). Unzip it alongside your other projects but *not* inside the pygame one. This is a separate project that we will open in PyCharm during the lesson. Unzipping the file will create a `bank-accounts/` subdirectory containing several files.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/cKYUWD-QXgg?si=VSN-fkWncnqPETKU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Code at the end of Lesson 3
- From our game
    - [`runner.py`](end-day-4/runner.py)
    - [`enemies.py`](end-day-4/enemies.py)
- From process-accounts project: [`process_accounts.py`](end-day-4/process_accounts.py)


## Lesson 4: Rules 5-6 on error handling

We pick up right where we left off in the previous example.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Klmzm0ju1Vw?si=zOtGIxbvUKSnm2yL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Code at the end of Lesson 4
- From process-accounts project: [`process_accounts.py`](end-day-5/process_accounts.py) -->