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

# Plot C as a function of F (C(F))
plt.figure(figsize=(8, 5))
plt.plot(df["F"], df["C"], color="red", linestyle="--", marker="o", markersize=4)
plt.xlabel("F")
plt.ylabel("C")
plt.title("C as a function of F")
plt.grid(True)
plt.tight_layout()

# Export pdf of the plot (must be before plt.show())
output_pdf_path = csv_path.with_suffix(".pdf")
plt.savefig(output_pdf_path)
print(f"Plot saved to {output_pdf_path}")

plt.show()

# verify the output file exists
if not output_pdf_path.exists():
    raise FileNotFoundError(f"Failed to create output file: {output_pdf_path}") 
else:
    print(f"Output file verified: {output_pdf_path}")   



