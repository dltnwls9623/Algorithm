import re, collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[\W]', ' ', paragraph)
        words = [word for word in paragraph.split() if word not in banned]

        cnt = collections.Counter(words)
        return cnt.most_common(1)[0][0]