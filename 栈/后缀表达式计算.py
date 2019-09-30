from 栈的顺序表实现 import Stack


def infix_to_suffix(infix):
    """中缀转后缀"""
    infix = infix.split(' ')
    operator = "*/+-"
    priority = {"+": 2, "-": 2, "*": 3, "/": 3}
    s1 = Stack()  # 符号栈
    suffix = []  # 后缀表达式结果

    for i in infix:

        if i in operator:
            # 如果时操作符
            while True:
                # s1为空或者s1栈顶为左括号，直接入栈
                if s1.is_empty() or s1.top() == '(':
                    s1.push(i)
                    break
                # 当前操作符优先级高于栈顶操作符，直接入栈
                elif priority[i] > priority[s1.top()]:
                    s1.push(i)
                    break
                # 否则，
                else:
                    suffix.append(s1.pop())
        elif i == '(':
            # 如果是左括号，直接压栈
            s1.push(i)
        elif i == ')':
            # 如果是右括号，弹出s1元素直到遇到左括号
            while s1.top() != '(':
                suffix.append(s1.pop())
            s1.pop()  # 弹出左括号
        else:
            # 如果是数字，直接添加到s2
            suffix.append(i)
    while not s1.is_empty():
        suffix.append(s1.pop())
    return suffix


def calculate_suffix(expression):
    operator = "*/+-"
    s = Stack()
    for item in expression:
        if item in operator:
            a = int(s.pop())
            b = int(s.pop())
            if item == '+':
                s.push(b + a)
            elif item == '-':
                s.push(b - a)
            elif item == '*':
                s.push(b * a)
            elif item == '/':
                s.push(b / a)
        else:
            s.push(item)
    return s.pop()


suffix = infix_to_suffix('( 3 - 5 ) * ( 6 + 17 * 4 ) / 3')
print(suffix)
calculate_suffix(suffix)
