    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        Trying to solve by O(n)/O(1)
        '''
        n = len(nums) - 1
        i = 0
        j = 0
        cur_ones = 0
        max_ones = 0
        hypo_ones = 0

        while i <= n:
            # first, the easy case of encounting 1
            if nums[i] == 1:
                cur_ones += 1
                i += 1
                # update the maximal value
                if cur_ones + hypo_ones > max_ones:
                    max_ones = cur_ones + hypo_ones
            # second case, encounting zero 
            elif nums[i] == 0:
                # set the second hypothetical pointer on zero
                j = min(i+1, n) # set the h.pointer to the next val
                hypo_ones += 1 # add as if it was 1
                while j<=n and nums[j] == 1 : # continue to count until the next zero
                    hypo_ones += 1
                    j += 1
                # update the max_ones value if need be
                if cur_ones + hypo_ones > max_ones:
                    max_ones = cur_ones + hypo_ones
                # reset the hypo params 
                cur_ones = 0
                hypo_ones = 0
                # when reached the 0 with hypo, move the original pointer anyway
                i += 1
            
        return max_ones