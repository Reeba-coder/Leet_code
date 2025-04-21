# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
def lowercase(s):
    result='  '
    for char in s:
        if 'A' <= char <='Z':
            lower_char=chr(ord(char)+32)
            result+=lower_char
        else:
            result+=char
    return result
print(lowercase("HELLO WORLD"))
print(lowercase("REEBA"))