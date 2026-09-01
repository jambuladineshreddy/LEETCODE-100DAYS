```python
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # Give every litter an index
        litter = {}
        start = None

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        total_litter = len(litter)
        target = (1 << total_litter) - 1

        # state = (row, col, remaining_energy, mask)
        q = deque()
        q.append((start[0], start[1], energy, 0))

        # visited[row][col][energy][mask]
        visited = set()
        visited.add((start[0], start[1], energy, 0))

        moves = 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                # All litter collected
                if mask == target:
                    return moves

                # Cannot move with zero energy
                if e == 0:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Outside grid
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    # Obstacle
                    if classroom[nr][nc] == 'X':
                        continue

                    new_energy = e - 1
                    new_mask = mask

                    # Collect litter
                    if (nr, nc) in litter:
                        idx = litter[(nr, nc)]
                        new_mask |= (1 << idx)

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    state = (nr, nc, new_energy, new_mask)

                    if state not in visited:
                        visited.add(state)
                        q.append(state)

            moves += 1

        return -1
```
