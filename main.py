import os
import signal
import time
from colorama import Fore, Back, init
from getch import _getChUnix as getChar
from alarmexception import AlarmException
from sys import exit

from board import Board
from paddle import Paddle
from scenery import Scenery
from ball import Ball
from bricks import Bricks
from powerup import Powerup
from finalBoss import Boss



obj_board= Board(30,200)
obj_board.createboard()
matrix=obj_board.getMatrix()

obj_scenery = Scenery()
obj_scenery.createBarH(matrix)
obj_scenery.createBarH2(matrix)
obj_scenery.createBarV1(matrix)
obj_scenery.createBarV2(matrix)


obj_bricks = Bricks()
level = obj_bricks.getlevel()

obj_ball = Ball()


L1 = 10
L2 = 12
L3 = 14
L4 = 8

# L1new= 10
# L2new = 12
# L3new = 14
# L4new = 8


def insertBrickslvl1():
    j = 50
    for i in range(0,3):
        obj_bricks.insertRedbrick(L1,j,matrix)
        # obj_bricks.insertRedbrick(10,60,matrix)
        # obj_bricks.insertRedbrick(10,70,matrix)
        # obj_bricks.insertRedbrick(10,80,matrix)
        # obj_bricks.insertRedbrick(10,90,matrix)
        # obj_bricks.insertRedbrick(10,100,matrix)
        # obj_bricks.insertRedbrick(10,110,matrix)
        # obj_bricks.insertRedbrick(10,120,matrix)
        # obj_bricks.insertRedbrick(10,130,matrix)
        # obj_bricks.insertRedbrick(10,140,matrix)
        # obj_bricks.insertRedbrick(10,150,matrix)

        obj_bricks.insertBluebrick(L2,j,matrix)
        # obj_bricks.insertBluebrick(12,60,matrix)
        # obj_bricks.insertBluebrick(12,70,matrix)
        # obj_bricks.insertBluebrick(12,80,matrix)
        # obj_bricks.insertBluebrick(12,90,matrix)
        # obj_bricks.insertBluebrick(12,100,matrix)
        # obj_bricks.insertBluebrick(12,110,matrix)
        # obj_bricks.insertBluebrick(12,120,matrix)
        # obj_bricks.insertBluebrick(12,130,matrix)
        # obj_bricks.insertBluebrick(12,140,matrix)
        # obj_bricks.insertBluebrick(12,150,matrix)

        obj_bricks.insertYellowbrick(L3,j,matrix)
        # obj_bricks.insertYellowbrick(14,60,matrix)
        # obj_bricks.insertYellowbrick(14,70,matrix)
        # obj_bricks.insertYellowbrick(14,80,matrix)
        # obj_bricks.insertYellowbrick(14,90,matrix)
        # obj_bricks.insertYellowbrick(14,100,matrix)
        # obj_bricks.insertYellowbrick(14,110,matrix)
        # obj_bricks.insertYellowbrick(14,120,matrix)
        # obj_bricks.insertYellowbrick(14,130,matrix)
        # obj_bricks.insertYellowbrick(14,140,matrix)
        # obj_bricks.insertYellowbrick(14,150,matrix)

        obj_bricks.insertUnbreakablebrick(L4,j,matrix)
        # obj_bricks.insertUnbreakablebrick(8,60,matrix)
        # obj_bricks.insertUnbreakablebrick(8,70,matrix)
        # obj_bricks.insertUnbreakablebrick(8,80,matrix)
        # obj_bricks.insertUnbreakablebrick(8,90,matrix)
        # obj_bricks.insertUnbreakablebrick(8,100,matrix)
        # obj_bricks.insertUnbreakablebrick(8,110,matrix)
        # obj_bricks.insertUnbreakablebrick(8,120,matrix)
        # obj_bricks.insertUnbreakablebrick(8,130,matrix)
        # obj_bricks.insertUnbreakablebrick(8,140,matrix)
        # obj_bricks.insertUnbreakablebrick(8,150,matrix)
        j = j+10

def movelvl1brick():
    j = 50
    for i in range(0,3):
        if(matrix[L1][j] != " "):
            obj_bricks.deleteBrick(L1,j,matrix)
            obj_bricks.insertRedbrick(obj_ball.getl1new(),j,matrix)
        if(matrix[L2][j] != " "):
            obj_bricks.deleteBrick(L2,j,matrix)
            obj_bricks.insertBluebrick(obj_ball.getl2new(),j,matrix)
        if(matrix[L3][j] != " "):
            obj_bricks.deleteBrick(L3,j,matrix)
            obj_bricks.insertYellowbrick(obj_ball.getl3new(),j,matrix)
        if(matrix[L4][j] != " "):
            obj_bricks.deleteBrick(L4,j,matrix)
            obj_bricks.insertUnbreakablebrick(obj_ball.getl4new(),j,matrix)
        j = j+10
    

def movelvl2brick():
    j = 50
    for i in range(0,6):
        if(matrix[L1][j] != " "):
            obj_bricks.deleteBrick(L1,j,matrix)
            obj_bricks.insertRedbrick(obj_ball.getl1new(),j,matrix)
        if(matrix[L2][j] != " "):
            obj_bricks.deleteBrick(L2,j,matrix)
            obj_bricks.insertBluebrick(obj_ball.getl2new(),j,matrix)
        if(matrix[L3][j] != " "):
            obj_bricks.deleteBrick(L3,j,matrix)
            obj_bricks.insertYellowbrick(obj_ball.getl3new(),j,matrix)
        if(matrix[L4][j] != " "):
            obj_bricks.deleteBrick(L4,j,matrix)
            obj_bricks.insertUnbreakablebrick(obj_ball.getl4new(),j,matrix)
        j = j+10

def movelvl3brick():
    j = 50
    for i in range(0,11):
        if(matrix[L1][j] != " "):
            obj_bricks.deleteBrick(L1,j,matrix)
            obj_bricks.insertRedbrick(obj_ball.getl1new(),j,matrix)
        if(matrix[L2][j] != " "):
            obj_bricks.deleteBrick(L2,j,matrix)
            obj_bricks.insertBluebrick(obj_ball.getl2new(),j,matrix)
        if(matrix[L3][j] != " "):
            obj_bricks.deleteBrick(L3,j,matrix)
            obj_bricks.insertYellowbrick(obj_ball.getl3new(),j,matrix)
        if(matrix[L4][j] != " "):
            obj_bricks.deleteBrick(L4,j,matrix)
            obj_bricks.insertUnbreakablebrick(obj_ball.getl4new(),j,matrix)
        j = j+10





def deletelvl1bricks():
    j = 50
    for i in range(0,3):
        obj_bricks.deleteBrick(L1,j,matrix)

        obj_bricks.deleteBrick(L2,j,matrix)

        obj_bricks.deleteBrick(L3,j,matrix)

        obj_bricks.deleteBrick(L4,j,matrix)

        j=j+10

def deletelvl2bricks():
    j = 50
    for i in range(0,6):
        obj_bricks.deleteBrick(L1,j,matrix)

        obj_bricks.deleteBrick(L2,j,matrix)

        obj_bricks.deleteBrick(L3,j,matrix)

        obj_bricks.deleteBrick(L4,j,matrix)

        j=j+10

def deletelvl3bricks():
    j = 50
    z1 = 50
    z2 = 100
    for i in range(0,11):
        obj_bricks.deleteBrick(L1,j,matrix)

        obj_bricks.deleteBrick(L2,j,matrix)

        obj_bricks.deleteBrick(L3,j,matrix)

        obj_bricks.deleteBrick(L4,j,matrix)

        j=j+10
    
    # for i in range(0,10):
    #     obj_bricks.deleteUnBrick(7,z1+i,matrix)
    #     obj_bricks.deleteUnBrick(7,z2+i,matrix)
    #     # obj_bricks.deleteUnBrick(11,z1+i,matrix)
    #     # obj_bricks.deleteUnBrick(11,z2+i,matrix)



def insertBrickslvl2():
    j = 50
    for i in range(0,6):
        obj_bricks.insertRedbrick(L1,j,matrix)

        obj_bricks.insertBluebrick(L2,j,matrix)

        obj_bricks.insertYellowbrick(L3,j,matrix)

        obj_bricks.insertUnbreakablebrick(L4,j,matrix)

        j=j+10

def insertBrickslvl3():
    j = 50
    for i in range(0,11):
        obj_bricks.insertRedbrick(L1,j,matrix)

        obj_bricks.insertBluebrick(L2,j,matrix)

        obj_bricks.insertYellowbrick(L3,j,matrix)

        obj_bricks.insertUnbreakablebrick(L4,j,matrix)

        j=j+10




# obj_bricks.insertexplosionbrick(7,50,matrix)
# obj_bricks.insertexplosionbrick(7,51,matrix)
# obj_bricks.insertexplosionbrick(7,52,matrix)
# obj_bricks.insertexplosionbrick(7,53,matrix)
# obj_bricks.insertexplosionbrick(7,54,matrix)
# obj_bricks.insertexplosionbrick(7,55,matrix)
# obj_bricks.insertexplosionbrick(7,56,matrix)
# obj_bricks.insertexplosionbrick(7,57,matrix)
# obj_bricks.insertexplosionbrick(7,58,matrix)
# obj_bricks.insertexplosionbrick(7,59,matrix)
# obj_bricks.insertexplosionbrick(7,100,matrix)
# obj_bricks.insertexplosionbrick(7,101,matrix)
# obj_bricks.insertexplosionbrick(7,102,matrix)
# obj_bricks.insertexplosionbrick(7,103,matrix)
# obj_bricks.insertexplosionbrick(7,104,matrix)
# obj_bricks.insertexplosionbrick(7,105,matrix)
# obj_bricks.insertexplosionbrick(7,106,matrix)
# obj_bricks.insertexplosionbrick(7,107,matrix)
# obj_bricks.insertexplosionbrick(7,108,matrix)
# obj_bricks.insertexplosionbrick(7,109,matrix)

# obj_bricks.insertexplosionbrick(11,50,matrix)
# obj_bricks.insertexplosionbrick(11,51,matrix)
# obj_bricks.insertexplosionbrick(11,52,matrix)
# obj_bricks.insertexplosionbrick(11,53,matrix)
# obj_bricks.insertexplosionbrick(11,54,matrix)
# obj_bricks.insertexplosionbrick(11,55,matrix)
# obj_bricks.insertexplosionbrick(11,56,matrix)
# obj_bricks.insertexplosionbrick(11,57,matrix)
# obj_bricks.insertexplosionbrick(11,58,matrix)
# obj_bricks.insertexplosionbrick(11,59,matrix)
# obj_bricks.insertexplosionbrick(11,100,matrix)
# obj_bricks.insertexplosionbrick(11,101,matrix)
# obj_bricks.insertexplosionbrick(11,102,matrix)
# obj_bricks.insertexplosionbrick(11,103,matrix)
# obj_bricks.insertexplosionbrick(11,104,matrix)
# obj_bricks.insertexplosionbrick(11,105,matrix)
# obj_bricks.insertexplosionbrick(11,106,matrix)
# obj_bricks.insertexplosionbrick(11,107,matrix)
# obj_bricks.insertexplosionbrick(11,108,matrix)
# obj_bricks.insertexplosionbrick(11,109,matrix)


# obj_bricks.insertRedbrick(12,100,matrix)



obj_powerup = Powerup()

obj_paddle = Paddle(27,90)
obj_boss = Boss(10,90)


x1 = 0
y1 = 0
alive = 1
spawn = 0

def movePaddle(char):
    [x,y]=obj_paddle.getPaddlecood()
    l = obj_paddle.getlengthofpad()
    if(char == 'a'):
        y = y-8
        if(y<=1):
            y=1
        
    if(char == 'd'):
        y = y + 8
        if(y>=199 - l):
            y=199 - l
    
    # if(char == 's'):
    #     shot = 1
        # obj_ball.shootBall()
    
    obj_paddle.setPaddlecood(x,y)

def take_input():
    
    def alarmhandler(signum, frame):
        raise AlarmException

    def user_input(timeout=0.05):
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)

        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''
    return user_input()


start_time=time.time()

stringis = ""

hasReachedlvl1 = 0
hasReachedlvl2 = 0
hasReachedlvl3 = 0
hasReachedboss = 0

Lvl1time = 0
Lvl2time = 0
Lvl3time = 0

working = True
while working:
    os.system('clear')

    stringis=""
    vartime = (round(time.time()) - round(start_time))
    stringis=stringis + "TIME :"+ str(vartime) +'          '
    stringis=stringis + "SCORE:"+ str(obj_ball.getscore())+'           '
    stringis=stringis + "LIVES:"+ str(obj_ball.getlives())+'           '
    stringis=stringis + "LEVEL:"+ str(obj_bricks.getlevel())+'           '
    if(hasReachedboss == 1):
        stringis=stringis + "BossLife:"+ str(obj_ball.getBosslife())+'           '
    if(obj_ball.getBosslife() == 0):
        print("GAME OVER BOI")
        working = False


    if(obj_powerup.getp1active()==1 and (vartime-obj_powerup.getp1activationtime())>10):
        obj_powerup.setp1active(0) 
        obj_powerup.p1redu(obj_paddle)
    if(obj_powerup.getp1active() ==1):
        stringis=stringis + "SHRINK:"+str(10-(vartime- obj_powerup.getp1activationtime()))+'        '

    if(obj_powerup.getp2active()==1 and (vartime-obj_powerup.getp2activationtime())>10):
        obj_powerup.setp2active(0) 
        obj_powerup.p2redu(obj_paddle)
    if(obj_powerup.getp2active() ==1):
        stringis=stringis + "ELONGATE:"+str(10-(vartime- obj_powerup.getp2activationtime()))+'        '

    if(obj_powerup.getp4active()==1 and (vartime-obj_powerup.getp4activationtime())>10):
        obj_powerup.setp4active(0) 
        obj_powerup.p4redu(obj_ball)
    if(obj_powerup.getp4active() ==1):
        stringis=stringis + "THRU-BALL:"+str(10-(vartime- obj_powerup.getp4activationtime()))+'        '

    if(obj_powerup.getp5active()==1 and (vartime-obj_powerup.getp5activationtime())>10):
        obj_powerup.setp5active(0) 
        obj_powerup.p5redu(obj_ball)
    if(obj_powerup.getp5active() ==1):
        stringis=stringis + "FAST-BALL:"+str(10-(vartime- obj_powerup.getp5activationtime()))+'        '

    if(obj_ball.getgrabball() == 1):
        stringis = stringis + "GRAB : ON" +'        '
    
    if(obj_ball.getlives()<0):
        print("GAME OVER BOI")
        working = False

    if((vartime - Lvl1time) > 15):
        if(hasReachedlvl1 == 1 and hasReachedlvl2 == 0):
            movelvl1brick()
            L1 = obj_ball.getl1new()
            L2 = obj_ball.getl2new()
            L3 = obj_ball.getl3new()
            L4 = obj_ball.getl4new()
            if(L3 > 25):
                print("GAME OVER BOI")
                working = False

    if((vartime - Lvl2time) > 30):
        if(hasReachedlvl2 == 1 and hasReachedlvl3 == 0):
            movelvl2brick()
            L1 = obj_ball.getl1new()
            L2 = obj_ball.getl2new()
            L3 = obj_ball.getl3new()
            L4 = obj_ball.getl4new()
            if(L3 > 25):
                print("GAME OVER BOI")
                working = False

    if((vartime - Lvl3time) > 30):
        if(hasReachedlvl3 == 1 and hasReachedboss == 0):
            movelvl3brick()
            L1 = obj_ball.getl1new()
            L2 = obj_ball.getl2new()
            L3 = obj_ball.getl3new()
            L4 = obj_ball.getl4new()
            if(L3 > 25):
                print("GAME OVER BOI")
                working = False
        

    if(obj_ball.getscore() == 12 and hasReachedlvl2 == 0):
        Lvl2time = vartime
        

        deletelvl1bricks()
        insertBrickslvl2()
        hasReachedlvl2 = 1
        obj_bricks.setlevel(2)
        obj_ball.setisShot(0)

        obj_powerup.setp1active(0) 
        obj_powerup.p1redu(obj_paddle)
        obj_powerup.setp2active(0) 
        obj_powerup.p2redu(obj_paddle)
        obj_powerup.setp4active(0) 
        obj_powerup.p4redu(obj_ball)
        obj_powerup.setp5active(0) 
        obj_powerup.p5redu(obj_ball)

        L1 = 10
        L2 = 12
        L3 = 14
        L4 = 8

        obj_ball.setl1new(10)
        obj_ball.setl2new(12)
        obj_ball.setl3new(13)
        obj_ball.setl4new(8)
    if(obj_ball.getscore() == 24 and hasReachedlvl3 == 0):
        Lvl3time = vartime
        

        deletelvl2bricks()
        insertBrickslvl3()
        hasReachedlvl3 = 1
        obj_bricks.setlevel(3)
        obj_ball.setisShot(0)


        obj_powerup.setp1active(0) 
        obj_powerup.p1redu(obj_paddle)
        obj_powerup.setp2active(0) 
        obj_powerup.p2redu(obj_paddle)
        obj_powerup.setp4active(0) 
        obj_powerup.p4redu(obj_ball)
        obj_powerup.setp5active(0) 
        obj_powerup.p5redu(obj_ball)

        L1 = 10
        L2 = 12
        L3 = 14
        L4 = 8

        obj_ball.setl1new(10)
        obj_ball.setl2new(12)
        obj_ball.setl3new(13)
        obj_ball.setl4new(8)
    if(obj_ball.getscore() == 44 and hasReachedboss == 0):
        

        deletelvl3bricks()
        hasReachedboss = 1

        obj_bricks.setlevel(4)
        obj_ball.setisShot(0)


        obj_powerup.setp1active(0) 
        obj_powerup.p1redu(obj_paddle)
        obj_powerup.setp2active(0) 
        obj_powerup.p2redu(obj_paddle)
        obj_powerup.setp4active(0) 
        obj_powerup.p4redu(obj_ball)
        obj_powerup.setp5active(0) 
        obj_powerup.p5redu(obj_ball)

        L1 = 10
        L2 = 12
        L3 = 14
        L4 = 8

        obj_ball.setl1new(10)
        obj_ball.setl2new(12)
        obj_ball.setl3new(13)
        obj_ball.setl4new(8)
    


    # stringis=stringis + "COINS:"+ str(obj_mando.getMandocoin()+ obj_bullet.getdragonscore())+'          '
    # stringis=stringis +"BULLETS:"+str(100-bulletcount)+'        '
    # stringis=stringis +"DRAGON LIVES:"+str(obj_bullet.getdragonlife())+"\n"
    # print(shot)
    matrix=obj_board.getMatrix()
    obj_board.setMatrix(matrix)

    obj_paddle.printPaddle(matrix)
    [x,y]=obj_paddle.getPaddlecood()
    if(hasReachedboss == 1):
        obj_boss.setbosscoor(10,y)
        obj_boss.printBoss(matrix)
    
    # v1 = obj_ball.isalive()
    # v2 = obj_ball.isonpaddle()

    if(obj_ball.getspawn() == 0):
        obj_ball.setspawn(1)
        obj_paddle.setrandno()
        
    if(obj_ball.getisShot() == 0):
        [x1,y1] = obj_paddle.getBallpos()
        obj_ball.setBall(x1,y1)
    else:
        # obj_ball.shootBall()
        [x1,y1] = obj_paddle.getPaddlecood()
        obj_ball.checkcoll(matrix,x1,y1,obj_powerup)

    [x1,y1] = obj_ball.getBall() 
    obj_ball.setBall(x1,y1)
    obj_ball.printBall(matrix)
    obj_powerup.movepowerups(matrix,obj_paddle,vartime,obj_ball)



    print(stringis)
    obj_board.printboard()

    obj_ball.deleteBall(matrix)
    obj_paddle.deletePaddle(matrix)
    obj_powerup.deletepowup(matrix)
    if(hasReachedboss == 1):
        obj_boss.deleteBoss(matrix)

    if(hasReachedlvl1 == 0):
        Lvl1time = vartime
        hasReachedlvl1 = 1
        insertBrickslvl1()

    

    char = take_input()

    movePaddle(char)

    if(char == "s"):
        obj_ball.setisShot(1)
    if(char == "n"):
        if(hasReachedlvl2 == 0):
            Lvl2time = vartime
            

            deletelvl1bricks()
            insertBrickslvl2()
            hasReachedlvl2 = 1
            obj_bricks.setlevel(2)
            obj_ball.setisShot(0)

            obj_powerup.setp1active(0) 
            obj_powerup.p1redu(obj_paddle)
            obj_powerup.setp2active(0) 
            obj_powerup.p2redu(obj_paddle)
            obj_powerup.setp4active(0) 
            obj_powerup.p4redu(obj_ball)
            obj_powerup.setp5active(0) 
            obj_powerup.p5redu(obj_ball)

            L1 = 10
            L2 = 12
            L3 = 14
            L4 = 8

            obj_ball.setl1new(10)
            obj_ball.setl2new(12)
            obj_ball.setl3new(13)
            obj_ball.setl4new(8)
        elif(hasReachedlvl2 == 1 and hasReachedlvl3 == 0):
            Lvl3time = vartime
            

            deletelvl2bricks()
            insertBrickslvl3()
            hasReachedlvl3 = 1
            obj_bricks.setlevel(3)
            obj_ball.setisShot(0)


            obj_powerup.setp1active(0) 
            obj_powerup.p1redu(obj_paddle)
            obj_powerup.setp2active(0) 
            obj_powerup.p2redu(obj_paddle)
            obj_powerup.setp4active(0) 
            obj_powerup.p4redu(obj_ball)
            obj_powerup.setp5active(0) 
            obj_powerup.p5redu(obj_ball)

            L1 = 10
            L2 = 12
            L3 = 14
            L4 = 8

            obj_ball.setl1new(10)
            obj_ball.setl2new(12)
            obj_ball.setl3new(13)
            obj_ball.setl4new(8)
        elif(hasReachedlvl3 == 1 and hasReachedboss == 0):
            

            deletelvl3bricks()
            hasReachedboss = 1

            obj_bricks.setlevel(4)
            obj_ball.setisShot(0)


            obj_powerup.setp1active(0) 
            obj_powerup.p1redu(obj_paddle)
            obj_powerup.setp2active(0) 
            obj_powerup.p2redu(obj_paddle)
            obj_powerup.setp4active(0) 
            obj_powerup.p4redu(obj_ball)
            obj_powerup.setp5active(0) 
            obj_powerup.p5redu(obj_ball)

            L1 = 10
            L2 = 12
            L3 = 14
            L4 = 8

            obj_ball.setl1new(10)
            obj_ball.setl2new(12)
            obj_ball.setl3new(13)
            obj_ball.setl4new(8)
            
        
    if(char == "q"):
        exit()























# import os

# # class screen:

# #     def __init__(self,x,y):
# #         self.__x = x
# #         self.__y = y
# #         self.__x = x

# class Board:
    
#     def __init__(self,rows, columns):
#         self.__rows=rows
#         self.__columns=columns
#         self.__matrix=[]
#         self.__boardstring=""

#     def getboardstring(self):
#         return self.__boardstring
#     def setboardstring(self,stringboard):
#         self.__boardstring=stringboard

#     def getBoarddim(self):
#         return [self.__rows, self.__columns]
#     def setBoarddim(self,rows,columns):
#         self.__rows=rows
#         self.__columns=columns

#     def getMatrix(self):
#         return self.__matrix
#     def setMatrix(self,grid):
#         self.__matrix=grid

#     def createboard(self):
        
#         for i in range(self.__rows):
#             c=1
#             temp=[]
#             for j in range(self.__columns):
#                 temp.append(" ")
#                 c=c+1
#                 if(c==10):
#                     c=1
#             self.__matrix.append(temp)
        
#     def printlines(self, leftmarg,rightmarg):
#         boardstring=""
#         for i in range(self.__rows):
#             for j in range(leftmarg,rightmarg):
#                 boardstring=boardstring+self.__matrix[i][j]
#                 #print(self.__matrix[i][j], end="")
#             #print()
#             boardstring=boardstring+"\n"
    
#         print(boardstring)


#     def printboard(self, mandopos):

#         if( mandopos>=0 and mandopos<=30):
#             self.printlines(0,120)
#         elif(mandopos>=self.__columns-120):
#             self.printlines(self.__columns-120,self.__columns)
#         else:
#             self.printlines(mandopos-30, mandopos+90)

# obj_board= Board(30,800)
# obj_board.createboard()
# matrix=obj_board.getMatrix()

# working = True
# while working:
    


