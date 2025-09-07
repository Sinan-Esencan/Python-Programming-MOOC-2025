#Please write a function named invert(dictionary: dict), which takes a dictionary as its argument. The dictionary should be inverted in place so that values become keys and keys become values.

def invert(dictionary: dict):
    copy_dictionary = dictionary.copy() #listteki slice ile esdeger
    dictionary.clear()
    for key, value in copy_dictionary.items():
        dictionary[value] = key
    print(copy_dictionary)

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)


#V2 - mooc.fi:
def invert(dictionary: dict):
	copy = {}
	for key in dictionary:
		copy[key] = dictionary[key]
    #alt: copy = dictionary.copy()

	for key in copy:
		del dictionary[key]
    #alt: dictionary.clear()
    
	for key in copy:
		dictionary[copy[key]] = key


#V3:
def invert(dictionary: dict):
    copy_dictionary = {}
    for key, value in dictionary.items():
        copy_dictionary[value] = key
    dictionary.clear()  # Orijinal sözlüğü temizle
    dictionary.update(copy_dictionary)  # Ters çevrilmiş kopyayı ekle


#V4 - dictionary comprehension:
def invert(dictionary: dict):
    # orijinali bozmamak için shallow-copy al (gerekiyorsa)
    inverted = {v: k for k, v in dictionary.items()}
    dictionary.clear()          # eski içeriği sil
    dictionary.update(inverted) # ters çevrileni yerleştir
