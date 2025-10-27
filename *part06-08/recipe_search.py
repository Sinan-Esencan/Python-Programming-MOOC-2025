# uzun oldugundan kopyalamıyorum, siteden bak

def add_to_list(filename: str): 
#normalde bu fonksiyon 1 kere main içerisinde çağrılmalı ve return edilen recipe_list, search_by_name(), search_by_time()
#ve search_by_ingredient() fonksiyonlarına file_name argumenti yerine pass edilmeli
    with open(filename, "r") as file:
        recipe_list = []
        recipe = []
        for line in file:
            line = line.strip()
            if line != "": #ilk asamada recipe'ye dataları ekliyoruz
                recipe.append(line)
            elif line == "":
                if recipe: #başta boşluk varsa diye
                    recipe_list.append(recipe) #daha sonra recipe'yi listeye ekliyoruz
                    recipe = []
        if recipe: #dosya sonunda bosluk olmadıgı zaman son recipe'yi eklemek icin
            recipe_list.append(recipe)
        return recipe_list

def search_by_name(filename: str, word: str):
    recipe_list = add_to_list(filename)
    searched_recipes = []
    for recipe in recipe_list:
        if word in recipe[0].lower():
            searched_recipes.append(recipe[0])
    return searched_recipes

def search_by_time(filename: str, prep_time: int):
    recipe_list = add_to_list(filename)
    searched_recipes = []
    for recipe in recipe_list:
        if int(recipe[1]) <= prep_time:
            searched_recipes.append(f"{recipe[0]}, preparation time {recipe[1]} min")
    return searched_recipes

def search_by_ingredient(filename: str, ingredient: str):
    recipe_list = add_to_list(filename)
    # print(recipe_list)
    searched_recipes = []
    for recipe in recipe_list:
        if ingredient in recipe[2:]:
            searched_recipes.append(f"{recipe[0]}, preparation time {recipe[1]} min")
    return searched_recipes

if __name__ == "__main__":
    if True:
        filename = "recipes1.txt"
        word = "cake"
        minutes = 20
        ingredient = "eggs"
    else:
        filename = input("Please enter the filename: ")
        word = input("Please enter the searched word: ")
        minutes = input("Please enter the maximum duration: ")
        ingredient = input("Please enter the searched ingredient: ")
    # found_recipes = search_by_name(filename, word)
    # found_recipes = search_by_time(filename, minutes)
    found_recipes = search_by_ingredient(filename, ingredient)
    print(found_recipes)


# V2 - Mooc.fi: benim kullandıgım [[a,b,c,d]] yerine [{'ingredients': [c,d], 'name':a, 'prep_time':b}] kullanmıs
def read_file(filename):
    with open(filename) as file:
# rows ara depolayıcı ile burada file -(row)-> rows -(row)-> new_recipe_dict -> recipes
# sırası kullanılmıs. bu rows arrayi kullanmadan da yazabilirdik. bkz: V3
        rows = []
        for row in file:
            rows.append(row.strip())
        # print(rows,"\n")
    recipes = []
    name_in_row = True
    prep_time_in_row = True
    new_recipe_dict = { "ingredients": []} # *bu bicimde gosterimi bil*
    for row in rows:
        if name_in_row: #1. satır isim (dosyanın bos baslamaması sart)
            new_recipe_dict["name"] = row
            name_in_row = False
            prep_time_in_row = True #2. satır prep time
        elif prep_time_in_row:
            new_recipe_dict["prep_time"] = int(row)
            prep_time_in_row = False
        elif len(row) > 0: #bosluga kadar ingredients
            new_recipe_dict["ingredients"].append(row)
        else: #bosluga geldik
            recipes.append(new_recipe_dict)
            name_in_row = True
            new_recipe_dict = {"ingredients": []} #sıfırlandı
    recipes.append(new_recipe_dict) # *dosya boş satırla bitmediği icin son recipeyi ekliyoruz*
    # print(recipes)
    return recipes

def search_by_name(filename: str, word: str):
    recipes = read_file(filename)
    found = []
    for recipe in recipes:
        if word.lower() in recipe["name"].lower():
            found.append(recipe["name"])
    return found

def search_by_time(filename: str, time: int):
    recipes = read_file(filename)
    found = []
    for recipe in recipes:
        if recipe["prep_time"] <= time:
            found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
    return found

def search_by_ingredient(filename: str, ingredient: str):
    recipes = read_file(filename)
    found = []
    for recipe in recipes:
        if ingredient.lower() in recipe["ingredients"]:
            found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
    return found

if __name__ == "__main__":
    if True:
        filename = "recipes1.txt"
        word = "cake"
        minutes = 20
        ingredient = "eggs"
    else:
        filename = input("Please enter the filename: ")
        word = input("Please enter the searched word: ")
        minutes = input("Please enter the maximum duration: ")
        ingredient = input("Please enter the searched ingredient: ")
    # found_recipes = search_by_name(filename, word)
    # found_recipes = search_by_time(filename, minutes)
    found_recipes = search_by_ingredient(filename, ingredient)
    print(found_recipes)


# V3: read_file() icerisinde rows arrayi kullanmadan dogrudan dosyadan okunabilirdi 
# (ancak V2'deki daha okunabilir cunku once dosya okunuyor sonra veri isleniyor)
# file -(row)-> new_recipe_dict -> recipes:
def read_file(filename):
    with open(filename) as file:
        recipes = []
        name_in_row = True
        prep_time_in_row = False
        new_recipe_dict = {"ingredients": []}
        
        for row in file:
            row = row.strip()
            
            if name_in_row:  # 1. satır isim (dosyanın boş başlamaması şart)
                new_recipe_dict["name"] = row
                name_in_row = False
                prep_time_in_row = True  # 2. satır prep time
            elif prep_time_in_row:
                new_recipe_dict["prep_time"] = int(row)
                prep_time_in_row = False
            elif len(row) > 0:  # boşluğa kadar ingredients
                new_recipe_dict["ingredients"].append(row)
            else:  # boşluğa geldik
                recipes.append(new_recipe_dict)
                name_in_row = True
                new_recipe_dict = {"ingredients": []}  # sıfırlandı
        
        recipes.append(new_recipe_dict)  # dosya boş satırla bitmediği için son recipe'yi ekliyoruz
        
    return recipes
