# some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#
#
# def func_nested_for_loop(some_list):
#     for elem_1 in some_list:
#         for elem_2 in some_list:
#             print(elem_1, elem_2)
#
#
# func_nested_for_loop(some_list)

some_list_02 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def find_the_match(search_list, match_elem):
    for elem in search_list:
        if elem == match_elem:
            return print("Find the match")
    return print("Did not find it")

#
# find_the_match(some_list_02, 1)

find_the_match(some_list_02, 20)