menu = {
    1: "Right-Angled Triangle",
    2: "Pyramid",
    3: "Inverted Pyramid",
    4: "Diamond",
    5: "Number Pyramid",
    6: "Floyd's Triangle",
    7: "Multiplication Table",
    8: "Multiplication Table Grid",
    9: "Pascal's Triangle",
    0: "Exit"
}
TUPLE OF ALLOWED SYMBOLS
allowed_symbols = ("*", "#", "@", "$", "+")
allowed_set = set(allowed_symbols)
patterns_data = {}

def get_size():
    while True:
        try:
            size = int(input("Enter pattern size: "))
            if size > 0:
                return size
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid integer.")

def get_symbol():
    while True:
        symbol = input(
            f"Choose a symbol {allowed_symbols}: "
        )
        if len(symbol) == 1 and symbol in allowed_set:
            return symbol
        else:
            print("Invalid symbol. Choose from the allowed symbols.")

def right_triangle(n, symbol):
    result = []
    for i in range(1, n + 1):
        row = ""
        for j in range(i):
            row += symbol + " "
        result.append(row)
    return "\n".join(result)

def pyramid(n, symbol):
    result = []
    for i in range(1, n + 1):
        row = ""
        for j in range(n - i):
            row += " "
        for j in range(2 * i - 1):
            row += symbol
        result.append(row)
    return "\n".join(result)
    
def inverted_pyramid(n, symbol):
    result = []
    for i in range(n, 0, -1):
        row = ""
        for j in range(n - i):
            row += " "
        for j in range(2 * i - 1):
            row += symbol
        result.append(row)
    return "\n".join(result)

def diamond(n, symbol):
    result = []
    for i in range(1, n + 1):
        row = ""
        for j in range(n - i):
            row += " "
        for j in range(2 * i - 1):
            row += symbol
        result.append(row)

    for i in range(n - 1, 0, -1):
        row = ""
        for j in range(n - i):
            row += " "
        for j in range(2 * i - 1):
            row += symbol
        result.append(row)
    return "\n".join(result)
# NUMBER PATTERNS 
def number_pyramid(n):
    result = []
    for i in range(1, n + 1):
        row = ""
        for j in range(n - i):
            row += " "
        for j in range(1, i + 1):
            row += str(j)
        for j in range(i - 1, 0, -1):
            row += str(j)
        result.append(row)
    return "\n".join(result)

def floyd_triangle(n):
    result = []
    number = 1
    for i in range(1, n + 1):
        row = ""
        for j in range(i):
            row += str(number) + " "
            number += 1
        result.append(row)
    return "\n".join(result)
# RECURSION AND PASCAL'S TRIANGLE
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
def pascal_triangle(n):
    result = []
    for i in range(n):
        row = ""
        for j in range(n - i - 1):
            row += " "
        for j in range(i + 1):
            value = (
                factorial(i) //
                (factorial(j) * factorial(i - j))
            )
            row += str(value) + " "
        result.append(row)
    return "\n".join(result)
