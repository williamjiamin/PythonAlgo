some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def func_nested_for_loop(some_list):
    for elem_1 in some_list:
        for elem_2 in some_list:
            print(elem_1, elem_2)


func_nested_for_loop(some_list)
