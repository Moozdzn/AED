from Stack import Stack
# from InfixToPostfix import infixToPostfix

def postfix_eval(expression):
    operand_stack = Stack()
    list = []
    output = []
    list = expression.split()
    for char in list:
        if char in '0123456789':
            operand_stack.push(int(char))
        elif char in '-*/+^':
            number_two = operand_stack.pop()
            number_one = operand_stack.pop()
            result = math(char,number_one,number_two)
            operand_stack.push(result)
        else:
            operand_stack.push(float(char))
        print(operand_stack)
    return operand_stack.pop()

def math(operator, operand1,operand2):
    if operator == '*':
        return float(operand1 * operand2)
    elif operator == '/':
        return float(operand1 / operand2)
    elif operator == '+':
        return float(operand1 + operand2)
    elif operator == '^':
        return float(operand1 ** operand2)
    else:
        return float(operand1 - operand2)

def main():
    postfix_eval('4.4 4.6 + 2 1 3 + / ^')

if __name__ == '__main__':
    main()
