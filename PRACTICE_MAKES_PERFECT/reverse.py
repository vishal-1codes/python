#Reverse string using python
def reverse(text):
    word=""
    l=len(text)-1
    while l>=0:
        word=word+text[l]
        l-=1
    return word

print(reverse("vishal"))