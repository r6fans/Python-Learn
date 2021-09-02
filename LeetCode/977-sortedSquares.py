class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        low,high,k = 0, n - 1, n - 1
        while low <= high:
            ls = nums[low] ** 2
            hs = nums[high] ** 2
            if ls > hs:
                res[k] = ls
                low += 1
            elif ls < hs:
                res[k] = hs
                high -= 1
            k -= 1
        return res
    
    def bobblesort(arr):
        for i in range(0,len(arr)):
            for j in range(0, len(arr) - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def selectionsort(arr):
        for i in range(0,len(arr) - 1):
            min = i
            for j in range(i, len(arr)):
                if arr[j] < arr[min]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
        return arr

    def insertionsort(arr):
        for 
    


                

            