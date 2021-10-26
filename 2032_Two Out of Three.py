class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        values = []
        counting = {}
        
        for i in nums1:
            if i in values:
                pass
            else :
                if i in counting.keys():
                    counting[i] += 1
                else :
                    counting[i] = 1
                values.append(i)
        
        del values[:]
        for i in nums2:
            if i in values:
                pass
            else :
                if i in counting.keys():
                    counting[i] += 1
                else :
                    counting[i] = 1
                values.append(i)
                    
        del values[:]
        for i in nums3:
            if i in values:
                pass
            else :
                if i in counting.keys():
                    counting[i] += 1
                else :
                    counting[i] = 1
                values.append(i)
        del values[:]
        
        for key, value in counting.items():
            if value > 1:
                values.append(key)
        return values
