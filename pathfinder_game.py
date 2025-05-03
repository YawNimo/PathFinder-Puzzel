import streamlit as st
import numpy as np
import time
from collections import deque
import csv
import os

# -------------------------------
# BFS Solver to find shortest path
def bfs_solver(grid, start, end):
    rows, cols = grid.shape
    visited = set()
    queue = deque()
    queue.append((start, [start]))  # (current_position, path)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols and
                grid[nx, ny] == 0 and (nx, ny) not in visited):
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None  # No path found

# -------------------------------
# Count direction changes in path
def count_turns(path):
    if not path or len(path) < 3:
        return 0

    turns = 0
    for i in range(2, len(path)):
        x1, y1 = path[i-2]
        x2, y2 = path[i-1]
        x3, y3 = path[i]
        dir1 = (x2 - x1, y2 - y1)
        dir2 = (x3 - x2, y3 - y2)
        if dir1 != dir2:
            turns += 1
    return turns

# -------------------------------
# Streamlit App Starts
st.set_page_config(page_title="Pathfinder Puzzle", layout="centered")

ROWS = st.sidebar.slider("Grid Rows", 4, 10, 5)
COLS = st.sidebar.slider("Grid Columns", 4, 10, 5)

# Game state setup
if "grid" not in st.session_state:
    st.session_state.grid = np.zeros((ROWS, COLS), dtype=int)
    st.session_state.start_time = None
    st.session_state.start_pos = (0, 0)
    st.session_state.end_pos = (ROWS - 1, COLS - 1)
    st.session_state.player_path = []

st.title("🧠 Pathfinder Puzzle")
st.write("Click cells to toggle obstacles. Then click **Start Game** to solve the path.")

# Draw the grid with buttons
for i in range(ROWS):
    cols = st.columns(COLS)
    for j in range(COLS):
        label = f"{i},{j}"
        cell = st.session_state.grid[i, j]

        # Show AI path in blue if solved
        if (i, j) in st.session_state.get("player_path", []):
            btn_label = "🟦"
        elif (i, j) == st.session_state.start_pos:
            btn_label = "🟢"
        elif (i, j) == st.session_state.end_pos:
            btn_label = "🔴"
        elif cell == 1:
            btn_label = "⬛"
        else:
            btn_label = "⬜"

        if cols[j].button(btn_label, key=label):
            if (i, j) not in [st.session_state.start_pos, st.session_state.end_pos]:
                st.session_state.grid[i, j] = 1 - cell  # Toggle obstacle

# Reset grid button
st.button("Reset Grid", on_click=lambda: st.session_state.update({
    "grid": np.zeros((ROWS, COLS), dtype=int),
    "player_path": []
}))

# Start timer
if st.button("Start Game"):
    st.session_state.start_time = time.time()
    st.success("Game started! Navigate mentally and then click 'End Game' when done.")

# End game and run BFS
if st.button("End Game"):
    if st.session_state.start_time:
        time_taken = time.time() - st.session_state.start_time
        st.info(f"Time to solve: {time_taken:.2f} seconds")

        path = bfs_solver(st.session_state.grid, st.session_state.start_pos, st.session_state.end_pos)
        st.session_state.player_path = path if path else []

        st.experimental_rerun()  # 👈 force redraw so 🟦 appears right away

        if path:
            path_length = len(path)
            num_turns = count_turns(path)
            st.success("✅ Path found!")
            st.write(f"Path length: {path_length} steps")
            st.write(f"Number of turns: {num_turns}")
            st.text(f"Path: {path}")

            # Log puzzle data
            num_obstacles = int(np.sum(st.session_state.grid))
            difficulty = "easy" if time_taken <= 15 else "medium" if time_taken <= 30 else "hard"

            data = {
                "grid_rows": ROWS,
                "grid_cols": COLS,
                "num_obstacles": num_obstacles,
                "path_length": path_length,
                "num_turns": num_turns,
                "time_to_solve": round(time_taken, 2),
                "difficulty_label": difficulty
            }

            csv_file = "puzzle_data.csv"
            file_exists = os.path.isfile(csv_file)

            with open(csv_file, mode="a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=data.keys())
                if not file_exists:
                    writer.writeheader()
                writer.writerow(data)

            st.success("📝 Puzzle data saved to CSV!")
        else:
            st.error("❌ No path found. This puzzle is unsolvable.")
            st.session_state.player_path = []

# Show obstacle grid
st.write("Obstacle Grid (1 = blocked):")
st.dataframe(st.session_state.grid)
