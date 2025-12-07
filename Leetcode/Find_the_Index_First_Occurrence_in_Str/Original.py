from collections import deque

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        # create a Queue with needle
        # iterating on haystack
        # When I find first char of needle in haystack:
            # I start a second loop in which I compare the char to the tail of the queue
                # It they are equal, I pop the queue
                # On each iteration, I check if the queue is empty. 
                    # If yes, return the first index
    	
        q = deque()
        for char in needle:
            q.append(char)

        for i, char in enumerate(haystack):
            if char == q[0]:
                qc = deque(q)
                j = i
                for j, char2 in enumerate(haystack, start=i):
                    if char2 == qc[0]:
                        qc.popleft()
                    else:
                        break
                    if not qc:
                        return i
            else:
                continue

        return -1

haystack = "hello"
needle = "ll"

Sol = Solution()
print(Sol.strStr(haystack,needle))