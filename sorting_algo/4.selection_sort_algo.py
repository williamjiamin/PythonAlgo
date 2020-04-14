# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

# cust_list = [7, 8, 5, 4, 9, 2]
cust_list = [3, 2, 4, 1, 5, 6, 7, 8, 9, 10, 2, 3, 6, 6]

def selection_sort_algo(list_to_be_sorted):
    for i in range(0, len(list_to_be_sorted) - 1):
        divider_elem = i
        for j in range(i + 1, len(list_to_be_sorted)):
            if list_to_be_sorted[j] < list_to_be_sorted[divider_elem]:
                divider_elem = j
        if divider_elem != i:
            list_to_be_sorted[i], list_to_be_sorted[divider_elem] = list_to_be_sorted[divider_elem], list_to_be_sorted[
                i]
    return list_to_be_sorted


print(selection_sort_algo(cust_list))
