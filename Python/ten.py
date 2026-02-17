import matplotlib.pyplot as plt
 
year=[1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
pop=[2.5, 3.0, 3.7, 4.4, 5.3, 6.1, 6.9, 7.8]

year=[1800, 1850, 1900,]+year # Add more years to the list
pop=[1.0, 1.2, 1.6,]+pop # Add corresponding population values to the list


plt.plot(year, pop,marker='o') # Plot with circle markers
plt.xlabel('Year') # Label for x-axis
plt.ylabel('Population (billions)') # Label for y-axis  
plt.title('World Population Growth') # Title of the plot
plt.yticks([0, 2, 4, 6, 8], ['0B', '2B', '4B', '6B', '8B']) # Set y-axis ticks and labels
plt.grid() # Add grid lines to the plot

plt.show() # Display the plot

