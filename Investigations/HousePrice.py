import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import CSV
df = pd.read_csv("data.csv")

# Preview the data
#print(df.head())

# Create data frame

#df['TIME_PERIOD_ADJUSTED'] = pd.to_datetime(df['TIME_PERIOD_ADJUSTED'])

#df_converted = df[pd.to_datetime(df['TIME_PERIOD_ADJUSTED'], format='%Y')].str[4:]

# Filter for observations from 1970-01-01 onwards
#df_filtered = df[df['TIME_PERIOD_ADJUSTED'] > '2000']
df['TIME_PERIOD_ADJUSTED']  = df['TIME_PERIOD_ADJUSTED'] 


#print(df['TIME_PERIOD_ADJUSTED'])
#print(df_converted)
#print(df_filtered['TIME_PERIOD_ADJUSTED'])

#print(df['TIME_PERIOD_ADJUSTED'].min(), df['TIME_PERIOD_ADJUSTED'].max())

#print(df_filtered.shape) 

sns.set_theme(style='whitegrid')

# Plot OBS_VALUE over TIME_PERIOD
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='TIME_PERIOD_ADJUSTED', y='OBS_VALUE', marker='o')

plt.title('ECB RESR: OBS_VALUE Over Time (All Countries)', fontsize=14)
plt.xlabel('Time Period')
plt.ylabel('Observation Value (OBS_VALUE)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print(df['REF_AREA'].unique())