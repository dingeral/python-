#这是Python中经典快速排序算法


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


f = input("请输入：")
s = eval(f)
print(quicksort(s))


'''
例：
>> python 排序.py
请输入：3,6,8,10,1,2,1
[1, 1, 2, 3, 6, 8, 10]
'''
