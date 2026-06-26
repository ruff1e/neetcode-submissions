class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        stack = []   # [temp, index]
        result = [0] * n


        # temperatures = [30,38,30,36,35,40,28]
        # result = [1,4,1,2,1,0,0]

        # stack = [[30,0]]



        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = (i - stackIndex)
            stack.append([temp, i])


        return result
