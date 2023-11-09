import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker

# Data for different countries and years (stored in a DataFrame)
data = {
    'Country': ['Germany', 'France', 'United Kingdom', 'Italy', 'United States', 'Spain', 'India'],
    '2020': [1320716, 1705971, 1737960, 1238072, 20905938, 1682047, 10286709],
    '2021': [5982758, 6728420, 8174319, 4327931, 47937834, 4000000, 34978292],
    '2022': [16125211, 17704169, 4088721, 9664174, 38468254, 3000000, 9729207],
    '2023': [14000000, 15000000, 3000000, 10000000, 1000000, 2000000, 1000000]
}

df = pd.DataFrame(data)

# Define the list of years
years = [2020, 2021, 2022, 2023]

# Create a line plot
plt.figure(figsize=(12, 6))

for i, row in df.iterrows():
    country = row['Country']
    y_data = [row[str(year)] / 1000000 for year in years]
    plt.plot(years, y_data, marker='o', label=country)

# Defining the axis and the titles
plt.xlabel('Year', fontsize=14)
plt.ylabel('Total Cases (M)', fontsize=14)
plt.title('COVID-19 Total Cases Over the Years (2020-2023)', fontsize=16)

# Add "M" as a unit to the y-axis numbers
ax = plt.gca()
formatter = ticker.StrMethodFormatter('{x:,.0f}M')
ax.yaxis.set_major_formatter(formatter)

# Setting the parameters
plt.xticks(years, fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)

plt.show()  # Showing the Final Results.
