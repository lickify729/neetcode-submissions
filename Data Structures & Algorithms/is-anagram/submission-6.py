import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        s_list = []
        t_list = []

        for i in s:
            s_list.append(i)
        for j in t:
            t_list.append(j)
        
        s_list.sort()
        t_list.sort()
        
        if (s_list == t_list):
            return True
        else:
            return False
        """
        fish_set = list(string.ascii_lowercase)
        frequency_dict = dict.fromkeys(fish_set, 0)
        for i in s:
            frequency_dict[i] += 1
        for j in t:
            if (frequency_dict[j] == 0):
                return False
            else:
                frequency_dict[j] -= 1
        for k in frequency_dict.values():
            if k != 0:
                return False
        return True