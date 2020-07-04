# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 10:36:29 2020

@author: maksd
"""
# Spyder IDE, Python 3.7
# This is a working script for the Discussion forum assignment. You can run it, in case you want to get a short tasks answers. You can download the file from the attach or copy\paste all the text, before the Output line, to the clean script file. Don't use it in the interactive mode.
# I'm using escape characters; \n which forces printing to the new line and \"\", which allows to place parenthesises inside the text parameters(w3schools.com, n.d., par. 1).
# it adds readability to the result.
# Example 1:
# Define a function that takes an argument. Call the function. Identify what code is the argument and what code is the parameter.
print("Example 1:")
def argument_function(a): # This functions takes an argument and prints out the parameter.
    print(a) # The parameter is "a".
print("\nCalling the function with the parameter \"banana\".")
argument_function("\nbanana")
# Example 2:
# Call your function from Example 1 three times with different kinds of arguments: a value, a variable, and an expression. Identify which kind of argument is which. 
print("\nExample 2:")
somenumber = 44 # Assigning a value to the variable.
print("\nPassing a value \"5\" to the function:")
argument_function(5) # This represents an adding the value to the function.
print("\nPassing a variable \"somenumber = 44\" to the function:")
argument_function(somenumber) # This represents an adding the variable to a function.
print("\nPassing an expression \"Some text.\" to the function:")
argument_function("Some text.") # This represents an expression adding to the function.
# Example 3:
# Create a function with a local variable. Show what happens when you try to use that variable outside the function. Explain the results.
# I'll be using the try/except functions, which allows to prevent program termination in case of errors(w3schools.com, n.d., par. 1).
print("\nExample 3:")
def loc_var_function():
    local_variable = 13
print("\nTrying to call a local_variable from the function...")
try: # This block catches possible errors, in order to prevent program unexpected termination(w3schools.com, n.d., par. 1).
    print(local_variable) # Trying to access local_variable outside the function...
except: # This block catches any type of the exception. Program can work further, instead of termination(w3schools.com, n.d., par. 1).
        print("\nNameError: name 'local_variable' is not defined")
        print("\nWe cannot call the local_varialbe outside of the function, because it exists only while the function call!")
# We cannot call local varialbe outside the function, it's exists only at the moment of function runing.
        
# Example 4:  
# Create a function that takes an argument. Give the function parameter a unique name. 
# Show what happens when you try to use that parameter name outside the function. Explain the results.
print("\nExample 4:")
def some_regular_function(a): # This functions takes an argument.
    banana_unique_variable = a       # Assigning a placeholder to the banana_unique_variable. 
print("\nTrying to call a local variable, with the unique name, from the function...")
try: # This block cathes possible errors, in order to prevent program unexpected termination(w3schools.com, n.d., par. 1).
    print(banana_unique_variable)
except: # This block catches any type of the exception. Program can work further, instead of termination(w3schools.com, n.d., par. 1).
    print("\nNameError: name 'banana_unique_variable' is not defined")
    print("\nWe cannot call the Local varialbe outside of a function, even though it has the unique name, because it exists only while the function call!!")
# Example 5:
# Show what happens when a variable defined outside a function has the same name as a local variable inside a function. Explain what happens to the value of each variable as the program runs.
print("\nExample 5:")
def some_function(): # The Void function with a local variable inside.
	the_same_name_variable = "Local variable" 
the_same_name_variable = "Global variable"
print(the_same_name_variable)
print("\nThere will be only the Global variable shown, even though Local and Global variables have the same name, the Local varibale exists only inside of the function, while the function call.")
    
    
    
# W3schools.com. (n.d.). Python Escape Characters. Retrieved June 30, 2020, from https://www.w3schools.com/python/gloss_python_escape_characters.asp
# W3schools.com. (n.d.). Python Try Except. Retrieved June 30, 2020, from https://www.w3schools.com/python/python_try_except.asp