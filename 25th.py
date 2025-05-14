def canConstruct(ransomeNote,magazine)->bool:
    for char in ransomeNote:
        if char in magazine:
            magazine=magazine.replace(char,'',1)
        else:
            return False
    return True
print(canConstruct("a","b"))
print(canConstruct("aa","ab"))
print(canConstruct("aa","aab"))