
def __is_integer(some_string):
    try:
        int(some_string)
        return True
    except:
        return False


def compute(expression: str = None) -> int:
    stack = []
    for element in expression.split():
        if __is_integer(element):
            stack.append(int(element))
            continue

        second = stack.pop()
        first = stack.pop()
        if element == "+":
            stack.append(first + second)
        elif element == "-":
            stack.append(first - second)
        elif element == "*":
            stack.append(first * second)
        elif element == "/":
            stack.append(first / second)

    if len(stack) == 0:
        return 0
    else:
        return int(stack.pop())
