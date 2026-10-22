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

# Figure A: Solar flare intensity throughout 2000

# Convert the peak times into datetime values
times = pd.to_datetime(df['event_peaktime'])

# Extract the flare classifications
classes = df['fl_goescls'].astype(str).str.strip()

# Separate the class letter from the numerical magnitude
flare_type = classes.str[0].str.upper()
magnitude = pd.to_numeric(classes.str[1:], errors='coerce')

# Convert GOES flare classifications to peak X-ray flux (W/m^2)
class_flux = {
    'A': 1e-8,
    'B': 1e-7,
    'C': 1e-6,
    'M': 1e-5,
    'X': 1e-4 }

flux = flare_type.map(class_flux) * magnitude

# Keep only valid observations
valid = times.notna() & flux.notna() & (flux > 0)

# Plot Creation
plt.figure(figsize=(12, 5))
plt.scatter(times[valid], flux[valid], s=8, alpha=0.5)

plt.yscale('log')

plt.xlabel('Time of Peak (UTC)')
plt.ylabel('Peak X-ray Flux (W/m²)')
plt.title('GOES Solar Flare Intensity During 2000')
plt.grid(True, which='both', alpha=0.3)

plt.tight_layout()

# Save the figure in the same folder as project_I.py
plt.savefig(Path(__file__).resolve().parent / 'project_Ia.png', dpi=150)
plt.close()

