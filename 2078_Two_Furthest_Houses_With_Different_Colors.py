class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max = 0
        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[i] != colors[j] and abs(i - j) > max:
                    max = abs(i - j)
        return max
