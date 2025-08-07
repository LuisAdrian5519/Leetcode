#Failure

from typing import List

class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        counter_s = {}
        counter_t = {}

        for char in s:
            counter_s[char] = counter_s.get(char, 0) + 1

        for char in t:
            counter_t[char] = counter_t.get(char, 0) + 1

        return counter_s == counter_t

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = []
        seen = {}	
        Sublist = -1
        i = 0
        j = 1
        countero = 0
        counter = 0
        
        for i, word1 in enumerate(strs):

            if (i, word1) not in seen.items():
                Sublist += 1
                seen[countero] = word1 
                output.append([])
                output[Sublist].insert(counter, word1)
                countero += 1 
                counter = 0    

            for j in range(i+1, len(strs)):
            
                word2 = strs[j]
                if word2 not in seen:

                    if self.isAnagram(word1, word2):

                        counter += 1
                        seen[i+counter] = word2
                        output[Sublist].insert(counter, word2)
                        countero += 1 
                    else:
                        continue
                else:
                    continue


        return output


strs = ["act","pots","tops","cat","stop","hat"]

sol = Solution()
print(sol.groupAnagrams(strs))
