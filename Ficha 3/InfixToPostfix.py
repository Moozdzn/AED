from Stack import Stack



def infixToPostfix(expression):
    op_stack = Stack()
    string2List = []
    output = []
    string2List = expression.split()
    for char in string2List:
        if char in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            output.append(char)
        elif char == '(':
            op_stack.push(char)
        elif char == ')':
            while True:
                if op_stack.is_empty():
                    break
                else:
                    c = op_stack.pop()
                    if c == '(':
                        break
                    else:
                        output.append(c)
        elif char in  '*/+-^':
            while True:
                if op_stack.is_empty():
                    op_stack.push(char)
                    break
                else:
                    try:
                        c = op_stack.peek()
                        if char == '+' and c in '*/-^+':
                            output.append(op_stack.pop())
                        elif char == '-' and c in '*/+^-':
                            output.append(op_stack.pop())
                        elif char == '*' and c == '/^*':
                            output.append(op_stack.pop())
                        elif char == '/' and c in '*^/':
                            output.append(op_stack.pop())
                        elif char == '^' and c in '^':
                            output.append(op_stack.pop())
                        else:
                            op_stack.push(char)
                            break
                    except:
                        print('Bad Expression: %s'%expression)
                        break
        else:
            try:
                output.append(float(char))
            except ValueError:
                print('Bad Expression: %s'%expression)
                break
    while True:
        if op_stack.is_empty():
            break
        else:
            output.append(op_stack.pop())
    return ' '.join(map(str,output))

def main():
    print(infixToPostfix("A * B + C ^ D"))
    print(infixToPostfix("( 4.4 + 4.6 ) ^ ( 2 / ( 1 + 3 ) )"))
    print(infixToPostfix("( 2 ^ 20 ) ^ ( 2 / ( 1 + 3 ) )"))
    print(infixToPostfix("A * B ) + ( C ^ D )"))
    print(infixToPostfix("( A * B ) + (C ^ D )"))
    print(infixToPostfix("7 + 9 * 8 / 4 ^ 2"))
    print(infixToPostfix("( 17 + 9 ) * 3 / ( 5 - 3 ) ^ 4"))

if __name__ == '__main__':
    main()
