#Task 1 Start

def temp_conversion(input_temp):
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
        processed_temp = temp_conversion(user_temp)
        temp_list.append(processed_temp)
        
print("The temperatures added are: ")
for item in temp_list:
    print(f"{item} degrees Fahrenheit")