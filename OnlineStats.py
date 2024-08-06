# -*- coding: utf-8 -*-

# Setting up the format string to display the required number of mean and variance
FORMAT_STRING = "Mean is %.2f and Variance is %.12g"

# Initializing the empty lists for storing input values, mean, and variance
values = []
mean_list = []
variance_list = []

# Asking for user input until a negative number is entered
while True:
    n = float(input("Enter a number: "))
    if n < 0:
        break
    
    # Adding the user input to the list of values
    values.append(n)
    
    # Calculating the mean of the values
    l = len(values)
    mean = sum(values) / l
    mean_list.append(mean)
    
    # Calculating the sample variance of the values
    if l == 1:
        variance = 0 
    else:
       variance =(((l-2)/(l-1))*variance_list[l-2]) + ((values[l-1]-mean_list[l-2])**2 / (l))
    variance_list.append(variance)
     
    # Displaying the current mean and variance by using the format string
    print(FORMAT_STRING % (mean, variance))
    
# End of program
