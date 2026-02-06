num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

calc = input("""Input a character depending in what calculation you want to do:
x → Multiply
/ → Divide
+ → Add
- → Subtract
r → Squares

Your choice: """)

def sqrt(var1, rad):
    if rad < 0:
        return "Error: Cannot compute square root of a negative number."
    return var1 ** (1 / rad)

while calc not in ["x", "/", "+", "-", "r"]:
    print("Invalid operation selected. Please try again.")
    calc = input("""Input a character depending in what calculation you want to do: 
x → Multiply
/ → Divide 
+ → Add
- → Subtract
r → Squares
                 
Your choice: """)
    
if calc == "x":
    result = num1 * num2
    print(f"The result of {num1} x {num2} is {result}")
elif calc == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")
    else:
        print("Error: Division by zero is not allowed.")
elif calc == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")
elif calc == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")
else:
    result = sqrt(num1, num2)
    print(f"The square root of {num1} with radicand {num2} is {result}")

round_choice = input("Do you want to round the result? (y/n): ").lower()
if round_choice == "y":
    try:
        decimal_places = int(input("Enter the number of decimal places to round to: "))
        rounded_result = round(result, decimal_places)
        print(f"The rounded result is: {rounded_result}")
    except ValueError:
        print("Invalid input for decimal places. Please enter an integer.")

invalid_chars = ['á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú', 'ñ', 'Ñ', 'ü', 'Ü']

def autoreplace(char):
    replacements = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ñ': 'n', 'Ñ': 'N', 'ü': 'u', 'Ü': 'U'
    }
    return replacements.get(char, char)

def no_weirdos(string):
    for char in string:
        if char in invalid_chars:
            string = string.replace(char, autoreplace(char))
    return string

user_input = input("Enter a string: ")
cleaned_string = no_weirdos(user_input)
print("Cleaned string:", cleaned_string)