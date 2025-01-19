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


def binarySearchRecursive(nums: list[int], target: int, left: int = 0, right: int = -1) -> int:
    
    # default right value as len of arr
    if right == -1:
        right = len(nums) - 1

    # Basic case
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if nums[mid] == target:
        return mid

    elif nums[mid] < target:
        return binarySearchRecursive(nums, target, mid+1, right)
    else:
        return binarySearchRecursive(nums, target, left, mid - 1)


