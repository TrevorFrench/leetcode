class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lengths = []
        for word in strs:
            lengths.append(len(word))
        i = 0
        prefix = []
        while i < min(lengths):
            compare = []
            for word in strs:
                compare.append(word[i])
            if len(set(compare)) == 1:
                prefix.append(compare[0])
            else:
                break
            i += 1
        pref_str = ""
        for letter in prefix:
            pref_str += letter
        return(pref_str)