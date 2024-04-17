def to_fahrenheit(x):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        x (float): The temperature in Celsius.

    Returns:
        float: The temperature in Fahrenheit.
    """
    return (x * 9 / 5) + 32

def to_celicius(x):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        x (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature in Celsius.
    """
    return (x - 32) * 5 / 9 

print('FARENHEIT \t | CELCIUS')
for x in range(32,100,10):    
    print(f'Farenheit: {x}, Celcius: {to_celicius(x):.2f}')
print('CELCIUS \t | FARENHEIT')
for x in range(32,100,10):    
    print(f'Celcius: {x}, Farenheit: {to_fahrenheit(x):.2f}')

