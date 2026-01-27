from collections import defaultdict, deque


class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        """Find the minimum number of semesters to take all courses.

        Intuition:
            This is a topological sort problem where each BFS level represents
            one semester of courses that can be taken in parallel.

        Approach:
            Build an adjacency list and compute in-degrees. Use BFS starting
            from all courses with zero in-degree. Each BFS level is one
            semester. If not all courses are processed, a cycle exists.

        Complexity:
            Time: O(n + E) where E is the number of relations
            Space: O(n + E) for the graph and queue
        """
        graph: dict[int, list[int]] = defaultdict(list)
        in_degree = [0] * n
        for prerequisite, course in relations:
            graph[prerequisite - 1].append(course - 1)
            in_degree[course - 1] += 1

        queue = deque(i for i, degree in enumerate(in_degree) if degree == 0)
        semesters = 0
        remaining = n
        while queue:
            semesters += 1
            for _ in range(len(queue)):
                current = queue.popleft()
                remaining -= 1
                for neighbor in graph[current]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
        return -1 if remaining else semesters
