# Please write a function named factorials(n: int), which returns the factorials of the numbers 1 to n in a dictionary. The number is the key, and the factorial of that number is the value mapped to it.
# A reminder: the factorial of the number n is written n! and is calculated by multiplying the number by each integer smaller than itself. For example, the factorial of 4 is 4 * 3 * 2 * 1 = 24.

def factorials(n: int):
    multiplied_num = 1
    factorial_dict = {}
    for i in range(1, n+1):
        multiplied_num *= i
        factorial_dict[i] = multiplied_num
    return factorial_dict

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])


#alt2: mooc.fi:
def factorials(n: int):
    result = {}
    result[1] = 1
    for i in range(2, n + 1):
        result[i] = result[i-1] * i
    return result
