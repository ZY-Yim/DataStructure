# this file is about Stack

"""
implemention of stack
"""

class Stack():
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        # self.items.insert(0, item)

    def pop(self):
        return self.items.pop()
        # return self.items.pop(0)

    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)

# s = Stack()
# print(s.is_empty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.is_empty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())

"""
balanced parentheses
"""

def match(open, close):
    opens = "([{"
    closes = ")]}"

    return opens.index(open) == closes.index(close)


def par_checker(symbol_str):
    s = Stack()
    balanced = True

    index = 0

    """
    # balanced parentheses
    while index < len(symbol_str) and balanced:
        symbol = symbol_str[index]

        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()

        index += 1
    """

    while index < len(symbol_str) and balanced:
        symbol = symbol_str[index]

        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not match(top, symbol):
                    balanced = False
        
        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False


# print(par_checker('((()))'))
# print(par_checker('(()'))

# print(par_checker('{{([][])}()}'))
# print(par_checker('[{()]'))


"""
Converting Decimal Numbers to Binary Numbers
Divide by 2
"""

def divide_by_base(dec_number, base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base    # 返回整数

    bin_str = ""
    while not rem_stack.is_empty():
        bin_str = bin_str + digits[rem_stack.pop()]
    
    return bin_str

# print(divide_by_base(233, 2))
# print(divide_by_base(233, 8))
# print(divide_by_base(233, 16))


"""
Conversion of Infix Expressions to Prefix and Postfix 
"""

def infix_to_postfix(infix_expr):
    prec = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }

    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    
    return " ".join(postfix_list)

# print(infix_to_postfix("A * B + C * D"))
# print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))


def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    
    return operand_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

# print(postfix_eval('7 8 + 3 2 + /'))

    

