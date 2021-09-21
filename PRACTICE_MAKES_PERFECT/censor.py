#Here we right program for when user enter 2nd string that second string convert in **** and it applied also in 1st string.
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
  
print(censor("this hack is wack hack", "hack"))