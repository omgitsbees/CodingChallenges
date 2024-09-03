import tkinter as tk
import math

def evaluate_expression(expression: str) -> float:
    try:
        rpn_expr = shunting_yard(expression)
        result = evaluate_rpn(rpn_expr)
        return result
    except Exception as e:
        result_display.set(f"Error: {e}")
        return None

def shunting_yard(expression: str) -> list:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, 'sin': 3, 'cos': 3, 'tan': 3}
    output_queue = []
    operator_stack = []
    tokens = tokenize(expression)

    for token in tokens:
        if is_number(token):
            output_queue.append(token)
        elif token in precedence:
            while (operator_stack and operator_stack[-1] != '(' and
                   precedence.get(token, 0) <= precedence.get(operator_stack[-1], 0)):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()  # Pop the '('

    while operator_stack:
        output_queue.append(operator_stack.pop())

    return output_queue

def evaluate_rpn(rpn_expression: list) -> float:
    stack = []
    for token in rpn_expression:
        if is_number(token):
            stack.append(float(token))
        elif token in {'+', '-', '*', '/'}:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ValueError("Division by zero is not allowed.")
                stack.append(a / b)
        elif token in {'sin', 'cos', 'tan'}:
            a = stack.pop()
            if token == 'sin':
                stack.append(math.sin(a))
            elif token == 'cos':
                stack.append(math.cos(a))
            elif token == 'tan':
                stack.append(math.tan(a))
    return stack[0]

def tokenize(expression: str) -> list:
    tokens = []
    num = ''
    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isdigit() or char == '.':
            num += char
        else:
            if num:
                tokens.append(num)
                num = ''
            if char in {'+', '-', '*', '/', '(', ')'}:
                if char == '-' and (i == 0 or expression[i-1] in {'(', '+', '-', '*', '/'}):
                    num = '-'  # This handles negative numbers
                else:
                    tokens.append(char)
            elif char.isalpha():
                func = ''
                while i < len(expression) and expression[i].isalpha():
                    func += expression[i]
                    i += 1
                tokens.append(func)
                continue
        i += 1
    if num:
        tokens.append(num)
    return tokens

def is_number(token: str) -> bool:
    try:
        float(token)
        return True
    except ValueError:
        return False

def on_calculate():
    expression = expression_entry.get()
    result = evaluate_expression(expression)
    if result is not None:
        result_display.set(result)

# Set up the main window
root = tk.Tk()
root.title("Calculator")

# Set up the string variables for GUI elements
expression_entry = tk.Entry(root, width=40)
expression_entry.grid(row=0, column=0, padx=10, pady=10)

result_display = tk.StringVar()
result_label = tk.Label(root, textvariable=result_display, width=40, anchor='w')
result_label.grid(row=1, column=0, padx=10, pady=10)

# Set up the calculate button
calculate_button = tk.Button(root, text="Calculate", command=on_calculate)
calculate_button.grid(row=2, column=0, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
