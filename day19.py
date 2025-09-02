def evaluate_postfix(expression: str) -> int:
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
            else:
                raise ValueError(f"Unsupported operator: {token}")

    return stack[0]
