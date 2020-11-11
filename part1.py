# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:31:52 2020

@author: airar
"""
import random

class Game:
    
    def RJM(self):
        
        inputSize = input("Rook Jumping Maze size (5-10)?")
            
        intputSize = int(inputSize)
            
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
            
        for i in range(intputSize):
            for j in range(intputSize):
                print(RJM[i][j], end = ' ')
              
            print("")
          
if __name__=='__main__':
    dog = Game()
    dog.RJM()