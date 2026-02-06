def multiply(a, b):
    "Return the product of a and b."
    return a * b

if __name__ == "__main__":
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
    else:
        result = multiply(x, y)
        print(f"{x} * {y} = {result}")