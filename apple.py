import turtle
import random

class Apple(turtle.Turtle):
    def __init__(self, color, x_pos, y_pos):
        super().__init__()
        self.shape("circle")
        self.apple_color = color
        self.position = [x_pos, y_pos]

    def draw(self):
        self.clear()
        self.shape("circle")
        self.penup()
        self.color(self.apple_color)
        self.hideturtle()
        self.goto(-190 + self.position[0] * 20, 190 - self.position[1] * 20)
        self.stamp()

    def respawn(self, snake_tail, snake_head):
        while True:
            new_position = [random.randint(0, 19), random.randint(0, 19)]
            if new_position not in snake_tail and new_position != snake_head:
                self.position = new_position
                break
        self.draw()
