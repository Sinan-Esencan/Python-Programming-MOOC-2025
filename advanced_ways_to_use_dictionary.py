# we want to categorize the words based on the initial letter in each word. One way to accomplish this would be to use dictionaries. the values mapped to the keys are lists.

word_list = [
  "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
  "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
  "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
]

def categorize_by_initial(my_list):
    groups = {}
    for word in my_list:
        initial = word[0]
        # initialize a new list when the letter is first encountered
        if initial not in groups:
            groups[initial] = []
        # add the word to the appropriate list
        groups[initial].append(word)
    return groups

groups = categorize_by_initial(word_list)

print(groups)
print()

for key, value in groups.items():
    print(f"words beginning with {key}:")
    for word in value:
        print(word)
