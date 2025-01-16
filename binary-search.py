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

def binary_search(nums: list[int], target: int) -> int:
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

