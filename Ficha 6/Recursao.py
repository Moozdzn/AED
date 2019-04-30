def string_inverter(expression):
    if len(expression) == 0:
        return expression
    else:
        return string_inverter(expression[1:]) + expression[0]

def palindrom_checker(expression):
    s = expression.lower().replace(',','').replace(' ','')
    
    if len(s) == 0:
        return True
    else: 
        if s[-1] == s[0]:
            return palindrom_checker(s[1:-1])
        else:
            return False

def list_inverter(l):
    if len(l) == 0:
        return l  
    else:
        return [l.pop()] + list_inverter(l)  

def factorial(n):
    if n == 0:
        return n
    else:
        return n * factorial(n - 1)

def f_recursive(n):
   if n <= 1:
       return n
   else:
       return(f_recursive(n-1) + f_recursive(n-2))

def f_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def pascal_triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        next_row = [1]
        result = pascal_triangle(n-1)
        prev_row = result[-1]
        for i in range(len(prev_row)-1):
            next_row.append(prev_row[i] + prev_row[i+1])
        next_row += [1]
        result.append(next_row)
    return result 

#a = str(input("Enter string: "))

#print(string_inverter(a))
#print(palindrom_checker(a))

#l = [1,2,3,4,5,6]
#print(list_inverter(l))

#print(f_recursive(6))
#print(f_iterative(6))

print(pascal_triangle(4))