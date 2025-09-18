from __future__ import annotations
from heapq import heapify, heappush, heappop
from typing import List


class TaskManager:
    """
    Optimized heap with lazy deletion for task prioritization

    Intuition:
        Use a max-heap behavior via negatives to always get the highest-priority,
        highest-taskId task. Keep a map of the latest valid tuple for each task
        to lazily skip outdated heap entries after edits/removals.

    Approach:
        Maintain a min-heap of tuples (-priority, -taskId, userId).
        Keep a dict `valid` keyed by -taskId -> latest tuple.
        - add: push new tuple and update dict
        - edit: push updated tuple; old tuple remains but will be skipped later
        - rmv: delete dict entry; all heap entries for that task become invalid
        - execTop: pop until a tuple matches the dict entry; return userId

    Complexity:
        Time: add/edit O(log n), rmv O(1), execTop amortized O(log n)
        Space: O(n)
    """

    def __init__(self, tasks: List[List[int]]):
        """
        Initialize heap and validity map from initial tasks

        Intuition:
            Preload all given tasks into a heap and a dict to enable O(1)
            checks for validity during lazy deletions.

        Approach:
            Build the heap array in O(n), record the latest tuple for each
            task in `valid` keyed by -taskId, then heapify once.

        Complexity:
            Time: O(n) to build + O(n) heapify
            Space: O(n)
        """
        self.heap: list[tuple[int, int, int]] = []
        self.valid: dict[int, tuple[int, int, int]] = {}
        for user_id, task_id, priority in tasks:
            t = (-priority, -task_id, user_id)
            self.heap.append(t)
            self.valid[-task_id] = t
        heapify(self.heap)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        """
        Add a task or replace its latest version using lazy insertion

        Intuition:
            Push a new tuple for this task; older tuples remain but will be
            ignored during execTop if outdated.

        Approach:
            Update `valid[-taskId]` with the newest tuple and push onto heap.

        Complexity:
            Time: O(log n)
            Space: O(1) auxiliary, O(n) total
        """
        t = (-priority, -taskId, userId)
        self.valid[-taskId] = t
        heappush(self.heap, t)

    def edit(self, taskId: int, newPriority: int) -> None:
        """
        Edit task priority via lazy insertion of an updated tuple

        Intuition:
            Do not search the heap; instead, insert a new tuple with the
            updated priority and mark it as the only valid one for the task.

        Approach:
            Read previous tuple to keep user and task keys, create a new tuple
            with updated priority, update `valid`, and push to heap.

        Complexity:
            Time: O(log n)
            Space: O(1) auxiliary, O(n) total
        """
        old_pri, old_task, old_user = self.valid[-taskId]
        t = (-newPriority, old_task, old_user)
        self.valid[-taskId] = t
        heappush(self.heap, t)

    def rmv(self, taskId: int) -> None:
        """
        Remove a task by invalidating it in the map (lazy deletion)

        Intuition:
            Skip expensive removal from heap; just delete the dict entry so any
            heap items for this task become invalid.

        Approach:
            Pop `valid[-taskId]` if present; leave heap untouched.

        Complexity:
            Time: O(1)
            Space: O(1)
        """
        self.valid.pop(-taskId, None)

    def execTop(self) -> int:
        """
        Execute the highest-priority task, breaking ties by larger taskId

        Intuition:
            Continuously pop from heap until a tuple matches the current valid
            entry (or has not been removed). Then consume it and return userId.

        Approach:
            Pop-validate loop: compare popped tuple with `valid[tsk]`.
            If mismatch or missing, skip; else delete from map and return.

        Complexity:
            Time: Amortized O(log n)
            Space: O(1) auxiliary
        """
        while self.heap:
            pri, tsk, usr = heappop(self.heap)
            cur = self.valid.get(tsk)
            if cur is None:
                continue
            if cur[0] != pri or cur[2] != usr:
                continue
            del self.valid[tsk]
            return usr
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
