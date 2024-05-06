# Arcade Game- Don't Get Caught
## CS110 Final Project - Spring 2024

## Team Members

Christopher Coon

***

## Project Description

The arcade game, Don't Get Caught, is an implementation of the classic arcade game Pac-Man using the Python module Pygame. Players control the white square (Runner) as he navigates through the red squares (Ghosts) avoiding capture. The game features various levels of increasing difficulty because the ghosts speed increases and they multiply. The ultimate goal is to achieve the highest score possible. When you get caught your score is saved until you beat it. Space Bar resets the game and arrow keys control the Runner.

***

## GUI Design

### Initial Design

![initial gui](assets/initial_gui.jpg)

### Final Design

![final gui](assets/final_gui.jpg)

## Program Design

### Features

1. Runner movement controlled by arrow keys.
2. Ghosts move randomly around the screen increasing in speed and multiplying over time, colliding with walls and avoiding other ghosts.
3. Survive against the time to gain points.
4. Clock and Score counter keep track of how long the Runner has avoided capture and the points they get for avoidance.
5. Ghosts multiply every 15 seconds.
6. Ghosts speed up every 20 seconds.
7. Player score increases by 100 points every 10 seconds.
8. Game over when Runner collides with a ghost and is captured.
9. Space Bar restarts the game.
10.Game runs at a 60 fps cap for smoother gameplay.

### Classes

- Player: Represents the player-controlled Pac-Man character.
- Ghost: Represents the non-player ghost characters.

## ATP

| Step                | Procedure                                | Expected Results                                 |
|---------------------|:----------------------------------------:|--------------------------------------------------|
| 1                   | Run the Arcade game main.py file         | Game window appears with Pac-Man and ghosts      |
| 2                   | Use arrow keys to move Runner            | Pac-Man moves around the screen                  |
| 3                   | Avoid collisions with ghosts             | Game continues if no collision occurs            |
| 4                   | Lose the game by colliding with a ghost  | Game over message appears                        |
| 5                   | Click anywhere on the screen             | Game window closes                               |