import os 
import random
from colorama import Fore, Back, init


class Paddle:
    
    def __init__(self,xcood,ycood):
        self.__shape1 = "|"#Fore.RED + '='
        self.__shape2 = "["
        self.__shape3 = "]"
        self.__shape4 = "="
        self.__orglen = 100
        self.__lengthofpaddle = 30
        self.__x=xcood
        self.__y=ycood
        self.__randno = 0

    def getPaddlecood(self):
        return [self.__x, self.__y]
    def setPaddlecood(self,x,y):
        self.__x=x
        self.__y=y

    def setrandno(self):
        self.__randno = random.randint(0,self.__lengthofpaddle -1)

    def getBallpos(self):
        return [(self.__x - 1),(self.__y + self.__randno)]

    def getlengthofpad(self):
        return self.__lengthofpaddle

    def setlengthofpad(self,l):
        self.__lengthofpaddle = l

    def deletePaddle(self,matrix):
        # for i in range(self.__y, self.__y+self.__lengthofpaddle,1):
        for i in range(1, 199,1):
            matrix[self.__x][i] = " "

    def printPaddle(self,matrix):
        
        # obj_paddle = paddle
        # obj_paddle.deletePaddle(matrix)
        if(self.__y + self.__lengthofpaddle > 198):
            self.__y = self.__y - (self.__y + self.__lengthofpaddle - 199)
        
        for i in range(self.__y, self.__y+self.__lengthofpaddle,1):
            mid = int((self.__lengthofpaddle + 1)/2)

            if(i < self.__y + (mid-1)):
                matrix[self.__x][i] = self.__shape2
            elif(i > self.__y + (mid-1)):
                matrix[self.__x][i] = self.__shape3
            else:
                matrix[self.__x][i] = self.__shape1

    


    
        