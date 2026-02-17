import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True] # drives_right
cpc = [809, 731, 588, 18, 200, 70, 45] # cars_per_cap
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cars.index=row_labels

print(cars[1:4],'\n')
# Here we are slicing the DataFrame to get rows from index 1 to 3 (inclusive of 1 and exclusive of 4).

print(cars.loc["RU"],'\n')
print(cars.loc[["RU"]],'\n')

print(cars.loc[["AUS","MOR"], ["country","cars_per_cap"]],'\n')
#loc is used to access a group of rows and columns by labels or a boolean array.
# Here we are accessing the row with label "RU" which corresponds to Russia