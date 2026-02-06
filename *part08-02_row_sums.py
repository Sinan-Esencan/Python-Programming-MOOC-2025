# Please write a function named row_sums(my_matrix: list), which takes an integer matrix as its argument.
# The function should add a new element on each row in the matrix. This element contains the sum of the other elements on that row. The function does not have a return value. It should modify the parameter matrix in place.
# An example of the function in action:

# my_matrix = [[1, 2], [3, 4]]
# row_sums(my_matrix)
# print(my_matrix)

# Sample output
# [[1, 2, 3], [3, 4, 7]]

def row_sums(my_matrix: list):
    for row in my_matrix:
        total = 0
        for col in row:
            total += col
        row.append(total)

if __name__ == "__main__":
    my_matrix = [[1, 2],
                 [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)

# alt1 - mooc.fi: daha basit ve guzel:
def row_sums(matrix: list):
    for row in matrix:
        row.append(sum(row))

# V1: bu yontemde liste kopyalanır ve orijinal degismez
def row_sums(matrix: list):
    # 1. Gelen listenin bir kopyasını oluştur
    # Sadece [:] yaparsak listenin içindeki listelerin (row) kopyaları oluşmaz (Shallow Copy).
    # Bu yüzden her satırın da kopyasını alıyoruz.
    kopya_matrix = [satir[:] for satir in matrix]
    #satir[:] yerine satir.copy() de denebilirdi
    #copy module import edildikten sonra kopya_matrix = copy.deepcopy(matrix) de denebilirdi
    
    # 2. İşlemleri KOPYA üzerinde yap
    for row in kopya_matrix:
        row.append(sum(row))
    
    return kopya_matrix

if __name__ == "__main__":
    my_matrix = [[1, 2],
                 [3, 4]]
    
    # Fonksiyonu çağırıyoruz
    sonuc = row_sums(my_matrix)
    
    print("Orijinal:", my_matrix)  # Çıktı: [[1, 2], [3, 4]] (Değişmedi!)
    print("Sonuç:   ", sonuc)      # Çıktı: [[1, 2, 3], [3, 4, 7]]
