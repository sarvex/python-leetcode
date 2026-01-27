from collections import Counter, deque


class Solution:
    def watchedVideosByFriends(
        self,
        watchedVideos: list[list[str]],
        friends: list[list[int]],
        person_id: int,
        level: int,
    ) -> list[str]:
        """Get videos watched by friends at a given level, sorted by frequency.

        Intuition:
            BFS from the person to find all friends at the exact given level,
            then aggregate and sort their watched videos.

        Approach:
            Use BFS with a visited array to find friends at the target level.
            Collect all videos watched by those friends, count frequencies, and
            sort by frequency then alphabetically.

        Complexity:
            Time: O(n + V log V) where V is the number of unique videos
            Space: O(n + V)
        """
        total_people = len(friends)
        visited = [False] * total_people
        queue = deque([person_id])
        visited[person_id] = True

        for _ in range(level):
            for _ in range(len(queue)):
                current = queue.popleft()
                for friend in friends[current]:
                    if not visited[friend]:
                        queue.append(friend)
                        visited[friend] = True

        video_frequency: Counter[str] = Counter()
        for _ in range(len(queue)):
            friend = queue.pop()
            for video in watchedVideos[friend]:
                video_frequency[video] += 1

        videos = list(video_frequency.items())
        videos.sort(key=lambda entry: (entry[1], entry[0]))
        return [video for video, _count in videos]
