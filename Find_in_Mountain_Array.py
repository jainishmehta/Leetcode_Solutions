class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()

        low = 1
        high = length - 2
        while low != high:
            test_index = (low + high) >> 1
            curr = mountain_arr.get(test_index) 
            next = mountain_arr.get(test_index + 1)
            
            if curr < next:
                if curr == target:
                    return test_index
                if next == target:
                    return test_index + 1
                low = test_index + 1
            else:
                high = test_index
        
        peak_index = low

        low = 0
        high = peak_index
        while low <= high:
            test_index = (low + high) >> 1
            curr = mountain_arr.get(test_index)
                
            if curr == target:
                return test_index
            elif curr < target:
                low = test_index + 1
            else:
                high = test_index - 1
        
        low = peak_index + 1
        high = length - 1
        while low <= high:
            test_index = (low + high) >> 1
            curr = mountain_arr.get(test_index)
                
            if curr == target:
                return test_index
            elif curr > target:
                low = test_index + 1
            else:
                high = test_index - 1
        
        return -1    
