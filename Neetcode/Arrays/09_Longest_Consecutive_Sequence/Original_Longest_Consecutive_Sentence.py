class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ord_nums = []
        numsset = set(nums)
        sequence_length = 1
        longest_sequence = 0

        if nums == []:
            return 0

        ord_nums = sorted(list(numsset))

        for i in range(len(ord_nums)-1):
            if ord_nums[i+1] == ord_nums[i]+1:
                sequence_length += 1
            
            else:
                if sequence_length >= longest_sequence:
                    longest_sequence = sequence_length
                sequence_length = 1
        
        if sequence_length >= longest_sequence:
            longest_sequence = sequence_length

        return longest_sequence