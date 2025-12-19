from collections import deque, defaultdict
from typing import List
from itertools import groupby


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        # Initialize secret knowledge: person 0 and firstPerson
        has_secret = [False] * n
        has_secret[0] = True
        has_secret[firstPerson] = True

        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])

        # Group meetings by their occurrence time
        for time, time_group in groupby(meetings, key=lambda x: x[2]):
            graph = defaultdict(list)
            people_involved = set()

            # Build an adjacency list for the current time slice
            for u, v, _ in time_group:
                graph[u].append(v)
                graph[v].append(u)
                people_involved.add(u)
                people_involved.add(v)

            # Start BFS from people who already know the secret in this group
            queue = deque([p for p in people_involved if has_secret[p]])

            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if not has_secret[neighbor]:
                        has_secret[neighbor] = True
                        queue.append(neighbor)

        # Return all people who know the secret
        return [i for i, known in enumerate(has_secret) if known]
