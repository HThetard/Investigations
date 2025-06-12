import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import CSV
df = pd.read_csv("data.csv")

# Preview the data
#print(df.head())

# Create data frame

df['TIME_PERIOD_ADJUSTED'] = pd.to_datetime(df['TIME_PERIOD_ADJUSTED'])

# Filter for observations from 1970-01-01 onwards
df_filtered = df[df['TIME_PERIOD_ADJUSTED'] >= '2000-01-01']

print(df_filtered)

sns.set_theme(style='whitegrid')

# Plot OBS_VALUE over TIME_PERIOD_ADJUSTED, colored by country (REF_AREA)
plt.figure(figsize=(14, 7))
sns.lineplot(data=df_filtered, x='TIME_PERIOD_ADJUSTED', y='OBS_VALUE', hue='REF_AREA', marker='o')

plt.title('ECB RESR: OBS_VALUE Over Time by Country', fontsize=16)
plt.xlabel('Time Period')
plt.ylabel('Observation Value (OBS_VALUE)')
plt.xticks(rotation=45)
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')  # Place legend outside plot
plt.tight_layout()
plt.show()

# Show all unique countries in the data
#print(df['REF_AREA'].unique())
