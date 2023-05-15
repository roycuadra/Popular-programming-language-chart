import matplotlib.pyplot as plt
import numpy as np

languages = ['Python', 'Java', 'JavaScript', 'C++', 'C#', 'Ruby', 'Swift', 'HTML/CSS']
counts = [5, 4, 6, 3, 2, 3, 1, 4]

colors = ['#00FF00', '#0000FF', '#FFFF00', '#800080', '#FF0000', '#FFA500', '#000000', '#FFFFFF']

# Generate a colormap based on the specified colors
cmap = plt.cm.colors.ListedColormap(colors)
bounds = np.arange(len(languages) + 1)
norm = plt.cm.colors.BoundaryNorm(bounds, cmap.N)
    
plt.bar(languages, counts, color=cmap(norm(range(len(languages)))))
plt.xlabel('Programming Languages')
plt.ylabel('Popularity')
plt.title('Popular Programming Languages')

# Create a colorbar legend
cbar = plt.colorbar(plt.cm.ScalarMappable(cmap=cmap, norm=norm), ticks=bounds[:-1])
cbar.set_ticklabels(languages)

plt.show()
