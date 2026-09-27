openers = ['(', '[', '{']
mapper = {")": "(", "]": "[", "}": "{"}
stack = []
valid = True

for paren_str in "{[()]}":
    if paren_str in openers:
        stack.append(paren_str)
    else:
        if not stack or stack.pop() != mapper[paren_str]:
            valid = False
            break

valid = valid and len(stack) == 0
print(valid)