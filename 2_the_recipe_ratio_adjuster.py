#Task 1 Start

class PositiveServingError(Exception):
    """Exception raised if the original recipe or desred servings entered are zero or less"""
    pass

try:
    original_recipe = float(input("How many servings is the recipe originally for?: "))
    if original_recipe <= 0:
        raise PositiveServingError("Original Recipe can't call for zero or negative servings")
    print(f"The recipe calls for {original_recipe} servings")
except ValueError:
    print("Please enter in digits!")
try:
    servings_desired = float(input("How many servings of the recipe do you desire?: "))
    if servings_desired <= 0:
        raise PositiveServingError("Servings Desired cannot be zero or less")
    print(f"You would like to convert the recipe to make {servings_desired} servings")
except ValueError:
    print("Please enter in digits!")




'''
Task 1 works by assigning the user inputs of how many servings the original recipe will make and how many servings are desired to two variables after the inputs are converted to floats.
This happens in a try block so any non-numerical input will print an error message when the conversion fails and creates a ValueError. I also created a custom exception that will require users to enter a positive number greater than zero
for both desired and original quantities as you cannot make negative food in real life and a recipe would not yield zero food.
'''

#Task 2 Quantity Calculation

def adjustment_factor(original, desired):
    try:
        adjust_by = desired / original
        # return adjust_by
    except ZeroDivisionError:
        print("Original servings must be greater than zero")
    except TypeError:
        print("Servings must be digits, cannot divide by strings")
    else:
        print("The adjustment factor will be", str(adjust_by))
        print(f"This means you should multiply all ingredient quantities by {adjust_by} to yield proper portions")
    finally:
        print("Regardless of how much food you're trying to eat, enjoy the culinary process and the deliciuos reward!")

try:
    adjustment_factor(original_recipe, servings_desired)
except NameError:
    print("original_recipe and servings_desired cannot be string")
#print("The adjustment factor will be", str(adjustment_factor(original_recipe,servings_desired)))

'''
For Task 2 I created a function that would calculate the adjustment factor dividing the desired serving amount
by what the original recipe calls for. When executed successfully the function will return the variable adjust_by.
When the try block fails it will print that the original servings cannot be zero as it would create a ZeroDivisionError.
Additionally it would catch any TypeErrors as one cannot divide by strings. Honestly neither of these Errors should arise as the ValueError and custom PositiveServingError would arise first in Task 1.
Lastly I printed an introductory statement and called the function while converting it back into string so another type error does not arise. This conversion is not stored as it is in a print statement and not assigned
to a variable.
'''

#Task 3 Serving Success
'''For Task 3 I will be creating an else and finally block inside the earlier defined function adjustment_factor
I commented out the original print statement that called the function in Task 2 as well as the return statement in the try block
Then I added an else block with two print statements, one similarly to my original writing from Task 2 declaring what the adjustment factor would be
The second print statement was an f-string that clarified the adjustment factor is what you should multiply all ingredient quantities by to yield the right amount of food.
I added a finally block that would tell the user that regardless of how much food they ate to enjoy it! Lastly when debugging I encountered a name error when trying to check for my type error in the function adjustment_factor,
so when calling it I put the call in a try block, where I added a name error exception saying that the two input variables cannot be string.
'''