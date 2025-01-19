# Binary Search Implementation
# 
# Binary search is an efficient algorithm for finding an item from a sorted list of items.
# It works by repeatedly dividing the search interval in half. If the value of the search key
# is less than the item in the middle of the interval, narrow the interval to the lower half.
# Otherwise, narrow it to the upper half. Repeat until the value is found or the interval is empty.
# 
# Time Complexity:
#     - O(log n), where n is the size of the list.
# Space Complexity:
#     - O(1), as this implementation uses an iterative approach.
#
# Parameters:
#     nums (list[int]): A sorted list of integers.
#     target (int): The element to search for.
#
# Returns:
#     int: The index of the target element if found, otherwise -1.



def binarySearch(nums: list[int], target: int) -> int:
    """Realization with iter"""
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
    """Realization with recursive"""
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


