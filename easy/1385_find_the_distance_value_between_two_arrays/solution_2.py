from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def find_insertion_index(arr: list, target: int) -> int:
            left, right = 0, len(arr) - 1

            while left <= right:
                index = (left + right) // 2

                if arr[index] == target:
                    return index
                elif arr[index] < target:
                    left = index + 1
                else:
                    right = index - 1

            return left

        def get_closest_value(arr: list, target: int) -> int:
            index = find_insertion_index(arr, target)

            if index == 0:
                return arr[0]

            if index == len(arr):
                return arr[index - 1]

            r_value = arr[index]
            l_value = arr[index - 1]

            if abs(r_value - target) < abs(l_value - target):
                return r_value
            else:
                return l_value

        result = 0
        arr2.sort()

        for i in range(len(arr1)):
            if abs(arr1[i] - get_closest_value(arr2, arr1[i])) > d:
                result += 1

        return result
