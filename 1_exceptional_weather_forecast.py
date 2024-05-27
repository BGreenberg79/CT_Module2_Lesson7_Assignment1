#Task 1 Start

def temp_type_conversion(input_temp):
    try:
        converted_temp = int(input_temp)
        return converted_temp
    except ValueError:
        print("Please enter a valid integer or float for the temperature input")

temp_list = []
while True:
    user_temp = input("Please enter a temperature in Fahrenheit (when finished type 'done'): ")
    if user_temp == "done":
        break
    else:
        processed_temp = temp_type_conversion(user_temp)
        temp_list.append(processed_temp)
        
print("The temperatures added are: ")
for f_temp in temp_list:
    print(f"{f_temp} degrees Fahrenheit")

'''
This code works by defining a function that will try to convert the parameter of input temperature from string to interger and return that value unless an exception is raised where there is a value error
because the input characters are not digits. After that I intialize the empty list temp_list = [] and i create a while loop to to take input temperature, that is broken if the user input is 'done'
an else block follows where processed_temp is a vlue that is created to run our earlier defined temp_type_conversion function and that variable is then appended to our empty list.
Lastly a print statement and a for loop of f-strings will print each temperature from our list in fahrenheit.
'''

#Task 2 (and Task 3) Temperature Conversion

def f_to_c_conversion(*temps_to_convert):
    try:
        celsius_temps = []
        for temp in temps_to_convert:
            celsius = (int(temp) - 32) * 5/9
            celsius_temps.append(celsius)  
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("Temperature input must be an integer value")
    else:
        print("The temperature in celsius are:")
        for c_temp in celsius_temps:
            print(f"{c_temp} degrees Celsius")
    finally:
        print("Thank you for using our temperature conversion and weather forecast app!")


f_to_c_conversion(*temp_list)

# print("The temperature in celsius are:")

# for temp in temp_list:
#     celsius_temps.append(f_to_c_conversion(temp))
# for c_temp in celsius_temps:
#     print(f"{c_temp} degrees Celsius")

'''
For task 2 I defined a function for f_to_c_conversion where I applied the known formula to convert fahrenheit to celsius
and assigned it to the celsius variable which was then returned in the try block. I also created a type error exception if the user inputs a non integer value
and a zero division error exception in case somehow the user inds a way to divide by zero, while using the input.
I created a new empty list for celsius_temps and printed the list of celsius_temps by running two for loops.
The first for loop ran the function for each temp in the previous tasks temp list and then appended it to the empty celsius temps.
The second for loop printed each newly added result from that celsius_temps list in an f-string.
'''

#Task 3 User Experience
'''
For Task 3 I moved all of the print statements that I ran outside of the function into the function I deined in Task 2.
I also got rid of the return statement so the else and finally blocks can be executed. I initialized celius_list inside the function instead of trying to intialize it globally.
I also put a star in front of the parameter so I could call the function with temp_list as the argument also nullifying the need to reference temp_list as a global variable/list when defining the function.
I moved the append to celsius_list statement into the same for loop that defines celsius as a variable to ensure that each celsius conversion is stored and not lost for every input the user gives.
The else statement just ran the print statement for each celsius temperature value we recorded with a second for loop through celsius_list and f-strings. The finally block
thanks users for using the app regardless if they give valid input.
'''