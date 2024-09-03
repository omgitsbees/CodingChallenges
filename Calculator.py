import math

def evaluate_expression(expression: str) -> float:
    try:
        # Convert the infix expression to postfix (RPN)
        rpn_expr = shunting_yard(expression)
        # Evaluate the RPN expression
        result = evaluate_rpn(rpn_expr)
        return result
    except Exception as e:
        print(f"Error evaluating expression: {e}")
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
                # To handle functions like sin, cos, tan
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

if __name__ == "__main__":
    # Test cases to demonstrate the calculator's capabilities
    test_expressions = [
        "1 + 2",                # Simple addition
        "2 - 1",                # Simple subtraction
        "2 * 3",                # Simple multiplication
        "3 / 2",                # Simple division
        "1 + 1 * 5",            # Operator precedence
        "( 1 + 1 ) * 5",        # Parentheses for grouping
        "10 / ( 6 - 1 )",       # Division with parentheses
        "sin ( 0 )",            # Sine function
        "cos ( 0 )",            # Cosine function
        "tan ( 0 )",            # Tangent function
        "1 + 2 * 3",            # Mix of addition and multiplication
        "( 1 + 2 ) * 3",        # Grouping with parentheses
        "2 + 3 * ( 2 - 1 ) / 4",# Complex expression
        "5 / 0",                # Division by zero (should raise an error)
        "-5 + 3",               # Negative numbers
        "2 * -3",               # Multiplication with a negative number
    ]
    
    for expr in test_expressions:
        result = evaluate_expression(expr)
        print(f"{expr} = {result}")
