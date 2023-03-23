class Solution(object):
    lookup = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        last = None
        for l in s:
            if l == "V" and last == "I":
                i = i + 3
            elif l == "X" and last == "I":
                i = i + 8
            elif l == "L" and last == "X":
                i = i + 30
            elif l == "C" and last == "X":
                i = i + 80
            elif l == "D" and last == "C":
                i = i + 300
            elif l == "M" and last == "C":
                i = i + 800
            else:
                i = i + self.lookup[l]
            last = l
        return(i)
    