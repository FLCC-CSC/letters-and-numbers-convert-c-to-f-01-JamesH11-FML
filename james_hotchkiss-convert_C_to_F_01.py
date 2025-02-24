# FILE NAME - convert_C_to_F_01.py

# NAME: James Hotchkiss
# DATE: 02/24/2025
# BRIEF DESCRIPTION:  conversion function C->F



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience




    
# Don't forget to cast user input as a float!
    
########## ENTER YER CODE BELOW THIS LINE ##########
degree_sign = "\u00B0"
celcius = float(input("please provide the degrees of celcius: "))
find_fahrenheit = celcius * float(9/5) + 32

print(f'{find_fahrenheit}{degree_sign}F')








########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a temperature in Celsius: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: 1

1 degrees Celsius is 33.8 degrees Fahrenheit.

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does `float` mean?
float refers to a number with decimals, not a string(words)
and not a integer(whole numbers).




2. Why do you think it is important to use `float` as opposed to
   a different type of variable type?
float confirms with the python manager that your variable is
a number with decimals as apposed to
a string or an integer.




'''
