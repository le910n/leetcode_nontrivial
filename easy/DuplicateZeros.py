    def duplicateZeros(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ########################
        #  # # praparation # # #
        ########################
        max_idx = len(nums) - 1
        possible_dups = 0

        ######################
        # # # first pass # # #
        ######################
        # Find the number of zeros to be duplicated
        for left in range(max_idx + 1): # list(range(3)) = [0, 1, 2] 

            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if left > max_idx - possible_dups:
                break

            # Count the zeros
            if nums[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included  
                if left == max_idx - possible_dups:
                    nums[max_idx] = 0 # For this zero we just copy it without duplication.
                    max_idx -= 1
                    break

                possible_dups += 1

        # Start backwards from the last element which would be part of new list.
        last = max_idx - possible_dups

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if nums[i] == 0:
                nums[i + possible_dups] = 0
                possible_dups -= 1
                nums[i + possible_dups] = 0
            else:
                nums[i + possible_dups] = nums[i]
        