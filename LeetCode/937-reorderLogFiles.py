class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        return sorted(logs, key=lambda log: (0, log.split(' ')[1:], log.split(' ')[0]) if log[-1].isalpha() else (1,))

print(Solution().reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))