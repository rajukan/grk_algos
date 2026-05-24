
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





def isValid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        # if it's an opening bracket, push onto stack
        if char in mapping.values():
            stack.append(char)
        # if it's a closing bracket, check match with top of stack
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            # unexpected character (optional: treat as invalid)
            return False

    # all brackets matched if stack is empty
    return len(stack) == 0

print(isValid("{[()]}"))