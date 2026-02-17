import matplotlib.pyplot as plt

values=[1,5,2,0,0.6,0.8,0.9,0.7,0.5,6,7,8,9] # Create a histogram with 3 bins
plt.hist(values, bins=3, edgecolor='black') # Add labels and title
plt.show() 
plt.clf()# Clear the current figure