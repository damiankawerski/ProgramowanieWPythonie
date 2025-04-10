import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the initial grid with a random pattern
grid_size = 100
grid = np.zeros((grid_size, grid_size))
grid = np.random.choice([0, 1], size=(grid_size, grid_size))

# Updatedatefine the update function for each generation
def evolve(frame_num, grid, grid_size):
    # Start your code here:
    # =====================


    height, width = grid.shape
    new_grid = np.zeros((height, width))
    neighbors = np.zeros((height, width))
    
    # Count the number of neighbors for each cell
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbors += np.roll(grid, shift=(i, j), axis=(0, 1))
            
    
    for i in range(0, height):
        for j in range(0, width):
            # Apply the rules of Conway's Game of Life
            if grid[i, j] == 1 and (neighbors[i, j] == 2 or neighbors[i, j] == 3):
                new_grid[i, j] = 1
            elif grid[i, j] == 0 and neighbors[i, j] == 3:
                new_grid[i, j] = 1


    grid[:] = new_grid[:]
    # =====================
    
    # Update the plot with the new grid
    mat.set_data(grid)
    return mat

# Set up the animation plot
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, evolve, frames=200, fargs=(grid, grid_size), interval=30)
plt.show()