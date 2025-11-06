class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0

        visited = {}
        first = 0
        maxLength = 0
        n = len(s)

        for last in range(n):
            char = s[last]
            if char in visited and visited[char] >= first:
                first = visited[char] + 1

            visited[char] = last
            maxLength = max(maxLength, last-first+1)

        return maxLength

        return length

        