from math import inf


class Solution:
    def smallestSufficientTeam(
        self, req_skills: list[str], people: list[list[str]]
    ) -> list[int]:
        """Find the smallest team whose combined skills cover all required skills.

        Intuition:
            Represent each person's skills as a bitmask. The problem becomes
            finding the minimum set of bitmasks that OR to the full mask.

        Approach:
            Use dynamic programming over bitmask states. For each achievable
            state, try adding each person and update the next state if the
            team size improves. Track the last person added and the previous
            state for path reconstruction.

        Complexity:
            Time: O(2^m * n) where m is the number of skills and n is the number of people
            Space: O(2^m) for the DP arrays
        """
        skill_index = {skill: i for i, skill in enumerate(req_skills)}
        num_skills = len(req_skills)
        num_people = len(people)
        person_mask = [0] * num_people
        for i, skills in enumerate(people):
            for skill in skills:
                person_mask[i] |= 1 << skill_index[skill]

        total_states = 1 << num_skills
        min_team_size = [inf] * total_states
        last_person = [0] * total_states
        prev_state = [0] * total_states
        min_team_size[0] = 0

        for state in range(total_states):
            if min_team_size[state] == inf:
                continue
            for person in range(num_people):
                next_state = state | person_mask[person]
                if min_team_size[state] + 1 < min_team_size[next_state]:
                    min_team_size[next_state] = min_team_size[state] + 1
                    last_person[next_state] = person
                    prev_state[next_state] = state

        state = total_states - 1
        team: list[int] = []
        while state:
            team.append(last_person[state])
            state = prev_state[state]
        return team
