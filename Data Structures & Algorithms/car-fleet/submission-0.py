class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        # target = 10, position = [1,4], speed = [3,2]
        

        #       c1
        #                         c2
        # 0-----1-----2-----3-----4-----5-----6-----7-----8-----9-----target


        # target = 10, position = [4,1,0,7], speed = [2,2,1,1]

        #                         c1                                 c1
        #       c2                                  c2
        # c3                 c3
        #                                           c4               c4
        # 0-----1-----2-----3-----4-----5-----6-----7-----8-----9-----target
        #[3]


        

        speedMap = {}

        for i in range(len(position)):
            speedMap[position[i]] = speed[i]

        # speedMap = {4:2, 1:2, 0:1, 7:1}

        position.sort(reverse=True)

        # position = [7,4,1,0]
        #            3/3/4.5/10

        fleetCount = 0

        currentFleetFinishTime = (target - position[0]) / speedMap[position[0]]
        # 3

        for i in range(1, len(position)):
            finishTime = (target - position[i]) / speedMap[position[i]]
            if finishTime > currentFleetFinishTime:
                fleetCount += 1
                currentFleetFinishTime = finishTime
            
        fleetCount += 1
        
        return fleetCount


