import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Path to the CSV in this directory
csv_path = Path(__file__).with_name("SIGNAL.csv")

# Load the data; skip metadata lines and keep only the columns we plot
df = pd.read_csv(
    csv_path,
    comment="#",  # ignore instrument metadata lines
    usecols=["C", "F"],  # ignore trailing empty/stat columns
)

# Ensure required columns exist
for col in ("C", "F"):
    if col not in df.columns:
        raise ValueError(f"Missing column '{col}' in {csv_path}")

# Plot C vs F
plt.figure(figsize=(8, 5))
plt.plot(df["C"], df["F"], marker="o", linestyle="-", color="steelblue")
plt.xlabel("C")
plt.ylabel("F")
plt.title("C vs F")
plt.grid(True)
plt.tight_layout()
plt.show()
