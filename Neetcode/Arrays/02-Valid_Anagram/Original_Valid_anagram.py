class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        hashS = self.arr2hash(s)
        hashT = self.arr2hash(t)

        if hashT != hashS:
            return False
        else:
            return True

    def arr2hash(self, array):

        hashmap = {}

        for char in array:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] +=1

        return hashmap

