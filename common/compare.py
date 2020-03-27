# -*- coding: utf-8 -*-
# @Time : 2020/3/13 14:53
# @Author : wangmengmeng


def listdict_compare(list1, list2):
    """两个列表格式同为 列表里嵌套字典（格式如[{'id': 1002, 'pharmacist_id': '3', 'pharmacist_name': 'wangmm'}]） 比较是否相等
    """
    if len(list1) != len(list2):
        return 0
    for i in list1:
        if i in list2:
            continue
        return 0
    return 1

if __name__ == '__main__':

    list1 = [1, 4]
    list2 = [1, 3]
    list3 = [1, 4]
    print(listdict_compare(list1, list2))
    print(listdict_compare(list1, list3))
