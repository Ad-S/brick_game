import random
import time
import signal
import os
from bricks import Bricks
from paddle import Paddle
from powerup import Powerup
from colorama import Fore, Back, init
from finalBoss import Boss

class Ball:

    def __init__(self):
        self.__ballshape = "o"
        self.__x = 0
        self.__y = 0
        self.__lives = 10
        self.__score = 0
        self.__speedx = -1
        self.__speedy = 1
        self.__thruball = 0
        self.__grabball = 0
        self.__isShot = 0
        self.__spawn = 0
        self.__Bosslife = 5
        self.__L1new = 10
        self.__L2new = 12
        self.__L3new = 14
        self.__L4new = 8
        # self.__onpaddle = 0
        # self.__alive = 0

    def getl1new(self):
        return self.__L1new

    def getl2new(self):
        return self.__L2new
    
    def getl3new(self):
        return self.__L3new
    
    def getl4new(self):
        return self.__L4new

    def getBosslife(self):
        return self.__Bosslife

    def setl1new(self,x):
        self.__L1new = x
    def setl2new(self,x):
        self.__L2new = x
    def setl3new(self,x):
        self.__L3new = x
    def setl4new(self,x):
        self.__L4new = x
    
    


    def setspeedy(self,y):
        self.__speedy = y
    def getspeedy(self):
        return self.__speedy
    
    def setisShot(self,x):
        self.__isShot = x
    def getisShot(self):
        return self.__isShot

    def getspawn(self):
        return self.__spawn
    def setspawn(self,x):
        self.__spawn = x

    def getgrabball(self):
        return self.__grabball

    def getthruball(self):
        return self.__thruball
    def setthruball(self,x):
        self.__thruball = x
    
    def getBall(self):
        return [self.__x,self.__y]
    def setBall(self,x,y):
        self.__x = x
        self.__y = y

    def setgrabball(self,x):
        self.__grabball = x

    def getscore(self):
        return self.__score

    def getlives(self):
        return self.__lives
    def setlives(self,x):
        self.__lives = x

    def printBall(self,matrix):
        matrix[self.__x][self.__y] = self.__ballshape

    def deleteBall(self,matrix):
        matrix[self.__x][self.__y] = " "

    # def shootBall(self):
        
    #     if(self.__x > 1 and self.__x < 26):
    #         self.__x = self.__x + self.__speedx
    #     else:
    #         self.__speedx = self.__speedx * -1
    #         self.__x = self.__x + self.__speedx

    #     if(self.__y > 1 and self.__y < 198):
    #         self.__y = self.__y + self.__speedy
    #     else:
    #         self.__speedy = self.__speedy * -1
    #         self.__y = self.__y + self.__speedy

    def checkcoll(self,matrix,px,py,pfunc):
        randno = random.randint(0,20)
        obj_bricks = Bricks()
        obj_paddle = Paddle(px,py)
        obj_powerup = pfunc
        obj_boss = Boss(px,py)

        # print("hello")
        # i think uppar vale collision ke vajay se ho rh out of bounds
        
        if(self.__x + self.__speedx >= 29 or self.__x + self.__speedx <= 1 or self.__y + self.__speedy <= 1 or self.__y + self.__speedy >= 198):
            
            if(self.__x + self.__speedx >= 29 or self.__x + self.__speedx <= 1):
                if(self.__x + self.__speedx == 29 or self.__x + self.__speedx > 29):
                    self.__lives = self.__lives - 1
                    self.__spawn = 0
                    self.__isShot = 0
                self.__speedx = self.__speedx * -1
            
            if(self.__y + self.__speedy <= 1 or self.__y + self.__speedy >= 198):
                self.__speedy = self.__speedy * -1
            
            self.__x = self.__x + self.__speedx
            self.__y = self.__y + self.__speedy
        
        elif( matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "[" or matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "]" or matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "|"):
            # print("HELLO")

            self.__L1new = self.__L1new + 1
            self.__L2new = self.__L2new + 1
            self.__L3new = self.__L3new + 1
            self.__L4new = self.__L4new + 1



            leng = obj_paddle.getlengthofpad()
            distfromc = 0

            if(self.__grabball == 1):
                self.__isShot = 0
                self.__grabball = 0
                # self.__x = self.__x + self.__speedx - 1
                # self.__y = self.__y + self.__speedy

            else:
                if( matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "["):
                    vary = self.__y + self.__speedy
                    while ( matrix[self.__x + self.__speedx][vary] == "["):
                        distfromc = distfromc + 1
                        vary = vary + 1

                    if(distfromc < int(leng/6)):
                        if(self.__speedy < 0):
                            self.__speedy = -1
                        else:
                            self.__speedy = 1
                    elif(distfromc < int(leng/3)):
                        if(self.__speedy < 0):
                            self.__speedy = -2
                        else:
                            self.__speedy = 2
                    elif(distfromc <= int(leng/2)):
                        if(self.__speedy < 0):
                            self.__speedy = -3
                        else:
                            self.__speedy = 3
                    self.__y = self.__y + self.__speedy
                    self.__speedx = self.__speedx * -1
                    self.__x = self.__x + self.__speedx
                
                elif( matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "]"):
                    vary = self.__y + self.__speedy
                    while ( matrix[self.__x + self.__speedx][vary] == "]"):
                        distfromc = distfromc + 1
                        vary = vary - 1
                    if(distfromc < int(leng/6)):
                        if(self.__speedy < 0):
                            self.__speedy = -1
                        else:
                            self.__speedy = 1
                    elif(distfromc < int(leng/3)):
                        if(self.__speedy < 0):
                            self.__speedy = -2
                        else:
                            self.__speedy = 2
                    elif(distfromc <= int(leng/2)):
                        if(self.__speedy < 0):
                            self.__speedy = -3
                        else:
                            self.__speedy = 3   

                    

                    self.__y = self.__y + self.__speedy
                    self.__speedx = self.__speedx * -1
                    self.__x = self.__x + self.__speedx
                
                elif( matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "|"):

                    if(self.__speedy < 0):
                        self.__speedy = -1
                    else:
                        self.__speedy = 1

                    self.__y = self.__y + self.__speedy
                    self.__speedx = self.__speedx * -1
                    self.__x = self.__x + self.__speedx


            # if(matrix[self.__x + self.__speedx][self.__y ] == "["  or matrix[self.__x + self.__speedx][self.__y ] == "]" or matrix[self.__x + self.__speedx][self.__y] == "|" ):
            #     if(matrix[self.__x + self.__speedx][self.__y ] == "["):

        elif(matrix[self.__x + self.__speedx][self.__y ] == "B" or matrix[self.__x + self.__speedx][self.__y ] == "O" or matrix[self.__x + self.__speedx][self.__y] == "S" or matrix[self.__x + self.__speedx][self.__y ] == "(" or matrix[self.__x + self.__speedx][self.__y ] == ")" or matrix[self.__x][self.__y + self.__speedy] == "B" or matrix[self.__x ][self.__y + self.__speedy] == "O" or matrix[self.__x ][self.__y + self.__speedy] == "S" or matrix[self.__x ][self.__y + self.__speedy] == "(" or  matrix[self.__x ][self.__y + self.__speedy] == ")" or matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "B" or matrix[self.__x + self.__speedx ][self.__y + self.__speedy] == "O" or matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "S" or matrix[self.__x + self.__speedx ][self.__y + self.__speedy] == "(" or matrix[self.__x + self.__speedx ][self.__y + self.__speedy] == ")"):
            
            os.system("aplay mixkit-fast-game-explosion-1688.wav > /dev/null 2>&1 &")

            if(matrix[self.__x + self.__speedx][self.__y ] == "B" or matrix[self.__x + self.__speedx][self.__y ] == "O" or matrix[self.__x + self.__speedx][self.__y] == "S" or matrix[self.__x + self.__speedx][self.__y ] == "(" or matrix[self.__x + self.__speedx][self.__y ] == ")"):
                self.__Bosslife = self.__Bosslife - 1
                if(self.__Bosslife == 0):
                    obj_boss.deleteBoss(matrix)
                    self.__score = self.__score + 1

                self.__y = self.__y + self.__speedy
                self.__speedx = self.__speedx * -1
                self.__x = self.__x + self.__speedx
            elif(matrix[self.__x][self.__y + self.__speedy] == "B" or matrix[self.__x ][self.__y + self.__speedy] == "O" or matrix[self.__x ][self.__y + self.__speedy] == "S" or matrix[self.__x ][self.__y + self.__speedy] == "(" or  matrix[self.__x ][self.__y + self.__speedy] == ")"):
                self.__Bosslife = self.__Bosslife - 1
                if(self.__Bosslife == 0):
                    obj_boss.deleteBoss(matrix)
                    self.__score = self.__score + 1

                self.__speedy = self.__speedy * -1
                self.__y = self.__y + self.__speedy
                # self.__speedx = self.__speedx * -1
                self.__x = self.__x + self.__speedx
            elif(matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "B" or matrix[self.__x + self.__speedx ][self.__y + self.__speedy] == "O" or matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "S" or matrix[self.__x + self.__speedx ][self.__y + self.__speedy] == "(" or matrix[self.__x + self.__speedx ][self.__y + self.__speedy] == ")"):
                self.__Bosslife = self.__Bosslife - 1
                if(self.__Bosslife == 0):
                    obj_boss.deleteBoss(matrix)
                    self.__score = self.__score + 1

                self.__speedy = self.__speedy * -1
                self.__y = self.__y + self.__speedy
                self.__speedx = self.__speedx * -1
                self.__x = self.__x + self.__speedx
            
            
        elif(matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "T" or matrix[self.__x ][self.__y + self.__speedy] == "T" or matrix[self.__x + self.__speedx][self.__y] == "T" ):
            
            os.system("aplay mixkit-fast-game-explosion-1688.wav > /dev/null 2>&1 &")
            
            if(matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "T"):
                varx = self.__x + self.__speedx
                vary = self.__y + self.__speedy
                
                # if(matrix[varx][vary] == "T"):
                matrix = obj_bricks.deleteUnBrick(varx,vary,matrix)
                v1 = varx
                v2 = vary
                if(matrix[v1 - 1][v2] != " "):
                    if(matrix[v1 - 1][v2] == "*"):
                        while (matrix[v1 -1][v2] == "*"):
                            v2 = v2 - 1
                    if(matrix[v1 - 1][v2] == "r"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1-1,v2,matrix)
                        obj_powerup.whichpowerup(v1-1,v2,matrix,randno)
                    elif(matrix[v1 - 1][v2] == "b"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1-1,v2,matrix)
                        obj_powerup.whichpowerup(v1-1,v2,matrix,randno)
                    elif(matrix[v1 - 1][v2] == "y"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1-1,v2,matrix)
                        obj_powerup.whichpowerup(v1-1,v2,matrix,randno)
                    elif(matrix[v1 - 1][v2] == "U"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1-1,v2,matrix)
                        obj_powerup.whichpowerup(v1-1,v2,matrix,randno)
                    elif(matrix[v1 - 1][v2] == "T"):
                        # self.__score = self.__score + 1
                        matrix = obj_bricks.deleteUnBrick(v1-1,v2,matrix)
                        obj_powerup.whichpowerup(v1-1,v2,matrix,randno)
                v1 = varx
                v2 = vary
                if(matrix[v1 + 1][v2] != " "):
                    if(matrix[v1 + 1][v2] == "*"):
                        while (matrix[v1 +1][v2] == "*"):
                            v2 = v2 - 1
                    if(matrix[v1 + 1][v2] == "r"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1+1,v2,matrix)
                        obj_powerup.whichpowerup(v1+1,v2,matrix,randno)
                    elif(matrix[v1 + 1][v2] == "b"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1+1,v2,matrix)
                        obj_powerup.whichpowerup(v1+1,v2,matrix,randno)
                    elif(matrix[v1 + 1][v2] == "y"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1+1,v2,matrix)
                        obj_powerup.whichpowerup(v1+1,v2,matrix,randno)
                    elif(matrix[v1 + 1][v2] == "U"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1+1,v2,matrix)
                        obj_powerup.whichpowerup(v1+1,v2,matrix,randno)
                    elif(matrix[v1 + 1][v2] == "T"):
                        # self.__score = self.__score + 1
                        matrix = obj_bricks.deleteUnBrick(v1+1,v2,matrix)
                        obj_powerup.whichpowerup(v1+1,v2,matrix,randno)

                v1 = varx
                v2 = vary
                if(matrix[v1][v2+1] != " "):
                    if(matrix[v1][v2+1] == "*"):
                        while (matrix[v1][v2+1] == "*"):
                            v2 = v2 - 1
                    if(matrix[v1][v2+1] == "r"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2+1,matrix)
                        obj_powerup.whichpowerup(v1,v2+1,matrix,randno)
                    elif(matrix[v1][v2+1] == "b"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2+1,matrix)
                        obj_powerup.whichpowerup(v1,v2+1,matrix,randno)
                    elif(matrix[v1][v2+1] == "y"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2+1,matrix)
                        obj_powerup.whichpowerup(v1,v2+1,matrix,randno)
                    elif(matrix[v1][v2+1] == "U"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2+1,matrix)
                        obj_powerup.whichpowerup(v1,v2+1,matrix,randno)
                    elif(matrix[v1][v2+1] == "T"):
                        # self.__score = self.__score + 1
                        matrix = obj_bricks.deleteUnBrick(v1,v2+1,matrix)
                        obj_powerup.whichpowerup(v1,v2+1,matrix,randno)

                v1 = varx
                v2 = vary
                if(matrix[v1][v2-1] != " "):
                    if(matrix[v1][v2-1] == "*"):
                        while (matrix[v1][v2-1] == "*"):
                            v2 = v2 - 1
                    if(matrix[v1][v2-1] == "r"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2-1,matrix)
                        obj_powerup.whichpowerup(v1,v2-1,matrix,randno)
                    elif(matrix[v1][v2-1] == "b"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2-1,matrix)
                        obj_powerup.whichpowerup(v1,v2-1,matrix,randno)
                    elif(matrix[v1][v2-1] == "y"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2-1,matrix)
                        obj_powerup.whichpowerup(v1,v2-1,matrix,randno)
                    elif(matrix[v1][v2-1] == "U"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2-1,matrix)
                        obj_powerup.whichpowerup(v1,v2-1,matrix,randno)
                    elif(matrix[v1][v2-1] == "T"):
                        # self.__score = self.__score + 1
                        matrix = obj_bricks.deleteUnBrick(v1,v2-1,matrix)
                        obj_powerup.whichpowerup(v1,v2-1,matrix,randno)
                
                if(self.__thruball == 1):
                    self.__y = self.__y + self.__speedy
                    self.__x = self.__x + self.__speedx
                
                else:
                    self.__speedy = self.__speedy * -1
                    self.__y = self.__y + self.__speedy
                    self.__speedx = self.__speedx * -1
                    self.__x = self.__x + self.__speedx

            if(matrix[self.__x][self.__y + self.__speedy] == "T"):
                varx = self.__x 
                vary = self.__y + self.__speedy
                
                # if(matrix[varx][vary] == "T"):
                matrix = obj_bricks.deleteUnBrick(varx,vary,matrix)
                v1 = varx
                v2 = vary
                if(matrix[v1 - 1][v2] != " "):
                    if(matrix[v1 - 1][v2] == "*"):
                        while (matrix[v1 -1][v2] == "*"):
                            v2 = v2 - 1
                    if(matrix[v1 - 1][v2] == "r"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1-1,v2,matrix)
                        obj_powerup.whichpowerup(v1-1,v2,matrix,randno)
                    elif(matrix[v1 - 1][v2] == "b"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1-1,v2,matrix)
                        obj_powerup.whichpowerup(v1-1,v2,matrix,randno)
                    elif(matrix[v1 - 1][v2] == "y"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1-1,v2,matrix)
                        obj_powerup.whichpowerup(v1-1,v2,matrix,randno)
                    elif(matrix[v1 - 1][v2] == "U"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1-1,v2,matrix)
                        obj_powerup.whichpowerup(v1-1,v2,matrix,randno)
                    elif(matrix[v1 - 1][v2] == "T"):
                        # self.__score = self.__score + 1
                        matrix = obj_bricks.deleteUnBrick(v1-1,v2,matrix)
                        obj_powerup.whichpowerup(v1-1,v2,matrix,randno)
                v1 = varx
                v2 = vary
                if(matrix[v1 + 1][v2] != " "):
                    if(matrix[v1 + 1][v2] == "*"):
                        while (matrix[v1 +1][v2] == "*"):
                            v2 = v2 - 1
                    if(matrix[v1 + 1][v2] == "r"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1+1,v2,matrix)
                        obj_powerup.whichpowerup(v1+1,v2,matrix,randno)
                    elif(matrix[v1 + 1][v2] == "b"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1+1,v2,matrix)
                        obj_powerup.whichpowerup(v1+1,v2,matrix,randno)
                    elif(matrix[v1 + 1][v2] == "y"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1+1,v2,matrix)
                        obj_powerup.whichpowerup(v1+1,v2,matrix,randno)
                    elif(matrix[v1 + 1][v2] == "U"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1+1,v2,matrix)
                        obj_powerup.whichpowerup(v1+1,v2,matrix,randno)
                    elif(matrix[v1 + 1][v2] == "T"):
                        # self.__score = self.__score + 1
                        matrix = obj_bricks.deleteUnBrick(v1+1,v2,matrix)
                        obj_powerup.whichpowerup(v1+1,v2,matrix,randno)

                v1 = varx
                v2 = vary
                if(matrix[v1][v2+1] != " "):
                    if(matrix[v1][v2+1] == "*"):
                        while (matrix[v1][v2+1] == "*"):
                            v2 = v2 - 1
                    if(matrix[v1][v2+1] == "r"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2+1,matrix)
                        obj_powerup.whichpowerup(v1,v2+1,matrix,randno)
                    elif(matrix[v1][v2+1] == "b"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2+1,matrix)
                        obj_powerup.whichpowerup(v1,v2+1,matrix,randno)
                    elif(matrix[v1][v2+1] == "y"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2+1,matrix)
                        obj_powerup.whichpowerup(v1,v2+1,matrix,randno)
                    elif(matrix[v1][v2+1] == "U"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2+1,matrix)
                        obj_powerup.whichpowerup(v1,v2+1,matrix,randno)
                    elif(matrix[v1][v2+1] == "T"):
                        # self.__score = self.__score + 1
                        matrix = obj_bricks.deleteUnBrick(v1,v2+1,matrix)
                        obj_powerup.whichpowerup(v1,v2+1,matrix,randno)

                v1 = varx
                v2 = vary
                if(matrix[v1][v2-1] != " "):
                    if(matrix[v1][v2-1] == "*"):
                        while (matrix[v1][v2-1] == "*"):
                            v2 = v2 - 1
                    if(matrix[v1][v2-1] == "r"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2-1,matrix)
                        obj_powerup.whichpowerup(v1,v2-1,matrix,randno)
                    elif(matrix[v1][v2-1] == "b"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2-1,matrix)
                        obj_powerup.whichpowerup(v1,v2-1,matrix,randno)
                    elif(matrix[v1][v2-1] == "y"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2-1,matrix)
                        obj_powerup.whichpowerup(v1,v2-1,matrix,randno)
                    elif(matrix[v1][v2+1] == "U"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteUnBrick(v1,v2+1,matrix)
                        obj_powerup.whichpowerup(v1,v2+1,matrix,randno)
                    elif(matrix[v1][v2+1] == "T"):
                        # self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2+1,matrix)
                        obj_powerup.whichpowerup(v1,v2+1,matrix,randno)
                
                if(self.__thruball == 1):
                    self.__y = self.__y + self.__speedy
                    self.__x = self.__x + self.__speedx
                
                else:
                    self.__speedy = self.__speedy * -1
                    self.__y = self.__y + self.__speedy
                    # self.__speedx = self.__speedx * -1
                    self.__x = self.__x + self.__speedx
                
            if(matrix[self.__x + self.__speedx][self.__y ] == "T"):
                varx = self.__x + self.__speedx
                vary = self.__y 
                
                # if(matrix[varx][vary] == "T"):
                matrix = obj_bricks.deleteUnBrick(varx,vary,matrix)
                v1 = varx
                v2 = vary
                if(matrix[v1 - 1][v2] != " "):
                    if(matrix[v1 - 1][v2] == "*"):
                        while (matrix[v1 -1][v2] == "*"):
                            v2 = v2 - 1
                    if(matrix[v1 - 1][v2] == "r"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1-1,v2,matrix)
                        obj_powerup.whichpowerup(v1-1,v2,matrix,randno)
                    elif(matrix[v1 - 1][v2] == "b"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1-1,v2,matrix)
                        obj_powerup.whichpowerup(v1-1,v2,matrix,randno)
                    elif(matrix[v1 - 1][v2] == "y"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1-1,v2,matrix)
                        obj_powerup.whichpowerup(v1-1,v2,matrix,randno)
                    elif(matrix[v1 - 1][v2] == "U"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1-1,v2,matrix)
                        obj_powerup.whichpowerup(v1-1,v2,matrix,randno)
                    elif(matrix[v1 - 1][v2] == "T"):
                        # self.__score = self.__score + 1
                        matrix = obj_bricks.deleteUnBrick(v1-1,v2,matrix)
                        obj_powerup.whichpowerup(v1-1,v2,matrix,randno)
                v1 = varx
                v2 = vary
                if(matrix[v1 + 1][v2] != " "):
                    if(matrix[v1 + 1][v2] == "*"):
                        while (matrix[v1 +1][v2] == "*"):
                            v2 = v2 - 1
                    if(matrix[v1 + 1][v2] == "r"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1+1,v2,matrix)
                        obj_powerup.whichpowerup(v1+1,v2,matrix,randno)
                    elif(matrix[v1 + 1][v2] == "b"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1+1,v2,matrix)
                        obj_powerup.whichpowerup(v1+1,v2,matrix,randno)
                    elif(matrix[v1 + 1][v2] == "y"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1+1,v2,matrix)
                        obj_powerup.whichpowerup(v1+1,v2,matrix,randno)
                    elif(matrix[v1 + 1][v2] == "U"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1+1,v2,matrix)
                        obj_powerup.whichpowerup(v1+1,v2,matrix,randno)
                    elif(matrix[v1 + 1][v2] == "T"):
                        # self.__score = self.__score + 1
                        matrix = obj_bricks.deleteUnBrick(v1+1,v2,matrix)
                        obj_powerup.whichpowerup(v1+1,v2,matrix,randno)

                v1 = varx
                v2 = vary
                if(matrix[v1][v2+1] != " "):
                    if(matrix[v1][v2+1] == "*"):
                        while (matrix[v1][v2+1] == "*"):
                            v2 = v2 - 1
                    if(matrix[v1][v2+1] == "r"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2+1,matrix)
                        obj_powerup.whichpowerup(v1,v2+1,matrix,randno)
                    elif(matrix[v1][v2+1] == "b"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2+1,matrix)
                        obj_powerup.whichpowerup(v1,v2+1,matrix,randno)
                    elif(matrix[v1][v2+1] == "y"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2+1,matrix)
                        obj_powerup.whichpowerup(v1,v2+1,matrix,randno)
                    elif(matrix[v1][v2+1] == "U"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2+1,matrix)
                        obj_powerup.whichpowerup(v1,v2+1,matrix,randno)
                    elif(matrix[v1][v2+1] == "T"):
                        # self.__score = self.__score + 1
                        matrix = obj_bricks.deleteUnBrick(v1,v2+1,matrix)
                        obj_powerup.whichpowerup(v1,v2+1,matrix,randno)

                v1 = varx
                v2 = vary
                if(matrix[v1][v2-1] != " "):
                    if(matrix[v1][v2-1] == "*"):
                        while (matrix[v1][v2-1] == "*"):
                            v2 = v2 - 1
                    if(matrix[v1][v2-1] == "r"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2-1,matrix)
                        obj_powerup.whichpowerup(v1,v2-1,matrix,randno)
                    elif(matrix[v1][v2-1] == "b"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2-1,matrix)
                        obj_powerup.whichpowerup(v1,v2-1,matrix,randno)
                    elif(matrix[v1][v2-1] == "y"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2-1,matrix)
                        obj_powerup.whichpowerup(v1,v2-1,matrix,randno)
                    elif(matrix[v1][v2-1] == "U"):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(v1,v2-1,matrix)
                        obj_powerup.whichpowerup(v1,v2-1,matrix,randno)
                    elif(matrix[v1][v2-1] == "T"):
                        # self.__score = self.__score + 1
                        matrix = obj_bricks.deleteUnBrick(v1,v2-1,matrix)
                        obj_powerup.whichpowerup(v1,v2-1,matrix,randno)
                
                if(self.__thruball == 1):
                    self.__y = self.__y + self.__speedy
                    self.__x = self.__x + self.__speedx
                
                else:
                    # self.__speedy = self.__speedy * -1
                    self.__y = self.__y + self.__speedy
                    self.__speedx = self.__speedx * -1
                    self.__x = self.__x + self.__speedx
                
    
        elif(matrix[self.__x + self.__speedx][self.__y ] == "*" or matrix[self.__x + self.__speedx][self.__y ] == "r" or matrix[self.__x + self.__speedx][self.__y] == "b" or matrix[self.__x + self.__speedx][self.__y ] == "y" or matrix[self.__x + self.__speedx][self.__y ] == "U" or matrix[self.__x][self.__y + self.__speedy] == "*" or matrix[self.__x ][self.__y + self.__speedy] == "r" or matrix[self.__x ][self.__y + self.__speedy] == "b" or matrix[self.__x ][self.__y + self.__speedy] == "y" or  matrix[self.__x ][self.__y + self.__speedy] == "U" or matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "*" or matrix[self.__x + self.__speedx ][self.__y + self.__speedy] == "r" or matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "b" or matrix[self.__x + self.__speedx ][self.__y + self.__speedy] == "y" or matrix[self.__x + self.__speedx ][self.__y + self.__speedy] == "U"):
                
            # print("hello")
            os.system("aplay mixkit-fast-game-explosion-1688.wav > /dev/null 2>&1 &")

            
            if(matrix[self.__x][self.__y + self.__speedy] == "*" or matrix[self.__x ][self.__y + self.__speedy] == "r" or matrix[self.__x ][self.__y + self.__speedy] == "b" or matrix[self.__x ][self.__y + self.__speedy] == "y" or matrix[self.__x ][self.__y + self.__speedy] == "U" ):   
                
                varx = self.__x 
                vary = self.__y + self.__speedy

                if(matrix[varx][vary] == "*"):
                    while (matrix[varx][vary] == "*"):
                        vary = vary - 1 

                if(matrix[varx][vary] == "r"):
                    if(self.__thruball == 1):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(varx,vary,matrix)
                        obj_powerup.whichpowerup(self.__x,self.__y+ self.__speedy,matrix,randno)
                    else:
                        matrix = obj_bricks.insertBluebrick(varx,vary,matrix)
                elif(matrix[varx][vary] == "b"):
                    if(self.__thruball == 1):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(varx,vary,matrix)
                        obj_powerup.whichpowerup(self.__x,self.__y+ self.__speedy,matrix,randno)
                    else:
                        matrix = obj_bricks.insertYellowbrick(varx,vary,matrix)
                elif(matrix[varx][vary] == "y"):
                    self.__score = self.__score + 1
                    matrix = obj_bricks.deleteBrick(varx,vary,matrix)
                    obj_powerup.whichpowerup(self.__x,self.__y+ self.__speedy,matrix,randno)
                elif(matrix[varx][vary] == "U"):
                    if(self.__thruball == 1):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(varx,vary,matrix)
                        obj_powerup.whichpowerup(self.__x,self.__y+ self.__speedy,matrix,randno)

                if(self.__thruball == 1):
                    self.__y = self.__y + self.__speedy
                    self.__x = self.__x + self.__speedx
                    
                else:
                    self.__speedy = self.__speedy * -1
                    self.__y = self.__y + self.__speedy
                    # self.__speedx = self.__speedx * -1
                    self.__x = self.__x + self.__speedx
            
            elif(matrix[self.__x + self.__speedx][self.__y ] == "*" or matrix[self.__x + self.__speedx][self.__y ] == "r" or matrix[self.__x + self.__speedx][self.__y] == "b" or matrix[self.__x + self.__speedx][self.__y ] == "y" or matrix[self.__x + self.__speedx][self.__y ] == "U"):   
                
                varx = self.__x + self.__speedx
                vary = self.__y 

                if(matrix[varx][vary] == "*"):
                    while (matrix[varx][vary] == "*"):
                        vary = vary - 1 

                if(matrix[varx][vary] == "r"):
                    if(self.__thruball == 1):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(varx,vary,matrix)
                        obj_powerup.whichpowerup(self.__x + self.__speedx,self.__y,matrix,randno)   
                    else:
                        matrix = obj_bricks.insertBluebrick(varx,vary,matrix)
                elif(matrix[varx][vary] == "b"):
                    if(self.__thruball == 1):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(varx,vary,matrix)
                        obj_powerup.whichpowerup(self.__x + self.__speedx,self.__y,matrix,randno)
                    else:
                        matrix = obj_bricks.insertYellowbrick(varx,vary,matrix)
                elif(matrix[varx][vary] == "y"):
                    self.__score = self.__score + 1
                    matrix = obj_bricks.deleteBrick(varx,vary,matrix)
                    obj_powerup.whichpowerup(self.__x + self.__speedx,self.__y,matrix,randno)
                elif(matrix[varx][vary] == "U"):
                    if(self.__thruball == 1):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(varx,vary,matrix)
                        obj_powerup.whichpowerup(self.__x + self.__speedx,self.__y,matrix,randno)


                if(self.__thruball == 1):
                    self.__y = self.__y + self.__speedy
                    self.__x = self.__x + self.__speedx

                else:
                    # self.__speedy = self.__speedy * -1
                    self.__y = self.__y + self.__speedy
                    self.__speedx = self.__speedx * -1
                    self.__x = self.__x + self.__speedx

            elif(matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "*" or matrix[self.__x + self.__speedx][self.__y + self.__speedy ] == "r" or matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "b" or matrix[self.__x + self.__speedx][self.__y + self.__speedy ] == "y" or matrix[self.__x + self.__speedx][self.__y + self.__speedy ] == "U"):   
                
                varx = self.__x + self.__speedx
                vary = self.__y + self.__speedy

                if(matrix[varx][vary] == "*"):
                    while (matrix[varx][vary] == "*"):
                        vary = vary - 1 

                if(matrix[varx][vary] == "r"):
                    if(self.__thruball == 1):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(varx,vary,matrix)
                        obj_powerup.whichpowerup(self.__x + self.__speedx,self.__y+ self.__speedy,matrix,randno)
                    else:
                        matrix = obj_bricks.insertBluebrick(varx,vary,matrix)
                elif(matrix[varx][vary] == "b"):
                    if(self.__thruball == 1):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(varx,vary,matrix)
                        obj_powerup.whichpowerup(self.__x + self.__speedx,self.__y+ self.__speedy,matrix,randno)
                    else:
                        matrix = obj_bricks.insertYellowbrick(varx,vary,matrix)
                elif(matrix[varx][vary] == "y"):
                    self.__score = self.__score + 1
                    matrix = obj_bricks.deleteBrick(varx,vary,matrix)
                    obj_powerup.whichpowerup(self.__x + self.__speedx,self.__y+ self.__speedy,matrix,randno)
                elif(matrix[varx][vary] == "U"):
                    if(self.__thruball == 1):
                        self.__score = self.__score + 1
                        matrix = obj_bricks.deleteBrick(varx,vary,matrix)
                        obj_powerup.whichpowerup(self.__x + self.__speedx,self.__y+ self.__speedy,matrix,randno)


                if(self.__thruball == 1):
                    self.__y = self.__y + self.__speedy
                    self.__x = self.__x + self.__speedx
                
                else:
                    self.__speedy = self.__speedy * -1
                    self.__y = self.__y + self.__speedy
                    self.__speedx = self.__speedx * -1
                    self.__x = self.__x + self.__speedx

        else:
            if(self.__x > 1 and self.__x < 28):
                    self.__x = self.__x + self.__speedx
            else:
                if(self.__x == 28 or self.__x > 28):
                    self.__lives = self.__lives - 1
                self.__speedx = self.__speedx * -1
                self.__x = self.__x + self.__speedx

            if(self.__y > 1 and self.__y < 198):
                self.__y = self.__y + self.__speedy
            else:
                self.__speedy = self.__speedy * -1
                self.__y = self.__y + self.__speedy

            
        
        # if(matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "*" or matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "r" or matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "b" or matrix[self.__x + self.__speedx][self.__y + self.__speedy] == "y" ):
        #     varx = self.__x + self.__speedx
        #     vary = self.__y 

        #     if(matrix[varx][vary] == "*"):
        #         while (matrix[varx][vary] == "*"):
        #             vary = vary - 1

        #     if(matrix[varx][vary] == "r"):
        #         matrix = obj_bricks.insertBluebrick(varx,vary,matrix)
        #     if(matrix[varx][vary] == "b"):
        #         matrix = obj_bricks.insertYellowbrick(varx,vary,matrix)
        #     if(matrix[varx][vary] == "y"):
        #         matrix = obj_bricks.deleteBrick(varx,vary,matrix)
            
        #     self.__speedx = self.__speedx * -1
        #     self.__x = self.__x + self.__speedx

        # if(matrix[self.__x][self.__y + 1] == "r" or matrix[self.__x][self.__y + 1] == "b" or matrix[self.__x][self.__y + 1] == "y" ):
        #     varx = self.__x
        #     vary = self.__y + 1
        
        #     if(matrix[self.__x ][self.__y + 1] == "r"):
        #         matrix = obj_bricks.insertBluebrick(varx,vary,matrix)
        #     if(matrix[self.__x ][self.__y + 1] == "b"):
        #         matrix = obj_bricks.insertYellowbrick(varx,vary,matrix)
        #     if(matrix[self.__x ][self.__y + 1] == "y"):
        #         matrix = obj_bricks.deleteBrick(varx,vary,matrix)
                
        #     self.__speedy = self.__speedy * -1
        #     self.__y = self.__y + self.__speedy    

        # if(matrix[self.__x][self.__y - 1] == "*"  ):
            
        #     varx = self.__x
        #     vary = self.__y - 1

        #     while (matrix[varx][vary] == "*"):
        #         vary = vary - 1

        #     if(matrix[varx][vary] == "r"):
        #         matrix = obj_bricks.insertBluebrick(varx,vary,matrix)
        #     if(matrix[varx][vary] == "b"):
        #         matrix = obj_bricks.insertYellowbrick(varx,vary,matrix)
        #     if(matrix[varx][vary] == "y"):
        #         matrix = obj_bricks.deleteBrick(varx,vary,matrix)

        #     self.__speedy = self.__speedy * -1
        #     self.__y = self.__y + self.__speedy

        




            # if(matrix[self.__x + 1][self.__y] == "r"):
                #     matrix = obj_bricks.insertBluebrick(self.__x + 1,self.__y,matrix)
                # if(matrix[self.__x + 1][self.__y] == "b"):
                #     matrix = obj_bricks.insertYellowbrick(self.__x + 1,self.__y,matrix)
                # if(matrix[self.__x + 1][self.__y] == "y"):
                #     matrix = obj_bricks.deleteBrick(self.__x + 1,self.__y,matrix)
            


                












# def isonpaddle(self):
    #     return self.__onpaddle
    # def setonpaddle(self,x):
    #     self.__onpaddle = x

    # def isalive(self):
    #     return self.__onpaddle
    # def setisalive(self,x):
    #     self.__alive = x