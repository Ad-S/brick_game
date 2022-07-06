import os
from colorama import * #Fore, Back, init

class Bricks:

    def __init__(self):
        self.__nope = " "
        self.__level = 1

    def setlevel(self,x):
        self.__level = x
    def getlevel(self):
        return self.__level
    
    def insertRedbrick(self,xcod,ycod,matrix):
        self.__s1 = 'r'
        self.__s2 = '*'
        self.__s3 = '*'
        self.__s4 = '*'
        self.__s5 = '*' #+ Style.RESET_ALL + ''


        matrix[xcod][ycod] = self.__s1
        matrix[xcod][ycod+1] = self.__s2
        matrix[xcod][ycod+2] = self.__s3
        matrix[xcod][ycod+3] = self.__s4
        matrix[xcod][ycod+4] = self.__s5

        return matrix


    def insertBluebrick(self,xcod,ycod,matrix):
        self.__s1 = 'b'
        self.__s2 = '*'
        self.__s3 = '*'
        self.__s4 = '*'
        self.__s5 = '*' #+ Style.RESET_ALL + ''


        matrix[xcod][ycod] = self.__s1
        matrix[xcod][ycod+1] = self.__s2
        matrix[xcod][ycod+2] = self.__s3
        matrix[xcod][ycod+3] = self.__s4
        matrix[xcod][ycod+4] = self.__s5

        return matrix

    def insertYellowbrick(self,xcod,ycod,matrix):
        self.__s1 = 'y'
        self.__s2 = '*'
        self.__s3 = '*'
        self.__s4 = '*'
        self.__s5 = '*' #+ Style.RESET_ALL + ''


        matrix[xcod][ycod] = self.__s1
        matrix[xcod][ycod+1] = self.__s2
        matrix[xcod][ycod+2] = self.__s3
        matrix[xcod][ycod+3] = self.__s4
        matrix[xcod][ycod+4] = self.__s5

        return matrix

    def insertUnbreakablebrick(self,xcod,ycod,matrix):
        self.__s1 = 'U'
        self.__s2 = '*'
        self.__s3 = '*'
        self.__s4 = '*'
        self.__s5 = '*' #+ Style.RESET_ALL + ''


        matrix[xcod][ycod] = self.__s1
        matrix[xcod][ycod+1] = self.__s2
        matrix[xcod][ycod+2] = self.__s3
        matrix[xcod][ycod+3] = self.__s4
        matrix[xcod][ycod+4] = self.__s5

        return matrix

    def insertexplosionbrick(self,xcod,ycod,matrix):
        self.__s1 = 'T'

        matrix[xcod][ycod] = self.__s1

        return matrix
    
    def deleteBrick(self,xcod,ycod,matrix):

        matrix[xcod][ycod] = " "
        matrix[xcod][ycod+1] = " "
        matrix[xcod][ycod+2] = " "
        matrix[xcod][ycod+3] = " "
        matrix[xcod][ycod+4] = " "

        return matrix

    def deleteUnBrick(self,xcod,ycod,matrix):
    
        matrix[xcod][ycod] = " "

        return matrix

    
