def calculate(a: float, b: float, operation: str):
    if operation == 'add':
        return a + b
    elif operation == 'sub':
        return a - b
    elif operation == 'mul':
        return a * b
    elif operation == 'div':
        if b == 0:
            raise ValueError('Cannot divide by zero')
        return a / b
    else:
        raise ValueError('Unknown operation')
