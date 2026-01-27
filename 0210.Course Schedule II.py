from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """Topological sort via BFS (Kahn's algorithm) to find course order.

        Intuition:
            A valid course order is a topological ordering of the prerequisite
            graph. BFS starting from zero in-degree nodes naturally produces
            this order.

        Approach:
            1. Build an adjacency list and in-degree array from prerequisites.
            2. Enqueue all courses with zero in-degree.
            3. Process the queue: append each course to the result, decrement
               neighbors' in-degree, and enqueue those reaching zero.
            4. Return the order if all courses are included, else empty list.

        Complexity:
            Time: O(V + E) where V = numCourses, E = len(prerequisites)
            Space: O(V + E)
        """
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            in_degree[course] += 1
        order = []
        queue = deque(i for i, degree in enumerate(in_degree) if degree == 0)
        while queue:
            current = queue.popleft()
            order.append(current)
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return order if len(order) == numCourses else []
