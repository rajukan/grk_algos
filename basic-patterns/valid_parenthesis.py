
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.



Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false


'''




def parens(paren_strs):
    openers=['(','[','{']
    closers=[')',']','}']

    mapper = {
        ")":"(",
        "]":"[",
        "}":"{",
    }
    stack=[]

    for paren_str in paren_strs:
        if paren_str in openers:
            stack.append(paren_str)
        elif paren_str in closers:
            if not stack or stack.pop() != mapper[paren_str]:
                return False
    return len(stack)==0


print(parens("{[(])}"))