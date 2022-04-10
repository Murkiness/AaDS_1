from stack_1 import Stack


def check_brackets(input_str):
    stack = Stack()

    for c in input_str:
        if c == "(":
            stack.push(c)
        elif c == ")" and stack.peek() is not None:
            stack.pop()
        else:
            return False

    return stack.size() == 0
