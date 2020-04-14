# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

# make swap to shift

cust_list = [3, 2, 4, 1, 5, 6, 7, 8, 9, 10, 2, 3, 6, 6]


def insertion_sort_algo_v2(list_to_be_sorted):
    for i in range(1, len(list_to_be_sorted)):
        Picked_Num = list_to_be_sorted[i]
        for j in range(i - 1, -1, -1):
            if list_to_be_sorted[j] > Picked_Num:
                list_to_be_sorted[j + 1] = list_to_be_sorted[j]
            else:
                list_to_be_sorted[j + 1] = Picked_Num
                break

    return list_to_be_sorted


print(insertion_sort_algo_v2(cust_list))
