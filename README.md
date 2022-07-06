# Python Terminal Brick game

## Introduction

This is the terminal version of Brick game written in Python. It uses the basic Python libraries and modules.

This game has been tested on **Linux** based Operating Systems.

## NEW FEATURES

Now there are levels in the game .

After each level new pattern of bricks will appear and the exploding bricks will remain as it is. Also breaking of exploding bricks will not add in your score.

In the boss level the boss will follow the paddle and killing the boss has 5 lives. After defeating the boss the game will end. Killing the boss will also lead to 1 point.

Falling bricks implemented

## Structure and Features

The game application exhibits the OOP concepts of Inheritance, Encapsulation, Polymorphism, Abstraction along with Function Overloading.


## About the Game

### Controls

* a - will move paddle Left
* d - will move paddle Right
* s - will shoot the ball
* q - Quit the game

### Features

1. Yellow brick - Will break in one collision. Has length 5

2. Blue brick - Will break in two collision and after one collison the colour will change to yellow. Has length 5

3. Red brick - Will break in three collision and after each collision the colour will change indicating the current strength. Has length 5

4. Unbreakable brick - Can't be broken with normal ball. Has length 5

5. TnT brick - These bricks have length 1 and on collision with the ball will break all nearby bricks. 


### Powerups

1. Shrink: This powerup will shrink the paddle for 10 seconds and after that the paddle will turn to normal.The powerup is denoted by S

2. Elongate: This powerup will increase the length of the paddle for 10 seconds and after that the paddle will turn to normal.The powerup is denoted by L

3. Thru-ball: When this powerup is active it will destroy any brick in its path for 10 seconds.The powerup is denoted by t

4. Fast ball: When this powerup is active it will increase the speed of the ball for 10 seconds.

5. Grab-ball: After picking up this powerup Grab power will become active and the next time when the ball will land on the paddle it will be grabbed and can be released on your will and then the grab power will turn inactive.

### Notes
- If shrink powerup is on and if you get elongate powerup so the elongate powerup will nullify the effect of shrink powerup and viceversa till both of them are active together.
- At the top you can see the score , total time , Remaning time of powerups.

## Running the program

1. Install all the requirements:
    - `pip install colorama`
2. Run the program:
    - `python3 main.py`

## Project Tree

* alarmexception.py
* ball.py
* board.py
* bricks.py
* getch.py
* main.py
* paddle.py
* powerup.py
* __pycache__
    * alarmexception.cpython-38.pyc
    * ball.cpython-38.pyc
    * board.cpython-38.pyc
    * bricks.cpython-38.pyc
    * getch.cpython-38.pyc
    * paddle.cpython-38.pyc
    * powerup.cpython-38.pyc
    * scenery.cpython-38.pyc
* README.md
* scenery.py
* testing.py

