import matplotlib.pyplot as plt

# Years on the x-axis
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

# Popularity scores for each language
python_popularity = [30, 35, 40, 45, 50, 55, 60, 65, 70]
java_popularity = [40, 38, 45, 42, 48, 50, 55, 53, 58]
javascript_popularity = [50, 45, 55, 58, 60, 65, 70, 75, 80]
cpp_popularity = [25, 28, 30, 32, 35, 37, 40, 42, 45]

# Plotting the line graph
plt.plot(years, python_popularity, label='Python')
plt.plot(years, java_popularity, label='Java')
plt.plot(years, javascript_popularity, label='JavaScript')
plt.plot(years, cpp_popularity, label='C++')

# Adding labels and title
plt.xlabel('Years')
plt.ylabel('Popularity')
plt.title('Popularity of Programming Languages')

# Adding a legend
plt.legend()

# Displaying the graph
plt.show()
