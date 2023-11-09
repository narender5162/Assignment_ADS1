import matplotlib.pyplot as plt
import pandas as pd

# Data for different countries (stored in a DataFrame)
data = {
    'Country': [
        'China', 'India', 'Indonesia', 'Korea, Rep.', 'Saudi Arabia',
        'Turkiye', 'United Kingdom', 'United States',
        'Spain', 'France', 'Germany',
        'Italy', 'Japan', 'Russian Federation'
    ],
    'Population (millions)': [
        1371.9, 1307.2, 256.2, 50.7, 32.1, 78.1,
        64.6, 318.4, 46.7, 66.0, 80.9, 60.8, 127.1, 143.5
    ],
    'GDP (billions)': [
        10476, 2039, 891, 1484, 767, 939,
        3065, 17551, 1200, 2846, 3845, 2149, 4850, 2063
    ]
}

df = pd.DataFrame(data)

# Colors for each country
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'lime', 'purple',
          'orange', 'pink', 'gold', 'lightblue', 'brown']

# Create a scatter plot with legends and colors
plt.figure(figsize=(10, 6))

for i, row in df.iterrows():
    country = row['Country']
    population = row['Population (millions)']
    gdp = row['GDP (billions)']
    plt.scatter(population, gdp, marker='o', s=100, color=colors[i], label=country)

plt.title('Scatter Plot of GDP vs. Population (2014)')
plt.xlabel('Population (millions)')
plt.ylabel('GDP (billions)')
plt.grid(True)

# Customize the legend by specifying the number of columns
plt.legend(loc='upper left', ncol=1, fontsize=8)

plt.show()  # Showing the Final Results.
