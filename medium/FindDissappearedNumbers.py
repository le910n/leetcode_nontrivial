def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    ''' 
    O(n) time complexity required. 
    O(1) space complexity required.
    '''
    N = len(nums)
    
    # first pass, marking indexwise as negative
    for n in nums:
        if nums[abs(n) - 1] > 0:
            nums[abs(n) - 1] = -nums[abs(n) - 1]
        
    
    # second pass, adding to the resulting array
    return [el for el in range(1, N + 1) if nums[el - 1] > 0]