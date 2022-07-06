import os
import random
from colorama import Fore, Back, init

class Boss:

    def __init__(self,xcood,ycood):
        self.__shape1 = "("
        self.__shape2 = ")"
        self.__shape3 = "B"
        self.__shape4 = "O"
        self.__shape5 = "S"
        self.__x=10
        self.__y=ycood

    def getbosscoor(self):
        return [self.__x, self.__y]

    def setbosscoor(self,x,y):
        self.__x=x
        self.__y=y

    def deleteBoss(self,matrix):
        matrix[self.__x][self.__y] = " "
        matrix[self.__x][self.__y + 1] = " "
        matrix[self.__x][self.__y + 2] = " "
        matrix[self.__x][self.__y + 3] = " "
        matrix[self.__x][self.__y + 4] = " "
        matrix[self.__x][self.__y + 5] = " "
        
    def printBoss(self,matrix):
        matrix[self.__x][self.__y] = self.__shape1
        matrix[self.__x][self.__y + 1] = self.__shape3
        matrix[self.__x][self.__y + 2] = self.__shape4
        matrix[self.__x][self.__y + 3] = self.__shape5
        matrix[self.__x][self.__y + 4] = self.__shape5
        matrix[self.__x][self.__y + 5] = self.__shape2
        
