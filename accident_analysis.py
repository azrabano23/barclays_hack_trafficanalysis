
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv("your_accident_data.csv")  # Replace with your file path

# Optional: Parse datetime if needed
# df['crash_time'] = pd.to_datetime(df['crash_time_column'])

### --- TIME ANALYSIS ---

# Extract hour from time column
df['hour'] = pd.to_datetime(df['crash_time']).dt.hour
df['period'] = pd.cut(df['hour'],
                      bins=[0, 6, 12, 18, 24],
                      labels=['12AM–6AM', '6AM–12PM', '12PM–6PM', '6PM–12AM'],
                      right=False)

# Plot crashes by hour
plt.figure(figsize=(10, 6))
sns.countplot(x='hour', data=df, palette='coolwarm')
plt.title("Crashes by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Crashes")
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot crash distribution by time period
plt.figure(figsize=(6, 4))
df['period'].value_counts(sort=False).plot(kind='bar', color='salmon', edgecolor='black')
plt.title("Crashes by Time Period")
plt.xlabel("Time Period")
plt.ylabel("Number of Crashes")
plt.tight_layout()
plt.show()

### --- DAY ANALYSIS ---

# Extract weekday
df['weekday'] = pd.to_datetime(df['crash_date']).dt.day_name()

plt.figure(figsize=(8, 5))
sns.countplot(x='weekday', data=df,
              order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
              palette='magma')
plt.title("Crashes by Day of the Week")
plt.xlabel("Day")
plt.ylabel("Number of Crashes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

### --- MONTH ANALYSIS ---

# Extract month
df['month'] = pd.to_datetime(df['crash_date']).dt.month_name()

plt.figure(figsize=(10, 6))
sns.countplot(x='month', data=df,
              order=['January', 'February', 'March', 'April', 'May', 'June',
                     'July', 'August', 'September', 'October', 'November', 'December'],
              palette='viridis')
plt.title("Crashes by Month")
plt.xlabel("Month")
plt.ylabel("Number of Crashes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

### --- WEATHER & LIGHT CONDITION ANALYSIS (Optional) ---

# Only run if you have columns like 'weather' and 'light_condition'
if 'weather' in df.columns and 'light_condition' in df.columns:
    plt.figure(figsize=(12, 5))
    sns.countplot(x='weather', data=df, order=df['weather'].value_counts().index, palette='pastel')
    plt.title("Crashes by Weather Condition")
    plt.xlabel("Weather")
    plt.ylabel("Number of Crashes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    sns.countplot(x='light_condition', data=df, order=df['light_condition'].value_counts().index, palette='muted')
    plt.title("Crashes by Light Condition")
    plt.xlabel("Lighting")
    plt.ylabel("Number of Crashes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
