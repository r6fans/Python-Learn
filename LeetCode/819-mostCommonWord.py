import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        paragraph = re.split(r"[ ,.!?';]",paragraph.lower())
        print(paragraph)

        dicts = {}
        for char in paragraph:
            dicts[char] = dicts.get(char,0)+1
        banned.append("")
        for i in dicts:
            if i in banned:
                dicts[i] = 0
        return max(dicts, key=dicts.get)
