class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if not list1 or not list2:
            return []
        dict1 = {}
        res = []
        # 字典记录list1中的情况。
        for i,string in enumerate(list1):
            dict1[string]=i
        # 遍历list2
        min = float('inf') # 因为是求较小的值，所以min初始化成一个较大的值，后面不断迭代变小
        for i,string in enumerate(list2):
            if string in dict1:
                if i + dict1[string] < min: 
                    min = i+dict1[string]
                    res.clear()
                    res.append(string)
                elif i + dict1[string] == min: 
                    res.append(string)
        return res