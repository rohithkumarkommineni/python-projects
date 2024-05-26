### Pong Game Project

This project is a Python implementation of the classic Pong game using the Turtle graphics library. The game simulates the traditional Pong experience with a ball, paddles, and a scoreboard to track the points.

#### File Overview

1. **ball.py**
   - **Class:** `Ball`
   - **Description:** This class extends the Turtle class to represent the ball in the Pong game. It initializes the ball's shape, color, and movement attributes. The ball can move, bounce off walls and paddles, and reset its position.
   - **Key Methods:**
     - `move()`: Updates the ball's position based on its current movement vector.
     - `bounce_y()`: Reverses the ball's vertical direction.
     - `bounce_x()`: Reverses the ball's horizontal direction and increases its speed.
     - `refresh()`: Resets the ball to the center of the screen and reverses its horizontal direction.

2. **main.py**
   - **Purpose:** This is the main script that sets up the game environment and runs the game loop.
   - **Functionality:**
     - Initializes the screen with a black background and sets up the paddles, ball, and scoreboard.
     - Handles user input for paddle movements.
     - Contains the game loop that updates the game state, including ball movement, collision detection, and score updates.
     - Ends the game loop when the user closes the window.

3. **paddle.py**
   - **Class:** `Paddle`
   - **Description:** This class extends the Turtle class to represent a paddle in the Pong game. It initializes the paddle's shape, color, and position. The paddle can move up and down in response to user input.
   - **Key Methods:**
     - `move_up()`: Moves the paddle up by a fixed amount.
     - `move_down()`: Moves the paddle down by a fixed amount.

4. **scoreboard.py**
   - **Class:** `Scoreboard`
   - **Description:** This class extends the Turtle class to manage and display the score in the Pong game. It keeps track of the scores for both players and updates the display accordingly.
   - **Key Methods:**
     - `update_score()`: Clears the previous score and displays the current scores.
     - `r_point()`: Increments the right player's score and updates the display.
     - `l_point()`: Increments the left player's score and updates the display.

#### How to Play
1. **Setup:**
   - Run the `main.py` script to start the game.
2. **Controls:**
   - Use the "Up" and "Down" arrow keys to move the right paddle.
   - Use the "W" and "S" keys to move the left paddle.
3. **Objective:**
   - Each player aims to prevent the ball from passing their paddle while trying to make the ball pass the opponent's paddle.
   - The scoreboard keeps track of points, awarding a point to a player each time the opponent misses the ball.

This project demonstrates basic game development concepts using Python's Turtle graphics library, including animation, collision detection, and user input handling.
