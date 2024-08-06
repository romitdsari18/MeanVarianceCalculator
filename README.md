# MeanVarianceCalculator
This is the Python code that requests a non-negative integer from the user, computes the mean and variance based on the user input, and terminates the execution when user enter the negative number.

# Explaination

The FORMAT_STRING variable is set up as a string that will be used to format the output of the program to specify the number of decimal places to display for each value.

Three empty lists are created to store the input values, the mean values, and the variance values.

A while loop is used for taking the input from the user until they enter a negative number, and it will execute the break statement when the user enters the negative number. 

Inside the loop, the user's input is taken by using the print function and assigned to the variable n.

If the value of n is non-negative, it is added to the values list using the append method.

The length of the values list is stored in a variable l.

The mean of the values in values is calculated as the sum of the values divided by the length of the list and stored in the mean variable. The mean value is then added to the mean_list using the append method.

The sample variance of the values is calculated and stored in the variance variable. If there is only one value in the list, the variance is set to 0. Otherwise, the variance is calculated using a formula that involves the previous variance value in variance_list and the current mean value in mean_list.

The current mean and variance values are displayed to the user using the print function and the FORMAT_STRING.

This loop will continue until the user enter the negative number.
