def palindrome(s: str)->bool:
    """
    check The string is palindrome or not"""
    result=" "
    for char in s:
        acsii =ord(char)
        if 48<= acsii <=57:
            result+=char
        elif 65<= acsii <=90:
            result+=chr(acsii+32) # chr()[built in function] function is used to convert the ascii valur in character 
        elif 97<= acsii <=122:
            result+=char
    # use two pointer to check palindrome
    left=0
    right=len(result)-1
    while left<right:
        if result[left]!= result[right]:
            return False
        left+=1
        right-=1
    return True

print(palindrome("madam"))