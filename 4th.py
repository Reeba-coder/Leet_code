# main.py

def lengthOfLastWord(s: str) -> int:
    s = s.strip()           # Aage/peeche ke spaces hata rahe hain
    words = s.split()       # Words me tod rahe hain
    return len(words[-1])   # Last word ki length return kar rahe hain

# Test cases
print(lengthOfLastWord("Hello World"))                  # Output: 5
print(lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(lengthOfLastWord("luffy is still joyboy"))        # Output: 6
