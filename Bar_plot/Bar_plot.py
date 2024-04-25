import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Replace 'your_excel_file.xlsx' with the actual path to your Excel file
excel_file = 'Your_data.xlsx'

# Read Excel file into a DataFrame, specifying the first row as the header
df = pd.read_excel(excel_file)

# Extracting data from the DataFrame
titles = df['Title']
half_time_values = df['fluorescence']
stdev_values = df['stdev']

# Create positions for the bars
bar_width = 0.7
bar_positions = np.arange(len(titles))

# Plotting grouped bar plot with error bars
fig, ax = plt.subplots(figsize=(4, 6))  # Adjust the figure size as needed
ax.bar(bar_positions - bar_width/2, half_time_values, width=bar_width, yerr=stdev_values, capsize=5, color='skyblue', label='Half-Time Values', alpha=0.7)

ax.set_xlabel('Titles')
ax.set_ylabel('Fluorescence')
ax.set_title('Calcium Concentration - Half-Time Values with Error Bars')
ax.legend()

# Rotate x-axis labels for better readability
plt.xticks(bar_positions, titles, rotation=45, ha='right')

# Adjust layout to prevent clipping of x-axis labels
plt.tight_layout()

# Save the plot to a PDF file
plt.savefig('Your_data.pdf')

# Show the plot
plt.show()
