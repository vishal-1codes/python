#Word Up +++
pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word=original.lower()
    first=word[0]
    print(original)
else:
    print('empty')