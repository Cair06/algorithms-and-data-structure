# Bubble Sort Implementation
#
# Bubble sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.
# It continues until the list is sorted.
#
# Time Complexity: O(n^2), best case O(n) with early exit.
# Space Complexity: O(1)
#
# Parameters:
#     arr (list[int]): List of integers to sort.
#
# Returns:
#     list[int]: Sorted list.


def bubbleSort(arr:list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
