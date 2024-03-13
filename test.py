def binary_search(arr, target):
    """
    使用二分查找在有序列表arr中查找target。
    如果找到target，返回它的索引；否则返回-1。
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        # 找到目标值，返回索引
        if arr[mid] == target:
            return mid
        # 中间的数小于目标值，在右半部分继续查找
        elif arr[mid] < target:
            left = mid + 1
        # 中间的数大于目标值，在左半部分继续查找
        else:
            right = mid - 1

    # 如果没有找到目标值，返回-1
    return -1

# 示例
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 1

result = binary_search(arr, target)
if result != -1:
    print(f"元素 {target} 在数组中的索引为 {result}")
else:
    print(f"元素 {target} 不在数组中")