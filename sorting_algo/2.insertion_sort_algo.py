# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

# using swawp like bubble sort we used
def insertion_sort_algo(list_to_be_sorted):
    for i in range(1, len(list_to_be_sorted)):
        for j in range(i - 1, -1, -1):
            if list_to_be_sorted[j] > list_to_be_sorted[j + 1]:
                list_to_be_sorted[j], list_to_be_sorted[j + 1] = list_to_be_sorted[j + 1], list_to_be_sorted[j]
            else:
                break
    return list_to_be_sorted


def insertion_sort_algo_v2(list_to_be_sorted):
    for i in range(1, len(list_to_be_sorted)):
        j = i - 1
        while list_to_be_sorted[j] > list_to_be_sorted[j + 1] and j >= 0:
            list_to_be_sorted[j], list_to_be_sorted[j + 1] = list_to_be_sorted[j + 1], list_to_be_sorted[j]
            j -= 1
    return list_to_be_sorted


cust_list = [3, 2, 4, 1, 5, 6, 7, 8, 9, 10, 2, 3, 6, 6]

# print(insertion_sort_algo(cust_list))
print(insertion_sort_algo_v2(cust_list))