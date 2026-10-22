import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Read a file created by data/download.py into a DataFrame
infile = Path(__file__).resolve().parent / 'data' / 'download.2000.csv'
print(f"Reading {infile}")
df = pd.read_csv(infile)

# Display the first few rows of the DataFrame
print(df.head())

# Extract only rows where the 4th column starts with "M" (r = reduced)
dfr = df[df.iloc[:, 3].astype(str).str.startswith('M')].copy()

# Remove the "X" from the start of the 4th column
dfr.loc[:, dfr.columns[3]] = dfr.iloc[:, 3].str.lstrip('M')

# Get unique values in the 4th column
unique_labels = pd.to_numeric(dfr.iloc[:, 3].unique())

# Convert the 4th column to numbers
dfr[dfr.columns[3]] = pd.to_numeric(dfr.iloc[:, 3])

# Convert the second column to datetime
dfr[dfr.columns[1]] = pd.to_datetime(dfr.iloc[:, 1])

# Display the first few rows of reduced data frame
print(dfr.head())

# Plot the 4th column vs the second column (timestamp)
plt.figure(figsize=(8.5, 11))
plt.plot(dfr.iloc[:, 1], dfr.iloc[:, 3], 'k.')
plt.yticks(unique_labels, fontsize=8)
plt.xlabel(r'Time of Peak [UTC] (event_peaktime)')
plt.ylabel('Classification')
plt.grid()
plt.title('GOES Event List M-Class Flares')
plt.savefig('project_I.png', dpi=300, bbox_inches='tight')

# ---------------------------------------------------------------------------------------- 
# Figure A: All solar flares during 2000

# Convert flare peak times to datetime values
times = pd.to_datetime(df['event_peaktime'])

# Convert flare classifications into numerical values
classes = df['fl_goescls'].astype(str)

# Use the first letter to identify each flare class
flare_type = classes.str[0]

# Assign each class a numerical position
class_levels = {'A': 0, 'B': 1, 'C': 2, 'M': 3, 'X': 4}
levels = flare_type.map(class_levels)

# Plot all recorded flare events
plt.figure(figsize=(12, 5))
plt.scatter(times, levels, s=5)

plt.yticks([0, 1, 2, 3, 4], ['A', 'B', 'C', 'M', 'X'])
plt.xlabel('Time of Peak (UTC)')
plt.ylabel('Solar Flare Class')
plt.title('GOES Solar Flare Events During 2000')
plt.grid(True)

plt.tight_layout()
plt.savefig('project/flares/project_Ia.png')
plt.close()

