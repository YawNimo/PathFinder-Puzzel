
import streamlit as st
import numpy as np
import time

st.set_page_config(page_title="Pathfinder Puzzle", layout="centered")

ROWS = st.sidebar.slider("Grid Rows", 4, 10, 5)
COLS = st.sidebar.slider("Grid Columns", 4, 10, 5)

# Setting the game state
if "grid" not in st.session_state:
    st.session_state.grid = np.zeros((ROWS, COLS), dtype=int)
    st.session_state.start_time = None
    st.session_state.start_pos = (0, 0)
    st.session_state.end_pos = (ROWS - 1, COLS - 1)
    st.session_state.player_path = []

st.title("🧠 Pathfinder Puzzle")
st.write("Click cells to toggle obstacles. Then click **Start Game** to solve the path.")

# Drawing the grid with buttons
for i in range(ROWS):
    cols = st.columns(COLS)
    for j in range(COLS):
        label = f"{i},{j}"
        cell = st.session_state.grid[i, j]

        btn_label = "⬛" if cell == 1 else "⬜"
        if (i, j) == st.session_state.start_pos:
            btn_label = "🟢"
        elif (i, j) == st.session_state.end_pos:
            btn_label = "🔴"

        if cols[j].button(btn_label, key=label):
            if (i, j) not in [st.session_state.start_pos, st.session_state.end_pos]:
                st.session_state.grid[i, j] = 1 - cell  # Toggle obstacle

st.button("Reset Grid", on_click=lambda: st.session_state.update({"grid": np.zeros((ROWS, COLS), dtype=int)}))

if st.button("Start Game"):
    st.session_state.start_time = time.time()
    st.success("Game started! Navigate mentally and then click 'End Game' when done.")

if st.button("End Game"):
    if st.session_state.start_time:
        time_taken = time.time() - st.session_state.start_time
        st.info(f"Time to solve: {time_taken:.2f} seconds")
       

st.write("Obstacle Grid (1 = blocked):")
st.dataframe(st.session_state.grid)
