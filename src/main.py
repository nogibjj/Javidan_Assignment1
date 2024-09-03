def add_two_numbers(num1, num2):
    if not (isinstance(num1, int) or isinstance(num1, float)) or not (isinstance(num2, int) or isinstance(num2, float)):
        raise ValueError("Number are not correct")

    return num1 + num2

