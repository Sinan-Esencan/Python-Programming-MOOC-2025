# Please create a class named ListHelper which contains the following two class methods.
#     greatest_frequency(my_list: list) returns the most common item on the list
#     doubles(my_list: list) returns the number of unique items which appear at least twice on the list
# It should be possible to use these methods without creating an instance of the class. An example of how the methods could be used:
# numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
# print(ListHelper.greatest_frequency(numbers))
# print(ListHelper.doubles(numbers))
# Sample output
# 5
# 3

class ListHelper:

    @staticmethod
    def count_repetitions(my_list):
        repetition_counts = {}
        for item in my_list:
            # alt: repetition_counts[item] = repetition.get(item, 0) + 1
            if item in repetition_counts:
                repetition_counts[item] += 1
            else:
                repetition_counts[item] = 1
        return repetition_counts
   
    @classmethod
    def greatest_frequency(cls, my_list: list):

        repetition_counts = cls.count_repetitions(my_list)
        
        number_with_max_repetition = None
        max_repetition = 0
        for number, repetition in repetition_counts.items():
            if repetition > max_repetition:
                max_repetition = repetition
                number_with_max_repetition = number
        return number_with_max_repetition


    @classmethod
    def doubles(cls, my_list: list):

        repetition_counts = cls.count_repetitions(my_list)

        double_numbers = []
        for number, repetition in repetition_counts.items():
            if repetition >= 2:
                double_numbers.append(number)
        # print(double_numbers)
        return len(double_numbers)


if __name__ == "__main__":
    # numbers = [1, 1, 1, 2, 2, 3]
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))


# alt - mooc.fi:
class ListHelper:
 
    @classmethod
    def greatest_frequency(cls, my_list: list):
        # If there is no items at all, then there is no frequency
        if not my_list:
            return None
 
        max_frequency = 0
        max_item = None
        for item in my_list:
            frequency = my_list.count(item)
            if not max_item or frequency > max_frequency:
                max_frequency = frequency
                max_item = item
 
        return max_item
 
    @classmethod
    def doubles(cls, my_list: list):
        counts = {}
        for item in my_list:
            counts[item] = my_list.count(item)
 
        doubles = 0
        for value in counts.values():
            if value > 1:
                doubles += 1
 
        return doubles
