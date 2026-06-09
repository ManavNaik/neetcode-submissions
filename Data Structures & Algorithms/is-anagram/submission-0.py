class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
        # return sorted(s) == sorted(t)

        # if len(s) != len(t):
        #     return False
        # sorteds = sorted(s)
        # print(sorteds)
        # sortedt = sorted(t)
        # print(sortedt)
        # if(sorteds == sortedt):
        #     return True
        # else:
        #     return False