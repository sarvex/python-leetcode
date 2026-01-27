from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """Topological sort via BFS (Kahn's algorithm) for cycle detection.

        Intuition:
            If we can topologically sort all courses, there is no cycle and all
            courses can be finished. Courses with zero in-degree can be taken
            first.

        Approach:
            1. Build an adjacency list and in-degree array from prerequisites.
            2. Enqueue all courses with zero in-degree.
            3. Process the queue: for each course, decrement neighbors'
               in-degree and enqueue those reaching zero.
            4. If all courses are processed, return True.

        Complexity:
            Time: O(V + E) where V = numCourses, E = len(prerequisites)
            Space: O(V + E)
        """
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            in_degree[course] += 1
        completed = 0
        queue = deque(i for i, degree in enumerate(in_degree) if degree == 0)
        while queue:
            current = queue.popleft()
            completed += 1
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return completed == numCourses
