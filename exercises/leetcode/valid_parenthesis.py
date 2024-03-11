#  Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#  An input string is valid if:

#  Open brackets must be closed by the same type of brackets.
#  Open brackets must be closed in the correct order.
#  Every close bracket has a corresponding open bracket of the same type.

def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            return False

    return not stack

# Test cases
n = is_valid('()')       # Output: True
print(n)

n = is_valid('()[]{}')   # Output: True
print(n)

n = is_valid('(]')       # Output: False
print(n)

n = is_valid('([)]')     # Output: False
print(n)

n = is_valid('{[]}')     # Output: True
print(n)
