# Snake Game

This Snake Game is a simple implementation of the classic Snake game using Python's Turtle Graphics library. The game allows the player to control a snake to collect apples, growing longer with each apple consumed. The objective is to avoid collisions with the walls or the snake's own tail.

## Table of Contents

- [Game Overview](#game-overview)
- [Files](#files)
  - [`main.py`](#mainpy)
  - [`snake.py`](#snakepy)
  - [`apple.py`](#applepy)
- [How to Run](#how-to-run)
- [Gameplay](#gameplay)
- [Improvements](#improvements)

---

## Game Overview

The player controls the snake using the arrow keys. The snake grows longer each time it reaches an apple, and the game ends if the snake either moves out of bounds or collides with its own tail. The player’s score is displayed in the console after each apple is collected. When the game ends, the Turtle Graphics window closes automatically.

## Files

### `main.py`

This file is the main entry point for the Snake Game. It initializes the game window and manages the core game loop, user input, and display.

- **Functions:**
  - `display_instructions()`: Displays the game's instructions in the console.
  - `draw_borders()`: Draws the boundary within which the snake can move.
  - `start_game(x, y)`: Main game loop. Handles the snake's movement, collision detection (walls and tail), and apple consumption. Ends the game when the snake dies by closing the Turtle Graphics window automatically.
  - `go_up()`, `go_down()`, `go_right()`, `go_left()`: Functions for changing the snake's direction based on keyboard input.

- **Setup:**
  - Initializes the screen, snake, and apple objects.
  - Defines keyboard bindings and starts the game loop upon screen click.

### `snake.py`

This file defines the `Snake` class, responsible for managing the snake's appearance, movement, and interactions.

- **Attributes:**
  - `head_color`, `tail_color`: Define the color of the snake’s head and tail segments.
  - `position`: Current position of the snake’s head.
  - `direction`: Direction in which the snake is moving.
  - `tail`: List of coordinates representing the snake’s tail segments.

- **Methods:**
  - `draw()`: Draws the snake on the screen, updating the head and tail positions.
  - `move()`: Updates the snake’s position based on its current direction, moves the tail, and calls `draw()` to refresh the snake on the screen.
  - `grow()`: Adds a new segment to the snake’s tail when it consumes an apple.
  - `is_off_screen()`: Checks if the snake’s head position is outside the game boundaries.
  - `is_biting_tail()`: Checks if the snake’s head has collided with one of its tail segments.

### `apple.py`

This file defines the `Apple` class, representing the apple object that the snake collects to gain points and grow.

- **Attributes:**
  - `apple_color`: Color of the apple.
  - `position`: Position of the apple on the game grid.

- **Methods:**
  - `draw()`: Draws the apple on the screen at its current position.
  - `respawn(snake_tail, snake_head)`: Generates a new position for the apple, ensuring it does not overlap with the snake's head or tail segments.

## How to Run

1. Make sure you have Python installed, along with the `turtle` and `random` libraries (which are included in Python's standard library).
2. Save all three files (`main.py`, `snake.py`, `apple.py`) in the same directory.
3. Run `main.py` to start the game.

```bash
python main.py
```

## Gameplay

- **Controls**: Use the arrow keys to change the snake’s direction.
- **Objective**: Guide the snake to the apple without hitting the boundaries or the snake’s tail.
- **End of Game**: The game ends when the snake hits a boundary or its own tail. The window closes automatically.

## Improvements

- Add a graphical score display in the game window instead of the console.
- Introduce difficulty levels by increasing the snake’s speed as it grows.
- Implement more game boundaries or obstacles within the game grid.
- Add sounds or visual effects when the snake consumes an apple or hits a boundary.

---

This game provides a solid base for understanding how to use Python's Turtle Graphics for interactive applications. Each file has a clear, focused role, making it easy to expand and improve. Happy coding!
