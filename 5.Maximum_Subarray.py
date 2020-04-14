# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum.

def max_subarray(array_of_integers):
    if len(array_of_integers) == 0:
        return print("Come on ! This is not an array!")

    max_sum_of_subarray = current_sum_of_subarray = array_of_integers[0]

    for num in array_of_integers[1:]:
        current_sum_of_subarray = max(current_sum_of_subarray + num, num)
        max_sum_of_subarray = max(current_sum_of_subarray, max_sum_of_subarray)

    print(max_sum_of_subarray)


max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
