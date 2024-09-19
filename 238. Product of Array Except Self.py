class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for i in range(len(nums))]
        prefix_pro = 1
        for i in range(len(nums)-1):
            output[i] = prefix_pro
            prefix_pro *= nums[i]
        output[-1] = prefix_pro
        postfix_pro = 1
        #print("output = ",output)
        for j in range(len(nums)-1,0,-1):
            output[j] = output[j] * postfix_pro
            postfix_pro *= nums[j]
        output[0] *= postfix_pro
        return output

        
