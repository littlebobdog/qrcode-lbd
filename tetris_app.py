import streamlit as st
import numpy as np
import time
import random

# Tetris settings
GRID_WIDTH = 10
GRID_HEIGHT = 20

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]

# Initialize grid
grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)

# Initialize variables
current_shape = random.choice(SHAPES)
current_position = [0, GRID_WIDTH // 2 - len(current_shape[0]) // 2]

def check_collision(shape, position):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                if (i + position[0] >= GRID_HEIGHT or
                    j + position[1] < 0 or
                    j + position[1] >= GRID_WIDTH or
                    grid[i + position[0], j + position[1]]):
                    return True
    return False

def place_shape(shape, position):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                grid[i + position[0], j + position[1]] = cell

def remove_full_lines():
    global grid
    new_grid = [row for row in grid if not all(row)]
    lines_removed = GRID_HEIGHT - len(new_grid)
    new_grid = [[0] * GRID_WIDTH for _ in range(lines_removed)] + new_grid
    grid = np.array(new_grid)

# Streamlit interface
st.title("Tetris Game")

start_button = st.button("Start")

if start_button:
    while True:
        st.write(grid)
        time.sleep(0.5)
        new_position = [current_position[0] + 1, current_position[1]]
        if check_collision(current_shape, new_position):
            place_shape(current_shape, current_position)
            remove_full_lines()
            current_shape = random.choice(SHAPES)
            current_position = [0, GRID_WIDTH // 2 - len(current_shape[0]) // 2]
            if check_collision(current_shape, current_position):
                st.write("Game Over!")
                break
        else:
            current_position = new_position
        st.write(grid)
