#Here we remove vowels from string AEOUI

def anti_vowel(text):
    result=""
    vowel="aeouiAEOUI"
    for char in text:
        if char not in vowel:
            result+=char
        return result
    print(anti_vowel("vishal"))
