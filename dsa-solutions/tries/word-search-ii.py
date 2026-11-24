from dataclasses import dataclass, field


@dataclass
class Trie:
    b: bool = False
    d: dict[str, "Trie"] = field(default_factory=dict)

    def insert(self, word: str) -> None:
        t = self
        for ch in word:
            if ch not in t.d:
                t.d[ch] = Trie()
            t = t.d[ch]
        t.b = True


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        RL, CL = len(board), len(board[0])
        P = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        root = Trie()
        for word in words:
            root.insert(word)
        v, wl = set(), []

        def search(r: int, c: int, l: list[str], t: Trie) -> None:
            l.append(board[r][c])
            t = t.d[board[r][c]]
            if t.b:
                wl.append("".join(l))
                t.b = False
            v.add((r, c))
            for dr, dc in P:
                nr, nc = r + dr, c + dc
                if 0 <= nr < RL and 0 <= nc < CL and (nr, nc) not in v and board[nr][nc] in t.d:
                    search(nr, nc, l, t)
            v.remove((r, c))
            l.pop()

        for r in range(RL):
            for c in range(CL):
                if board[r][c] in root.d:
                    search(r, c, [], root)
        return wl


# Time Complexity: O(s + m * n * 3^l) [s: words characters, m: board rows, n: board columns, l: longest word length]
# Space Complexity: O(s) [s: words characters]
