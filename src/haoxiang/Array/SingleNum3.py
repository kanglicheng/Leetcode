

class Solution(object):
    def singleNumber(self, nums):
        newMap = {}
        res = []
        for i in range(len(nums)):
            if newMap.has_key(nums[i]):
                newMap[nums[i]]+=1
            else:
                newMap[nums[i]] = 1

        for j in newMap:
            if newMap[j] == 1:
                res.append(j)
        return res
