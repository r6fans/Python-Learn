class Solution:
    def longestWord(self, words: List[str]) -> str:
        return min([w for w in words if all(w[:i] in s for i in range(1, len(w)))] + [""], key = lambda x : (-len(x), x)) if (s := set(words)) else ""

        