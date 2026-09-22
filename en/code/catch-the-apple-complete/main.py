from p5 import *
from random import randint

# Global variables go here
apple_x = 200
apple_y = 0
score = 0
lives = 3


def setup():
    size(400, 400)
    no_stroke()
    text_size(20)


def draw():
    # Access global variables
    global apple_x, apple_y, score, lives


    # Clear the background
    background('lightblue')


    # Display score and lives
    fill('black')
    text('Score: ' + str(score), 15, 30)
    text('Lives: ' + str(lives), 300, 30)


    # Check game over
    if lives == 0:
        text('Game over!', 140, 180)
        text('Stop, then Run to play again', 65, 220)
        return


    # Show instructions
    text('Move the mouse to catch apples', 45, 65)


    # Draw the basket
    fill('brown')
    rect(mouse_x - 40, 350, 80, 20)


    # Draw and move apple
    fill('red')
    circle(apple_x, apple_y, 20)
    apple_y = apple_y + 3


    # Check catches and misses
    if apple_y >= 340:
        if abs(apple_x - mouse_x) < 50:
            score = score + 1
        else:
            lives = lives - 1


        # Reset the apple
        apple_x = randint(20, 380)
        apple_y = 0


# Start the game
run()
