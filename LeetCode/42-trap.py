from re import L
from typing import List


class Solution:
    #双指针法
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            lHight = height[i - 1]
            rHight = height[i + 1]
            for j in range(i - 1):
                if height[j] > lHight:
                    lHight = height[j]
            
            for k in range(i + 2, len(height)):
                if height[k] > rHight:
                    rHight = height[k]
            
            resl = min(lHight, rHight) - height[i]

            if resl > 0:
                res += resl
            
        return res
    
    #动态规划
    def trap_dynamic(self, height: List[int]) -> int:
        leftheight, rightheight = [0]*len(height), [0]*len(height)
        
        leftheight[0]=height[0]
        for i in range(1,len(height)):
            leftheight[i]=max(leftheight[i-1],height[i])
        rightheight[-1]=height[-1]
        for i in range(len(height)-2,-1,-1):
            rightheight[i]=max(rightheight[i+1],height[i])
        
        result = 0
        for i in range(0,len(height)):
            summ = min(leftheight[i],rightheight[i])-height[i]
            result += summ
        return result

if __name__ == "__main__":
    print(Solution().trap([0,1,0,3,2,0,0,4,0]))