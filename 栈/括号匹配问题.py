from 栈的顺序表实现 import Stack


def check_parens(text):
    s = Stack()
    parens = "()[]{}"
    open_parens = "([{"
    map_dict = {")": "(", "]": "[", "}": "{"}

    for i in text:
        if i in parens:
            if i in open_parens:
                s.push(i)
            elif s.pop() != map_dict[i]:
                return False
    if s.is_empty():
        return True
    else:
        return False


print(check_parens('{}'))
