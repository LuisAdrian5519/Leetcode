from typing import List
from collections import defaultdict

class Solution:

    def encode(self, strs: List[str]) -> str:
        str_enc = ""

        for i, s in enumerate(strs):
            str_enc += f"{i}#{s}"  # Concatenate `i` y `strs[s]`

        return str_enc
    

    def decode(self, s: str) -> List[str]:

        str_dec = []
        
        current_num = None
        current_str = ""

        for c in s:
            if c.isnumeric():
                if current_num is not None:

                    str_dec[c] = current_str
                current_num = int(c)
                current_str = ""

            else:
                current_str += c

        if current_num is not None:
            str_dec[current_num] = current_str

        
        return str_dec


Input = ["neet","code","love","you"]

sol = Solution()
print(sol.decode(sol.encode(Input)))