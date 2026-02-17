import matplotlib.pyplot as plt
 
year=[1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
pop=[2.5, 3.0, 3.7, 4.4, 5.3, 6.1, 6.9, 7.8]

plt.plot(year, pop,marker='o') # Plot with circle markers

plt.show() # Display the plot
plt.clf()# Clear the current figure

plt.scatter(year, pop,color='red') # Scatter plot with red points
plt.show() # Display the scatter plot


plt.scatter(year, pop)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

plt.show()