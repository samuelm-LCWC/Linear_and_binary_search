def linear_search(search_list, search_item):
    #
    #Enter your code here
    #

def binary_search(search_list, search_item):
    #
    #Enter your code here


### --- USE THIS AS A TEST CASE SET --- ###

test_list_1 = [3, 5, 1, 4, 6, 7, 2]

test_list_2 = [2, 4, 6, 7, 9, 10, 23]

print(linear_search(test_list_1, 4))    # --> Should find at position 4

print(linear_search(test_list_1, 2))    # --> Should find at position 7

print(linear_search(test_list_1, 10))   # --> Should not find item

print(binary_search(test_list_2, 6))    # --> Should find at position 3

print(binary_search(test_list_2, 10))   # --> Should find at position 6

print(binary_search(test_list_2, 1))    # --> Should not find