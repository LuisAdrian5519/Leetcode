class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = []
        seen = set()
        
        for i in range(len(strs)):

            if i not in seen: 
            
                list = [strs[i]] 
                position = 1
                index = 9
            
                hashString = self.arr2hash(strs[i])

                for j in range(i+1, len(strs)):

                    hashSecondString = self.arr2hash(strs[j])

                    if hashString == hashSecondString:
                    
                        list.append(strs[j])
                        position += 1

                        seen.add(j)
                        index += 1


                result.append(list)
                

        return result
        
    
    def arr2hash(self, array):

        hashmap = {}

        for char in array:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] +=1

        return hashmap