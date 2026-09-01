from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {course: set() for course in range(numCourses)}

        for prerequisite in prerequisites:
            courses[prerequisite[0]].add(prerequisite[1])

        # print(f"Initial courses: {courses}")

        visited = set()
        global_visited = set()
        result = []

        def dfs(course: int) -> bool:
            # print(f"Starting DFS for {course}")
            if course in visited:
                # print("This course was considered before... It is a LOOP!!!")
                return False

            if not courses[course]:
                if course not in global_visited:
                    # print(f"This course({course}) doesn't have any pre-courses, ADD!")
                    result.append(course)
                    # print(f"RESULT: {result}")
                    global_visited.add(course)
                return True

            visited.add(course)

            for pre_course in courses[course]:
                if not dfs(pre_course):
                    # print(f"Inner function returned False, coming back!!!")
                    return False

            visited.remove(course)
            courses[course] = set()

            if course not in global_visited:
                # print(f"I have added this course({course}) because it hasn't been added yet")
                result.append(course)
                global_visited.add(course)

            return True

        for course in courses:
            # print(f"Checking {course}")
            if course in global_visited:
                # print(f"It is in global, skip it")
                continue

            if not dfs(course):
                return []

        return result
