# 🧠 PathFinder Puzzle

**PathFinder Puzzle** is a logic-based mini-game that challenges users to find a path from a start point to a goal across a customizable grid filled with obstacles. The game integrates a machine learning model that predicts puzzle difficulty based on player performance.

---

## 🚀 Project Description

- **Goal**: Create an interactive, stress-relieving game that sharpens critical thinking.
- **AI Component**: A `RandomForestClassifier` predicts puzzle difficulty level (`easy`, `medium`, `hard`) using the following features:
  - Grid size (`grid_rows`, `grid_cols`)
  - Number of obstacles
  - Path length
  - Number of turns
  - Time to solve

---

## 🕹️ Gameplay Instructions

- Click cells to add/remove obstacles.
- Click **Start Game** to begin solving.
- Click **End Game** to stop the timer and log results.
- Data is stored in `puzzle_data.csv`.

---

## 📊 Machine Learning Model

- **Model**: `RandomForestClassifier` with `stratify=y` for balanced class sampling
- **Features**: `grid_rows`, `grid_cols`, `num_obstacles`, `path_length`, `num_turns`, `time_to_solve`
- **Label**: `difficulty_label`
- **Accuracy**: ✅ 100% on current test set  
  

---

## 📌 Feature Importance (Top Predictors)

1. `time_to_solve` – most influential  
2. `num_obstacles`  
3. `num_turns`  
4. `path_length`  

---

## 📂 Files

- `pathfinder_game.py`: Streamlit game interface
- `puzzle_data.csv`: Collected game data (combined from all players)
- `PathFinder-Puzzel.ipynb`: Jupyter notebook with model training and testing
- `README.md`: This documentation

---

## 👨‍👩‍👧‍👦 Team Members

- Yaw Nimo-Agyare  
- Trevor Hitchcock  
- Kaylie Neal  
- Sahil Ghelani  

---

## 💡 The Three C's

- **Curiosity** – Encourages players to explore puzzle-building and strategy  
- **Connections** – Bridges game design, machine learning, and user behavior  
- **Creating Value** – Offers engaging gameplay and meaningful analytics

---

## ✅ Future Growth

- Auto-generate puzzles of varying shapes and sizes  
- Match puzzles to player skill level using the ML model  
- Expand with:
  - Multiplayer
  - Rankings
  - Daily challenges
  - Visualizations or path hints

---
