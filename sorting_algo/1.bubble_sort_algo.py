# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

def bubble_sort_algo(list_to_be_sorted):
    for i in range(0, len(list_to_be_sorted) - 1):
        for j in range(0, len(list_to_be_sorted) - 1 - i):
            if list_to_be_sorted[j] > list_to_be_sorted[j + 1]:
                list_to_be_sorted[j], list_to_be_sorted[j + 1] = list_to_be_sorted[j + 1], list_to_be_sorted[j]
                print(list_to_be_sorted)
    return list_to_be_sorted


cust_list = [3, 2, 4, 1, 5, 6, 7, 8, 9, 10, 2, 3, 6, 6]


# alpha_list = ["d", "a", "b", "c"]
# print(bubble_sort_algo(cust_list))
# bubble_sort_algo(cust_list)
# bubble_sort_algo(alpha_list)

def bubble_sort_algo_v2(list_to_be_sorted):
    for i in range(0, len(list_to_be_sorted) - 1):
        # check whether there is a swap going on
        no_swap_going_on = True
        for j in range(0, len(list_to_be_sorted) - 1 - i):
            if list_to_be_sorted[j] > list_to_be_sorted[j + 1]:
                list_to_be_sorted[j], list_to_be_sorted[j + 1] = list_to_be_sorted[j + 1], list_to_be_sorted[j]
                no_swap_going_on = False
        if no_swap_going_on == True:
            break
    return list_to_be_sorted


print(bubble_sort_algo_v2(cust_list))
