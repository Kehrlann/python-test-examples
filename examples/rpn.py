
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
    elif len(stack) != 1:
        raise Exception(f"stack has more than one element left: {len(stack)} elements")
    else:
        return int(stack.pop())
