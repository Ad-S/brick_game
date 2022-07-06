import os 
import sys
import random
# from paddle import Paddle
from sys import exit
# from ball import Ball

class Powerup:

    def __init__(self):
        self.__pshape1 = "S"
        self.__pshape2 = "L"
        self.__pshape3 = "M"
        self.__pshape4 = "t"
        self.__pshape5 = "^"
        self.__pshape6 = "G"
        self.__p1fall = 0
        self.__p1x = 0
        self.__p1y = 0
        self.__p2fall = 0
        self.__p2x = 0
        self.__p2y = 0
        self.__p3fall = 0
        self.__p3x = 0
        self.__p3y = 0
        self.__p4fall = 0
        self.__p4x = 0
        self.__p4y = 0
        self.__p5fall = 0
        self.__p5x = 0
        self.__p5y = 0
        self.__p6fall = 0
        self.__p6x = 0
        self.__p6y = 0

        self.__p1activationtime = 0
        self.__p1active = 0

        self.__p2activationtime = 0
        self.__p2active = 0

        self.__p4activationtime = 0
        self.__p4active = 0

        self.__p5activationtime = 0
        self.__p5active = 0

        self.__p6activationtime = 0
        self.__p6active = 0

        self.__willFallFrom = 15


    def setfallfrom(self,x):
        self.__willFallFrom = x
    def getfallfrom(self):
        return self.__willFallFrom
    
    def getp1activationtime(self):
        return self.__p1activationtime
    def setp1activationtime(self,x):
        self.__p1activationtime = x

    def getp1active(self):
        return self.__p1active
    def setp1active(self,x):
        self.__p1active = x

    def p1redu(self,paddle):
        obj_paddle = paddle
        lenpad = obj_paddle.getlengthofpad()
        newlenpad = int(lenpad * 2)
        obj_paddle.setlengthofpad(newlenpad)

    def getp2activationtime(self):
        return self.__p2activationtime
    def setp2activationtime(self,x):
        self.__p2activationtime = x

    def getp2active(self):
        return self.__p2active
    def setp2active(self,x):
        self.__p2active = x

    def p2redu(self,paddle):
        obj_paddle = paddle
        lenpad = obj_paddle.getlengthofpad()
        newlenpad = int(lenpad/2)
        obj_paddle.setlengthofpad(newlenpad)

    def getp4activationtime(self):
        return self.__p4activationtime
    def setp4activationtime(self,x):
        self.__p4activationtime = x

    def getp4active(self):
        return self.__p4active
    def setp4active(self,x):
        self.__p4active = x

    def p4redu(self,ball):
        obj_ball = ball
        obj_ball.setthruball(0)

    def getp5activationtime(self):
        return self.__p5activationtime
    def setp5activationtime(self,x):
        self.__p5activationtime = x

    def getp5active(self):
        return self.__p5active
    def setp5active(self,x):
        self.__p5active = x

    def p5redu(self,ball):
        obj_ball = ball
        obj_ball.setspeedy(1)

    def getp6activationtime(self):
        return self.__p6activationtime
    def setp6activationtime(self,x):
        self.__p6activationtime = x

    def getp6active(self):
        return self.__p6active
    def setp6active(self,x):
        self.__p6active = x

    def p6redu(self,ball):
        obj_ball = ball
        obj_ball.setgrabball(0)

    def setcoorp1(self,x,y):
        self.__p1x = x
        self.__p1y = y
    
    def setcoorp2(self,x,y):
        self.__p2x = x
        self.__p2y = y

    def setcoorp3(self,x,y):
        self.__p3x = x
        self.__p3y = y
    
    def setcoorp4(self,x,y):
        self.__p4x = x
        self.__p4y = y

    def setcoorp5(self,x,y):
        self.__p5x = x
        self.__p5y = y

    def deletepowup(self,matrix):
        matrix[self.__p1x][self.__p1y] = " "
        matrix[self.__p2x][self.__p2y] = " "
        matrix[self.__p3x][self.__p3y] = " "
        matrix[self.__p4x][self.__p4y] = " "
        matrix[self.__p5x][self.__p5y] = " "
        matrix[self.__p6x][self.__p6y] = " "


    def movepowerups(self,matrix,paddle,time,ball):
        # print(self.__p1active)
        obj_paddle = paddle
        obj_ball = ball
        if(self.__p1fall == 1):
            self.__p1x = self.__p1x + 1
            if(matrix[self.__p1x][self.__p1y] == "[" or matrix[self.__p1x][self.__p1y] == "|" or matrix[self.__p1x][self.__p1y] == "]"):
                self.__p1fall = 0
                lenpad = obj_paddle.getlengthofpad()
                newlenpad = int(lenpad/2)
                obj_paddle.setlengthofpad(newlenpad)
                self.__p1active = 1
                self.__p1activationtime= time
            else:
                if(self.__p1x >= 28):
                    self.__p1fall = 0
                else:
                    if(matrix[self.__p1x][self.__p1y] == " "):
                        matrix[self.__p1x][self.__p1y] = self.__pshape1
                        # exit()
        
        if(self.__p2fall == 1):
            self.__p2x = self.__p2x + 1
            if(matrix[self.__p2x][self.__p2y] == "[" or matrix[self.__p2x][self.__p2y] == "|" or matrix[self.__p2x][self.__p2y] == "]"):
                self.__p2fall = 0
                lenpad = obj_paddle.getlengthofpad()
                newlenpad = int(lenpad * 2)
                obj_paddle.setlengthofpad(newlenpad)
                self.__p2active = 1
                self.__p2activationtime= time
            else:
                if(self.__p2x >= 28):
                    self.__p2fall = 0
                else:
                    if(matrix[self.__p2x][self.__p2y] == " "):
                        matrix[self.__p2x][self.__p2y] = self.__pshape2
                        # exit()


        if(self.__p3fall == 1):
            self.__p3x = self.__p3x + 1
            matrix[self.__p3x][self.__p3y] = self.__pshape3

        if(self.__p4fall == 1):
            self.__p4x = self.__p4x + 1
            if(matrix[self.__p4x][self.__p4y] == "[" or matrix[self.__p4x][self.__p4y] == "|" or matrix[self.__p4x][self.__p4y] == "]"):
                self.__p4fall = 0
                self.__p4active = 1
                self.__p4activationtime= time
                obj_ball.setthruball(1)
            else:
                if(self.__p4x + 1 >= 28):
                    self.__p4fall = 0
                else:
                    if(matrix[self.__p4x][self.__p4y] == " "):
                        matrix[self.__p4x][self.__p4y] = self.__pshape4

        if(self.__p5fall == 1):
            self.__p5x = self.__p5x + 1
            if(matrix[self.__p5x][self.__p5y] == "[" or matrix[self.__p5x][self.__p5y] == "|" or matrix[self.__p5x][self.__p5y] == "]"):
                self.__p5fall = 0
                self.__p5active = 1
                self.__p5activationtime= time
                # var1 = obj_ball.getspeedx()
                # var1 = int(var1 * 2)
                obj_ball.setspeedy(3)
            else:
                if(self.__p5x + 1 >= 28):
                    self.__p5fall = 0
                else:
                    if(matrix[self.__p5x][self.__p5y] == " "):
                        matrix[self.__p5x][self.__p5y] = self.__pshape5

        if(self.__p6fall == 1):
            self.__p6x = self.__p6x + 1
            if(matrix[self.__p6x][self.__p6y] == "[" or matrix[self.__p6x][self.__p6y] == "|" or matrix[self.__p6x][self.__p6y] == "]"):
                self.__p6fall = 0
                self.__p6active = 1
                self.__p6activationtime= time
                obj_ball.setgrabball(1)
            else:
                if(self.__p6x + 1 >= 28):
                    self.__p6fall = 0
                else:
                    if(matrix[self.__p6x][self.__p6y] == " "):
                        matrix[self.__p6x][self.__p6y] = self.__pshape6


        # return matrix


    def whichpowerup(self,bx,by,matrix,rnum):
        if((rnum == 1 or rnum==2 or rnum==3 or rnum==4) and self.__p1fall == 0 and self.__p1active == 0):
            self.__p1fall = 1
            # print("\033[40;1H")
            # print(self.__p1fall)
            # sys.exit()
            self.__p1x = self.__willFallFrom
            self.__p1y = by
            # matrix[bx][by] = self.__pshape1

        if((rnum == 5 or rnum==6 or rnum==7 or rnum==8) and self.__p2fall == 0 and self.__p2active == 0):
            self.__p2fall = 1
            self.__p2x = self.__willFallFrom
            self.__p2y = by

        if((rnum == 9 or rnum==10 or rnum==11 or rnum==12) and self.__p4fall == 0 and self.__p4active == 0):
            self.__p4fall = 1
            self.__p4x = self.__willFallFrom
            self.__p4y = by

        if(rnum == 13 and self.__p5fall == 0 and self.__p5active == 0):
            self.__p5fall = 1
            self.__p5x = self.__willFallFrom
            self.__p5y = by

        if((rnum == 16 or rnum==15 or rnum==14)  and self.__p6fall == 0):
            self.__p6fall = 1
            self.__p6x = self.__willFallFrom
            self.__p6y = by




