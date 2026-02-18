import numpy as np


# Task 1 — Generate and Inspect

np.random.seed(42)
scores = np.random.randint(50, 101, size=(5, 4))
print("Scores:\n", scores)
print("\nScore of 3rd student in 2nd subject:", scores[2, 1])
print("\nScores of last two students:\n", scores[-2:])
print("\nScores of first 3 students in subjects 2 and 3:")
print(scores[:3, 1:3])


# Task 2 — Broadcasting Analysis

col_mean = np.round(scores.mean(axis=0), 2)
print("\nColumn-wise mean:", col_mean)
curve = np.array([5, 3, 7, 2])
curved_scores = scores + curve
curved_scores = np.clip(curved_scores, 0, 100)   # ensure ≤100
print("\nCurved scores:\n", curved_scores)
row_max = curved_scores.max(axis=1)
print("\nRow-wise max (best score per student):", row_max)


# Task 3 — Normalize and Identify

row_min = curved_scores.min(axis=1).reshape(-1, 1)
row_max2 = curved_scores.max(axis=1).reshape(-1, 1)
normalized = (curved_scores - row_min) / (row_max2 - row_min)
print("\nNormalized scores:\n", normalized)
max_index_flat = np.argmax(normalized)
row_idx, col_idx = np.unravel_index(max_index_flat, normalized.shape)
print("\nHighest value located at: student", row_idx, "subject", col_idx)
above_90 = curved_scores[curved_scores > 90]
print("\nScores above 90:", above_90)
