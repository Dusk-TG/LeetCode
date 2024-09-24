class Solution(object):
    def twoSum(self, nums, target):
        self = 0

        locater1 = 0
        locater2 = 1

        num1 = 0
        num2 = 0

        i = 1

        length = len(nums)

        keepGoing = True

        while keepGoing:

            num1 = nums[locater1]
            num2 = nums[locater2]

            result = num1 + num2

            if result == target:
                keepGoing = False
                results = []
                results.append(locater1)
                results.append(locater2)
                return(results)
            else:
                locater1 = locater1 + 1
                locater2 = locater2 + 1
            
            if locater1 == length:
                locater1 = 0
                locater1 = locater1 + i
                i = i + 1
                locater2 = 0
            
            if locater2 == length:
                locater1 = 0
                locater1 = locater1 + i
                i = i + 1
                locater2 = 0

            if locater2 == locater1:
                locater2 = locater2 + 1 
