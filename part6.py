# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:43:22 2020

@author: airar

 visited_nodes_in_order.append(starting_node)

    node = starting_node
    reached = []
    prev = [0] * (goal_node+1)
    
    reached.append(starting_node.ID)
    prev.append(starting_node.ID)

    frontier = []
    frontier.append(node)
    x = 1
    while len(frontier)!=0:
      find = False
      nodeA = frontier.pop(0)
      neighbors = nodeA.connected_nodes
      for row, r in enumerate(neighbors):
        s = neighbors[row][1]
        d = s.ID
        if d == goal_node:
          reached.append(d)
          prev[x] = d
          find = True
          break
        if d not in reached:
          reached.append(d)
          frontier.append(s)
          prev[x] = d
          x = x+1
        else: 
          prev.pop(x)
      if find:
        break
          
   
    visited_nodes_in_order = [i for i in prev]
"""
'''
    def DFS(RJM, nodeA, goalNodex, goalNodey, reached):
        
        if(nodeA == (goalNodex, goalNodey)):
            reached.append(nodeA)
            return 1
        if(nodeA not in reached):
            reached.append(nodeA)
            neighbors = []
            
            getJump = RJM[nodeA[0]][nodeA[1]]
            
            if(nodeA[0]+getJump <= 4 and nodeA[0]+getJump >= 0):
                neighbors.append((nodeA[0]+getJump, nodeA[1]))
            if(nodeA[0]-getJump <= 4 and nodeA[0]-getJump >= 0):
                neighbors.append((nodeA[0]-getJump, nodeA[1]))
            if(nodeA[1]+getJump <= 4 and nodeA[1]+getJump >= 0):
                neighbors.append((nodeA[0], nodeA[1]+getJump))
            if(nodeA[1]-getJump <= 4 and nodeA[1]-getJump >= 0):
                neighbors.append((nodeA[0], nodeA[1]-getJump))
            
            for row, col in neighbors:
                newVal = (row, col)
                dog = DFS(RJM, newVal, goalNodex, goalNodey, reached)
               
                if(dog == 1):

                    return 1
                
    reached = []
  
    nodeA = ((0, 0))
    
    depth = DFS(RJM, nodeA, goalNodex, goalNodey, reached)
    
        def DFS(RJM, nodeA, goalNodex, goalNodey, reached, parent):
        
        
        if(nodeA == (goalNodex, goalNodey)):
            reached.append(nodeA)
            return 1
        if(nodeA not in reached):
            reached.append(nodeA)
            neighbors = []
            
            getJump = RJM[nodeA[0]][nodeA[1]]
            
            if(nodeA[0]+getJump <= 4 and nodeA[0]+getJump >= 0):
                neighbors.append((nodeA[0]+getJump, nodeA[1]))
            if(nodeA[0]-getJump <= 4 and nodeA[0]-getJump >= 0):
                neighbors.append((nodeA[0]-getJump, nodeA[1]))
            if(nodeA[1]+getJump <= 4 and nodeA[1]+getJump >= 0):
                neighbors.append((nodeA[0], nodeA[1]+getJump))
            if(nodeA[1]-getJump <= 4 and nodeA[1]-getJump >= 0):
                neighbors.append((nodeA[0], nodeA[1]-getJump))
            
            for row, col in neighbors:
                newVal = (row, col)
                parent.append(newVal)
                dog = DFS(RJM, newVal, goalNodex, goalNodey, reached, parent)
               
                if(dog == 1):

                    return 1
                
    reached = []
  
    nodeA = ((0, 0))
    
    parent = []
    
    depth = DFS(RJM, nodeA, goalNodex, goalNodey, reached, parent)
    
    print(parent)
    
    return depth
'''
    
import random


class Game:
    
    def RJM(self):
        
        
        def depthFinder(RJM, goalNodex, goalNodey):
            
            
            
            depth = 0
            
            x = 0
            y = 0
            
            
            def goalCalc(RJM, depth, currentx, currenty, goalNodex, goalNodey):
          
                frontier = []
                reached = []
                
                reached.append((0, 0))
                frontier.append((0, 0))
                john = {}
          
                while len(frontier)!=0:
                    find = False
                    nodeA = frontier.pop(0)
                    
                    getJump = RJM[nodeA[0]][nodeA[1]]
                    neighbors = []
                    
                    
                    if(nodeA[0]+getJump <= 4 and nodeA[0]+getJump >= 0):
                        neighbors.append((nodeA[0]+getJump, nodeA[1]))
                    if(nodeA[0]-getJump <= 4 and nodeA[0]-getJump >= 0):
                        neighbors.append((nodeA[0]-getJump, nodeA[1]))
                    if(nodeA[1]+getJump <= 4 and nodeA[1]+getJump >= 0):
                        neighbors.append((nodeA[0], nodeA[1]+getJump))
                    if(nodeA[1]-getJump <= 4 and nodeA[1]-getJump >= 0):
                        neighbors.append((nodeA[0], nodeA[1]-getJump))
                    
                    for row, col in neighbors:
                        newVal = (row, col)
                        if(newVal == (goalNodex, goalNodey)):
                            reached.append(newVal)
                            john[(row,col)] = nodeA
                            find = True
                            break
                        if(newVal not in reached):
                            john[(row,col)] = nodeA
                            reached.append(newVal)
                            frontier.append(newVal)
                          
                    
                    if find:
                        break
                if((goalNodex, goalNodey) not in reached):
                    return 1000000
                
                johnX = goalNodex
                johnY = goalNodey
                iterate = 0
                cat = True
                while cat:
                    iterate += 1
                    a = john[(johnX, johnY)]
                    for x in reversed(john):
                        if(x == a):
                            johnX = x[0]
                            johnY = x[1]
        
                    if a == (0, 0):        
                        cat = False
                
                return iterate
        
            depth = goalCalc(RJM, depth, x, y, goalNodex, goalNodey)    
          
           
            return depth
        
        
        def eval_RJM(RJM):
            
            dog = depthFinder(RJM, 4, 4)
            
            if(dog == 1000000):
                
                return 1000000
            
            else:
            
                return -dog
            
        def RJM_Copy(RJM):
            
            newRJM = [[0 for x in range(5)] for y in range(5)]  
            
            for x in range(5):
                for y in range(5):
                    newRJM[x][y] = RJM[x][y]
            
            
            return newRJM
            
        def step(RJM):
            
            
            newRJM = [[0 for x in range(5)] for y in range(5)]  
            
            for x in range(5):
                for y in range(5):
                    newRJM[x][y] = RJM[x][y]
            
            
            randomCordx = 0
            randomCordy = 0
            cat = True
            while(cat):
                
                randomCordx = random.randint(0, 4)
                randomCordy = random.randint(0, 4)
                
                if(randomCordx != 4):
                    if(randomCordy != 4):
                        cat = False
            
            
            oldNum = RJM[randomCordx][randomCordy]
            randomSize = 4
            var1 = randomSize - randomCordx
            var2 = randomCordx - 1
            var3 = randomSize - randomCordy
            var4 = randomCordy - 1
            
            var5 = max(var1, var2, var3, var4)
            
            
            
            cat = True
            while(cat):
                var6 = random.randint(1, var5)
                
                if(var6 != oldNum):
                    cat = False
                    
            
            newRJM[randomCordx][randomCordy] = var6 
            
          
            return newRJM
        
        def jumpReset():
            
            newRJM = [[0 for x in range(5)] for y in range(5)]  
            
            for i in range(5):
              for j in range(5):
                  var1 = 4 - i
                  var2 = i - 1
                  var3 = 4 - j
                  var4 = j - 1
                  var5 = max(var1, var2, var3, var4)
                  newRJM[i][j] = random.randint(1, var5)
            
            
            return newRJM
        
        def hill_Climb(RJM, iterations, initalTemp, decayRate):
           
            jump = jumpReset()
            jumpPrime = 0
            jBest = RJM_Copy(jump)
            temp = initialTemp
        
            notZero = True
            while(notZero):
                
                for x in range(iterations):
                    jumpPrime = step(jump)
                    probFunction = eval_RJM(jump) - eval_RJM(jumpPrime)
                    probFunction = probFunction / temp
                    euler = 2.7182
                    
                    newProb = 0
                    
                    if(eval_RJM(jumpPrime) > eval_RJM(jump)):
                        
                        newProb = euler**probFunction
                        
        
                    if(eval_RJM(jumpPrime) <= eval_RJM(jump) or newProb):
                            
                        jump = RJM_Copy(jumpPrime)
                            
                        if(eval_RJM(jumpPrime) <= eval_RJM(jBest)):
                                
                            jBest = RJM_Copy(jump)
                    
                    
                    temp = temp * decayRate
            
                if(eval_RJM(jBest) == 1000000):
                    jump = jumpReset()
                else:
                    notZero = False
                    
                    
            
            return jBest
            
        ################################################################################################
        
        iterations = input("Itearations? ")
        
        iterations = int(iterations)
        
        initialTemp = input("Initial temperature? ")
        
        initialTemp = int(initialTemp)
        
        decayRate = input("Decay rate? ")
        
        decayRate = float(decayRate)
        
        
        intputSize = 5
        
        randomSize = intputSize - 1
        RJM = [[0 for x in range(intputSize)] for y in range(intputSize)] 
        
        for i in range(intputSize):
          for j in range(intputSize):
              var1 = randomSize - i
              var2 = i - 1
              var3 = randomSize - j
              var4 = j - 1
              var5 = max(var1, var2, var3, var4)
              RJM[i][j] = random.randint(1, var5)
            
            
         
        RJM[randomSize][randomSize] = 0
        
        
        dog = hill_Climb(RJM, iterations, initialTemp, decayRate)
        
        
        
        for i in range(intputSize):
          for j in range(intputSize):
              print(dog[i][j], end = ' ')
          
          print("")
          
        
          
        BFS = [[0 for x in range(intputSize)] for y in range(intputSize)] 
        print("Moves from start:")
        
        
        
        for x in range(5):
            for y in range(5):
                
                if((x, y)) == (0, 0):
                    continue
                BFS[x][y] = depthFinder(dog, x, y)
                
                
        BFS[0][0] = 0
        
        for x in range(5):
            for y in range(5):
                
                j = BFS[x][y]
                if (j == 1000000):
                    print("--", end = ' ')
                else:    
                    print(j, end = ' ')
            print("")
        
        
        dog2 = eval_RJM(dog)
        print(dog2)

if __name__=='__main__':
    dog = Game()
    dog.RJM()