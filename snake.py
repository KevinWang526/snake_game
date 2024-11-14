import turtle

class Snake(turtle.Turtle):
    def __init__(self, head_color, tail_color, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.head_color = head_color
        self.tail_color = tail_color
        self.score = 0
        self.position = [x_pos, y_pos]
        self.direction = "right"
        self.tail = []

    def draw(self):
        self.clear()
        self.shape("square")
        self.penup()
        self.color(self.head_color)
        self.hideturtle()
        self.goto(-190 + self.position[0] * 20, 190 - self.position[1] * 20)
        self.stamp()

        for pos in self.tail:
            self.color(self.tail_color)
            self.goto(-190 + pos[0] * 20, 190 - pos[1] * 20)
            self.stamp()

    def move(self):
        # Save the previous head position before moving
        previous_position = (self.position[0], self.position[1])

        # Update head position based on direction
        if self.direction == "up":
            self.position[1] -= 1
        elif self.direction == "down":
            self.position[1] += 1
        elif self.direction == "left":
            self.position[0] -= 1
        elif self.direction == "right":
            self.position[0] += 1

        # Update the tail with the previous head position
        if len(self.tail) >= 1:
            self.tail.insert(0, previous_position)
            self.tail.pop()

        self.draw()

    def grow(self):
        # Add the current head position to the tail as a new segment
        self.tail.append((self.position[0], self.position[1]))

    def is_off_screen(self):
        # Check if the snake has gone off the screen based on grid boundaries
        return self.position[0] < 0 or self.position[0] >= 20 or self.position[1] < 0 or self.position[1] >= 20

    def is_biting_tail(self):
        # Check if the head position matches any position in the tail
        return (self.position[0], self.position[1]) in self.tail
