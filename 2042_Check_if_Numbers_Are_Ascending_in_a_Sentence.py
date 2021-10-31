class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        spl = [int(i) for i in s.split(' ') if i.isdigit()]
        if list(dict.fromkeys(spl)) == spl :
            return sorted(spl) == spl
        return False
