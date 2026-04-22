# Please write a function named find_words(search_term: str). It should return a list containing all the words in the file which match the search term.
# The search term may include lowercase letters and the following wildcard characters:
#     a) A dot . means that any single character is acceptable in its place. For example, ca. would yield words like cat and car, p.ng would yield 
# words like ping and pong, and .a.e would yield words like sane, care and late.
#     b) An asterisk * at the end of the search term means that any word which begins with the search term is acceptable. An asterisk at the beginning
# of the search term means that any word which ends with the search term is acceptable. For example, ca* would yield words like california, cat, caring
# and catapult, while *ane would yield words like crane, insane and aeroplane. There can only ever be a single asterisk in the search term.
#     c) If there are no wildcard characters in the search term, only words which match the search term exactly are returned.
# You may assume both wildcards are never used in the same search term.
# The words in the file are all written in lowercase. You may also assume the argument to the function will be in lowercase entirely.
# If no matching words are found, the function should return an empty list.
# Hint: the Pythons string methods startswith() and endswith() may be useful here. You can search for more information about them online.
# An example of the function in action:
# print(find_words("*vokes"))
# Sample output:
# ['convokes', 'equivokes', 'evokes', 'invokes', 'provokes', 'reinvokes', 'revokes']

def asterix_beginning(search_term, new_file):
    matched_words = []
    for word in new_file:
        word = word.strip()
        if word.endswith(search_term):
            matched_words.append(word)
    return matched_words

def asterix_end(search_term, new_file):
    matched_words = []
    for word in new_file:
        word = word.strip()
        if word.startswith(search_term):
            matched_words.append(word)
    return matched_words

def normal_search(search_term, new_file):
    matched_words = []
    for word in new_file:
        word = word.strip()
        if search_term == word:
            matched_words.append(word)
    return matched_words

def find_words(search_term: str):
    with open("words.txt") as new_file:
        if search_term[-1] == "*":
            search_term = search_term[:-1]
            return asterix_end(search_term, new_file)
        
        if search_term[0] == "*":
            search_term = search_term[1:]
            return asterix_beginning(search_term, new_file)
        
        if "." in search_term:
            matched_words = []
            for word in new_file:
                word = word.strip()
                if len(word) != len(search_term):
                    continue

                for i, char in enumerate(search_term):
                    if search_term[i] == ".":
                        if i == len(search_term)-1: #kelime nokta ile bitiyorsa listeye eklemek icin
                            matched_words.append(word)
                        continue #sonraki harfe gecer

                    if word[i] != char: 
                        break #sonraki kelimeye gecer

                    if i == len(search_term)-1: #kelimeyi listeye sadece son indiste eklemek icin
                        matched_words.append(word)
            return matched_words
        # *alt: inner loopta flag kullanmak okunurlugu artırır:*
        #         eslesme_basarili = True
        #         for i in range(len(search_term)):
        #             if search_term[i] == ".":
        #                 continue # Jokerse takılma
        #             if word[i] != search_term[i]:
        #                 eslesme_basarili = False
        #                 break # Farklı harf var, bu kelimeyi boşver
        #         if eslesme_basarili:
        #             matched_words.append(word)
        #     return matched_words
        
        return normal_search(search_term, new_file)
        
if __name__ == "__main__":
    print(find_words("abaci"))
    print(find_words("*vokes"))
    print(find_words("abat*"))
    print(find_words(".."))
    print(find_words("c.t"))
    print(find_words("p.ng"))
    print(find_words(".a.e"))


# *alt: daha iyi mooc.fi versiyonu:*
def find_words(search_term: str):
    results = []
 
    with open("words.txt") as file:
        keyword_without_asterix = search_term.replace("*","") #\n olmasa bile hata vermez
# aslında performans acısından kelimelerin looplandıgı bu dongu if statementların icinde olmalı. (bkz. alt2)
        for word in file:
            word = word.replace("\n","") #alt: word.strip()
            # Is there an asterisk?
            if "*" in search_term:
                # start or end?
                if search_term[0] == "*":
                    if word.endswith(keyword_without_asterix):
                        results.append(word)
                else:
                    if word.startswith(keyword_without_asterix):
                        results.append(word)
            # Is there a dot?
            elif "." in search_term:
                # same length?
                if len(search_term) == len(word):
                    found = True
                    for i in range(len(search_term)): #enumerate kullanılabilirdi
                        if search_term[i] != "." and (search_term[i] != word[i]):
                            found = False
                            break
                    if found:
                        results.append(word)
            # No special characters, only whole word matches count
            else:
                if word == search_term:
                    results.append(word)
    return results


# alt2: mooc.fi alt.ının daha performanslısı cunku kelimeler if statement icinde looplanıyor
# search_term döngü boyunca hiç değişmediği için, her iterasyonda if "*" in search_term gibi 
# koşulları tekrar kontrol etmek gereksiz bir iş yükü oluşturur
def find_words(search_term: str):
    results = []
    keyword_without_asterisk = search_term.replace("*", "")

    with open("words.txt") as file:
        words = [word.strip() for word in file]  # Dosyayı bir kez oku

    if "*" in search_term:
        if search_term[0] == "*":
            for word in words:
                if word.endswith(keyword_without_asterisk):
                    results.append(word)
        else:
            for word in words:
                if word.startswith(keyword_without_asterisk):
                    results.append(word)

    elif "." in search_term:
        for word in words:
            if len(search_term) == len(word):
                if all(sc == "." or sc == wc for sc, wc in zip(search_term, word)):
                    results.append(word)

    else:
        for word in words:
            if word == search_term:
                results.append(word)

    return results
