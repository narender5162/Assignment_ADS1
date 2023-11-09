# Importing the required Libraries
import matplotlib.pyplot as plt
import pandas as pd

# Data for population (stored in a DataFrame)
data = {
    'Gender': ['Males', 'Females'],
    'Population (millions)': [623.7, 586.5]
}
# Creating a Pandas Data-Frame
df = pd.DataFrame(data)

# Create a pie chart
labels = df['Gender']
sizes = df['Population (millions)']
colors = ['blue', 'pink']

# Setting Parameters
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Population Distribution by Gender in India (2011, Excluding Transgender)', fontsize=14)

plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.

plt.show()  # Showing the Final Results.
