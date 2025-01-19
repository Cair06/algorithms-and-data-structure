# Binary Search Implementation
#
# Binary search efficiently finds an item in a sorted list by repeatedly halving the search interval.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Parameters:
#     nums (list[int]): Sorted list of integers.
#     target (int): Element to search for.
#
# Returns:
#     int: Index of target if found, otherwise -1.


def binarySearch(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Preventing overflow

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found


def binarySearchRecursive(nums: list[int], target: int, left: int = 0, right: int = 0) -> int:
    l, r = left, right if right != 0 else len(nums) - 1
    m = l + (r - l) // 2
    
    if l > r:
        return -1

    if nums[m] == target:
        return m
    elif nums[m] < target:
        return binarySearchRecursive(nums, target, m+1, r)
    else:
        return binarySearchRecursive(nums, target, l, m - 1)


