"""Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters as specified by the examples below."""

#alt1:
def squared(text, size):
    char_index = 0
    for i in range(size):
        row = ""
        for j in range(size):
            row += text[char_index % len(text)]
            char_index += 1
        print(row)
        
#alt1b: extra char var kullanılmıs:
def squared(text, size):
    char_index = 0
    for i in range(size):
        row = ""
        for j in range(size):
            char = text[char_index % len(text)]
            row += char
            char_index += 1
        print(row)
        
#alt1c: var kullanılmak yerine print edilmis:
def squared(text, size):
    char_index = 0
    for i in range(size):
        for j in range(size):
            print(text[char_index % len(text)], end="")
            char_index += 1
        print()


#alt2: mooc'nin ve 2 loop kullanmak yerine tek loop kullanıldıgından aradaki farkı anlamak acısından onemli:
def squared(characters, size):
    i = 0
    row = ""
    while i < size * size:
        if i > 0 and i % size == 0:
            print(row)
            row = ""
        row += characters[i % len(characters)]
        i += 1
    print(row)


squared("aybabtu", 5)
print()
squared("ab", 3)



#NOT alt: grok, claude ve chatgpt'ninki ise yaramadı:
def squared(s, n):
    for i in range(n):
        row = ""
        for j in range(n):
            index = (i + j) % len(s)
            row += s[index]
        print(row)
