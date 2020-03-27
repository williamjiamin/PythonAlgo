# using swawp like bubble sort we used
def insertion_sort_algo(list_to_be_sorted):
    for i in range(1, len(list_to_be_sorted)):
        for j in range(i - 1, 0, -1):
            if list_to_be_sorted[j] > list_to_be_sorted[j + 1]:
                list_to_be_sorted[j], list_to_be_sorted[j + 1] = list_to_be_sorted[j + 1], list_to_be_sorted[j]
            else:
                break


def insertion_sort_algo_v2(list_to_be_sorted):
    for i in range(1, len(list_to_be_sorted)):
        j = i - 1
        while list_to_be_sorted[j] > list_to_be_sorted[j + 1] and j >= 0:
            list_to_be_sorted[j], list_to_be_sorted[j + 1] = list_to_be_sorted[j + 1], list_to_be_sorted[j]
            j -= 1
