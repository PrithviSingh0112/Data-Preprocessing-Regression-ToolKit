import pandas as pd
import random

# Define the original positions
positions = [
    ("Business Analyst", 1, 45000),
    ("Junior Consultant", 2, 50000),
    ("Senior Consultant", 3, 60000),
    ("Manager", 4, 80000),
    ("Country Manager", 5, 110000),
    ("Region Manager", 6, 150000),
    ("Partner", 7, 200000),
    ("Senior Partner", 8, 300000),
    ("C-level", 9, 500000),
    ("CEO", 10, 1000000)
]

# Create 250 random entries
random_entries = [random.choice(positions) for _ in range(250)]

# Create DataFrame
df = pd.DataFrame(random_entries, columns=["Position", "Level", "Salary"])

# Save to CSV
df.to_csv("random_salary_data.csv", index=False)

print(df.head())