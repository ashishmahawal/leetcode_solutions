pr_str = input("Enter the parenthesis string: ")

# ()}

def isValidString(pr_str):
    open_br = ['[','{','(']
    closed_br = [']','}',')']
    stack_br = []
    for i in range(0,len(pr_str)):
        if pr_str[i] in open_br:
            stack_br.append(pr_str[i])
        else:
            if len(stack_br) == 0:
                return False
            top = stack_br.pop()
            if top == '[' and pr_str[i] != ']':
                return False
            elif top == '{' and pr_str[i] != '}':
                return False
            elif top == '(' and pr_str[i] != ')':
                return False
    if len(stack_br) == 0:
        return True
    else:
        return False

res = isValidString(pr_str)    

print(f'String is valid: {res}')
