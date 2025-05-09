🧠 PathFinder Puzzle
PathFinder Puzzle is a mini-game that combines logic-based gameplay with machine learning. The game challenges users to navigate from a starting point to a goal on a customizable grid filled with obstacles. Behind the scenes, an AI model evaluates each puzzle's difficulty based on how long it takes a user to solve it and other puzzle characteristics.

🚀 Project Description
Goal: Design an interactive puzzle game that helps relieve stress and engages users through brain-teasing challenges.

AI Component: A Random Forest machine learning model is trained to classify puzzles into difficulty levels (easy, medium, hard) based on gameplay data like:

Grid size

Number of obstacles

Path length

Number of turns

Time to solve

🕹️ Gameplay
Click cells on the grid to add/remove obstacles.

Use Start Game to begin solving.

Use End Game to stop the timer and let the AI analyze your path.

Data is saved locally as puzzle_data.csv.

📊 Machine Learning Model
The model uses RandomForestClassifier with stratify=y to ensure class balance during training.

Features: grid_rows, grid_cols, num_obstacles, path_length, num_turns, time_to_solve

Label: difficulty_label (easy, medium, hard)

Achieved 100% accuracy on test set (note: this may indicate overfitting given limited data)

📌 Feature Importance (Top Predictors):
time_to_solve – most influential

num_obstacles

num_turns

path_length

📂 Files
pathfinder_game.py: Streamlit game interface

puzzle_data.csv: Collected gameplay data (from you + team members)

PathFinder-Puzzel.ipynb: Jupyter Notebook for training/testing ML model and analyzing feature importance

README.md: Project documentation

👨‍👩‍👧‍👦 Team Members
Yaw Nimo-Agyare
(List your teammates and assign slides as per project requirement)

💡 The Three C’s
Curiosity: Encourages players to experiment with grid design and path planning

Connections: Bridges game design, data science, and teamwork

Creating Value: Demonstrates how a fun puzzle game can offer insights into difficulty modeling

✅ How This Game Can Grow
Can generate unlimited puzzles with varying sizes and shapes

Predictive difficulty helps match player skill level

Easy to expand with leaderboard, multiplayer, or adaptive challenges
