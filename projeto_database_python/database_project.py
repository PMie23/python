import matplotlib                   # Matplotlib needs this import to visualize the graphs
matplotlib.use('Agg')

import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns

# Importing and learning about database

df = pd.read_csv(r"C:\Users\Isaac Tavares\Documents\MeuPC\python\projeto_database_python\student_habits_performance.csv")

# Data visualization

print(df)

# Which habits have the biggest impact on students performance?
# Filtering numeric columns
columns = [
    "study_hours_per_day",
    "social_media_hours",
    "netflix_hours",
    "sleep_hours",
    "attendance_percentage",
    "exercise_frequency",
    "mental_health_rating",
    "exam_score",
]
# Plot "heatmap"
plt.title("Correlation between habits and exam score")
plt.show()












