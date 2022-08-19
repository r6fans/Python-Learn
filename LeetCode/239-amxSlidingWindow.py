class myqueue:
    def __init__(self):
        self.queue = []
    
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            return self.queue.pop(0)
    
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop(-1)
        self.queue.append(value)

    def front(self) -> int:
        return self.queue[0]
    
    def get_queue(self):
        return self.queue
    
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        queue = myqueue()

        for i in range(k):
            queue.push(nums[i])
        
        result = []
        result.append(queue.front())
        for j in range(k, len(nums)):
            queue.pop(nums[j - k])
            queue.push(nums[j])
            result.append(queue.front())

        return result  