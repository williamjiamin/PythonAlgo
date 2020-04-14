# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

def is_anagram_or_not_by_using_algorithm(s, t):
    s = s.replace(' ', '').lower()
    t = t.replace(' ', '').lower()

    # 如果长度不一致，直接排除
    if len(s) != len(t):
        return False

    count_dic = {}

    # 这种方法是先创建一个dic，然后逐步进行统计（逐步添加的统计），然后再确定的时候进行
    # 逐步减少的操作，最终看看是否完全清空
    for every_letter in s:
        if every_letter in count_dic:
            count_dic[every_letter] += 1
        else:
            count_dic[every_letter] = 1

    for every_letter in t:
        if every_letter in count_dic:
            count_dic[every_letter] -= 1
        else:
            count_dic[every_letter] = 1

    for n in count_dic:
        if count_dic[n] != 0:
            return False
    return True


answer = is_anagram_or_not_by_using_algorithm('Dog', 'goa')

print(answer)
