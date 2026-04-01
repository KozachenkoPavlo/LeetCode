from solution_3 import Solution

if __name__ == "__main__":
    solution = Solution()
    tests = [
        {
            "nums1": [1, 2, 3, 4, 5, 6, 7, 8],
            "nums2": [1, 2, 3, 8],
            "right_answer": 3.5,
        },
        {
            "nums1": [1, 4, 7],
            "nums2": [2, 3, 5, 6],
            "right_answer": 4.0,
        },
        {
            "nums1": [1, 2, 3, 4, 5],
            "nums2": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
            "right_answer": 9.0,
        },
        {
            "nums1": [1, 2, 3, 4],
            "nums2": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
            "right_answer": 9.5,
        },
        {
            "nums1": [100],
            "nums2": [101],
            "right_answer": 100.5
        },
        {
            "nums1": [101],
            "nums2": [100],
            "right_answer": 100.5
        },
    ]

    for test in tests:
        result = solution.findMedianSortedArrays(test["nums1"], test["nums2"])
        status = "SUCCESS" if test["right_answer"] == result else "FAILURE"

        print(f"{status} {result}")
