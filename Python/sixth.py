import numpy as np

h=[1.73, 1.68, 1.71, 1.89, 1.79]
height=np.array(h)
w=[65.4, 59.2, 63.6, 88.4, 68.7]
weight=np.array(w) # Create arrays from height and weight: np_height, np_weight
bmi=weight/height**2 # Calculate the BMI: bmi

print(bmi)
print(bmi>23) # Create a Boolean array where the condition is overweight: bmi_overweight
print(bmi[bmi>23]) # Print out the BMI values that are considered overweight
print(bmi[1]) # Print out the weight of the second person

numpy_array=np.array([1,2,3,4])
numpy_array=numpy_array+numpy_array
print(numpy_array) # Print the result of adding the array to itself

print(np.array([True, 1, 2]) + np.array([3, 4, False]) )
# Print the result of adding the Boolean array to the integer array

print(np.mean(bmi)) # Print the average of bmi

print(np.median(bmi)) # Print the median of bmi