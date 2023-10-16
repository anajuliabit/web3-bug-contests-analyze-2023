import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('results/contests.csv', delimiter=',').iloc[:-1]

# Remove any leading/trailing whitespaces from column names and values
data.columns = data.columns.str.strip()
data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Group by 'CATEGORY' and calculate sum of 'BOUNTY', mean of 'PARTICIPANTS', and sum of 'HRF'
grouped_data = data.groupby('CATEGORY').agg(
    AVG_BOBUNTY=pd.NamedAgg(column='BOUNTY', aggfunc='mean'),
    AVG_PARTICIPANTS=pd.NamedAgg(column='PARTICIPANTS', aggfunc='mean'),
    TOTAL_HRF=pd.NamedAgg(column='HRF', aggfunc='sum')
).reset_index()

# Sort the data for better visualization
grouped_data = grouped_data.sort_values(by='AVG_BOBUNTY', ascending=False)

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar plot for Avg Bounty Amount
bars = ax1.bar(grouped_data['CATEGORY'], grouped_data['AVG_BOBUNTY'], color='skyblue', label='Avg Bounty Amount')
ax1.set_xticks(range(len(grouped_data['CATEGORY'])))  # Set the x-ticks positions
ax1.set_xticklabels(grouped_data['CATEGORY'], rotation=75, fontsize=10)  # Set the labels, rotation, and fontsize
ax1.set_xlabel('Category')
ax1.set_ylabel('Avg Bounty Amount', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Line plot for Average Participants on a second y-axis
ax2 = ax1.twinx()
lines = ax2.plot(grouped_data['CATEGORY'], grouped_data['AVG_PARTICIPANTS'], color='tab:red', marker='o', label='Avg Participants')
ax2.set_ylabel('Avg Participants', color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Line plot for Total HRF on a third y-axis
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))  # Move the right spine outward to make room for the third y-axis
lines2 = ax3.plot(grouped_data['CATEGORY'], grouped_data['TOTAL_HRF'], color='tab:green', marker='s', linestyle='--', label='Total HRF')
ax3.set_ylabel('Total HRF', color='tab:green')
ax3.tick_params(axis='y', labelcolor='tab:green')

# Title and legend
plt.title('Bounty Amount, Avg Participants, and Total HRF per Category')
fig.tight_layout()
fig.legend(loc="upper left", bbox_to_anchor=(0.1,0.9))

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Save the figure to a file
plt.savefig('results/output.png', bbox_inches='tight')

plt.show()  # This line is optional if you just want to save the figure without displaying it
