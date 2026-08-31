from typing import List


class Solution:
    # Time: O(N + M)
    # Space: O(N)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: set() for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            pre_map[course].add(prerequisite)

        visit_set = set()

        def dfs(course: int):
            if course in visit_set:
                return False
            if not pre_map[course]:
                return True

            visit_set.add(course)

            for pre_course in pre_map[course]:
                if not dfs(pre_course):
                    return False

            visit_set.remove(course)
            pre_map[course] = set()

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
