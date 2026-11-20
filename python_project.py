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
def right_triangle(n, symbol):
    result = []
    for i in range(1, n + 1):
        row = ""
        for j in range(i):
            row += symbol + " "
        result.append(row)
    return "\n".join(result)
