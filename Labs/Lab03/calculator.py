
import math
# Lab 3

available_functions =  ['multiply', 'divide', 'add', 'subtract']

def check_allowed_function(operation):
    value = operation in available_functions
    return (value)

def get_inputs():
    operation = input("What is the operation? (enter q to quit)\n>>> ")
    operation = operation.lower()
    if(operation == 'q'):
        exit()

    if(not check_allowed_function(operation) ):
        raise NameError(f'Currently this calculator only supports {available_functions}')

    first_number = float(input("What is the first number? : "))
    second_number = float(input("What is the second number? : "))
    
    return (operation, first_number, second_number)



# Operations:
#   - add : +
#   - subtract : -
#   - multiply : *
#   - divide : /

def add(x, y):
    try:
        result = x + y
    except:
        raise ValueError
    finally:
        return (result)

def subtract(x, y):
    try:
        result = x - y
    except:
        raise ValueError
    finally:
        return (result)

def multiply(x, y):
    try:
        result = x * y
    except:
        raise ValueError
    finally:
        return (result)

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        result = 0;
    except TypeError as e:
        result = float(x) / float(y)
    except:
        raise ValueError
    finally:
        return (result)
      


# Prompt the user for
#   - the operation
#   - first number
#   - second number
# Display the result after each command.
def main():

   while(1):
    (operation, first_number, second_number) = get_inputs()

    if(operation == 'add'):
        result = add(first_number, second_number)
    elif (operation == 'subtract'):
        result = subtract(first_number, second_number)
    elif (operation == 'multiply'):
        result = multiply(first_number, second_number)
    elif (operation == 'divide'):
        result = divide(first_number, second_number)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
