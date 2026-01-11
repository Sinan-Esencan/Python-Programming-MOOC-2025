# The exercise template contains the file words.txt, which contains some English language words, one on each line.

# Please write a function named words(n: int, beginning: str), which returns a list containing n random words from the words.txt file. All words should begin with the string specified by the second argument.

# The same word should not appear twice in the list. If there are not enough words beginning with the specified string, the function should raise a ValueError exception.

# An example of the function in action:

# word_list = words(3, "ca")
# for word in word_list:
#     print(word)

# Sample output

# cat
# car
# carbon

from random import sample

def words(n: int, beginning: str):
    with open("words.txt", "r") as dosya:
        word_lst = [] #list of words starting with chars specified in "beginning" arg
        for line in dosya:
            line = line.strip()
            if line[:len(beginning)] == beginning:
                word_lst.append(line)

        if len(word_lst) < n: # *listedeki kelime sayısından daha fazla sayıda kelime aramamak icin*
            raise ValueError("Not enough suitable words can be found")

        selected_lst = sample(word_lst, n)
        return selected_lst

if __name__ == "__main__":
    try: #*burada try...except blok kullanıyoruz ki tracebackli hata mesajı degil sadece kendi yazdıgımız
        #hata mesajı gozuksun*
        word_list = words(3, "ca")
        for word in word_list:
            print(word)
    except ValueError as e:
        print(e)
