# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

# 1.recursive(递归，把大问题拆分成跟大问题"差不多"的小问题，大问题的最终解决方案依赖与每个"差不多"的小问题的结果)
# 2.Divdie and Conquer algo(把大问题拆分为小问题，逐个击破)
# 3.对大量数据处理更加有效率的算法

# cust_list = [3, 2, 4, 1, 5, 6, 7, 8, 9, 10, 2, 3, 6, 6]
cust_list = [16, 86, 21, 5, 40, 2, 53, 12]


def merge_sort_algo(list_to_be_sorted):
    # list总体判断，切分
    if len(list_to_be_sorted) > 1:
        middle = len(list_to_be_sorted) // 2
        Left = list_to_be_sorted[:middle]
        Right = list_to_be_sorted[middle:]

        # 递归思想（自己调取自己）
        merge_sort_algo(Left)
        merge_sort_algo(Right)

        # i为Left里面的index，j为Right里面的index，k为总列表里面的index
        i = j = k = 0
        # 比大小，swap操作
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                list_to_be_sorted[k] = Left[i]
                i += 1
            else:
                list_to_be_sorted[k] = Right[j]
                j += 1
            k += 1

        # 查漏补缺
        while i < len(Left):
            list_to_be_sorted[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            list_to_be_sorted[k] = Right[j]
            j += 1
            k += 1

    return list_to_be_sorted


print(merge_sort_algo(cust_list))
