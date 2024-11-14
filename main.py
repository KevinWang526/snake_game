import turtle
import random
import time
from snake import Snake
from apple import Apple

def display_instructions():
    print("Instructions:")
    print("1. Use the arrow keys on your keyboard to control the snake.")
    print("2. Do not let your snake reach the edges of the screen.")
    print("3. Direct your snake to reach the red apple to collect points.")
    print("4. Do not let your snake eat/cross its own tail.")
    print("5. Fully open the pop up to see the game better!")
    print("Double click on the screen to get started")
    print("")

def draw_borders():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(5)
    pen.color("#FFFFFF")
    pen.pensize(2)
    pen.penup()
    pen.goto(-199, -199)
    pen.pendown()
    for _ in range(4):
        pen.forward(398)
        pen.left(90)

def start_game(x, y):
    game_over = False
    delay = 0.25

    while not game_over:
        screen.bgcolor((200 / 255, 200 / 255, 200 / 255))
        snake.move()

        # Check if the snake goes off the screen
        if snake.is_off_screen():
            print(" >>> Game Over! <<<")
            game_over = True

        # Check if the snake bites its own tail
        elif snake.is_biting_tail():
            print(" >>> Game Over! <<<")
            game_over = True

        # Check if the snake reaches the apple
        elif snake.position == apple.position:
            snake.score += 1
            print(f"Score: {snake.score} pts")
            snake.grow()
            apple.respawn(snake.tail, snake.position)

        screen.update()
        time.sleep(delay)

    # Close the window after game over
    turtle.bye()


def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

# Setup the Stage
screen = turtle.Screen()
screen.tracer(0, 0)
screen.setup(400, 400)
screen.bgcolor((200 / 255, 200 / 255, 200 / 255))

# Draw the white borders
draw_borders()

# Initialize the snake and apple
apple = Apple("#FF0000", random.randint(0, 19), random.randint(0, 19))
apple.draw()

snake = Snake("#810081", "#B130B1", 0, 19)
snake.direction = "right"
snake.draw()

# Display instructions
display_instructions()

# Keyboard bindings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")

# Start the game on screen click
screen.onscreenclick(start_game, 1)

screen.mainloop()
