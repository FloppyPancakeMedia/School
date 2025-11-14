import sys

word : str = sys.argv[1]

def is_palindrome(s : str):
    chars : list[chr] = []
    for c in s:
        chars.append(c)
    if len(chars) == 0 or len(chars) == 1: return "Palindrome"

    if chars[0] == chars[len(chars) - 1]:
        chars.remove(chars[0])
        chars.remove(chars[len(chars) - 1])
        new_s : str = ''.join(chars)
        return is_palindrome(new_s)
    else:
        return "Not Palindrome"


print(is_palindrome(word))