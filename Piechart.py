import matplotlib.pyplot as plt

# Data for programming languages and their popularity percentages
languages = ['Python', 'Java', 'JavaScript', 'C++', 'Ruby']
popularity = [40, 25, 15, 10, 10]

# Create the pie chart
plt.pie(popularity, labels=languages, autopct='%1.1f%%', startangle=90)

# Add a title
plt.title('Popular Programming Languages')

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
