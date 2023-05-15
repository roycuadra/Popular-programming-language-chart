import matplotlib.pyplot as plt

# Data for programming languages and their popularity percentages
languages = ['Python', 'Java', 'JavaScript', 'C++', 'Ruby']
popularity = [40, 25, 15, 10, 10]

# Create the boxplot
plt.boxplot(popularity)

# Customize the plot
plt.xticks([1], [', '.join(languages)])  # Show the programming language names on x-axis
plt.ylabel('Popularity Percentage')
plt.title('Popular Programming Languages')

# Display the plot
plt.show()
