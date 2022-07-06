import os
import random
from colorama import init,Fore,Back

class Scenery:

    def __init__(self):
        
        self.__barH = []
        self.__barV = []

    def  createBarH(self,matrix):

        for i in range(200):
            #matrix[29][i]=random.randint(0,9)
            #matrix[28][i]=random.randint(0,9)
            # matrix[29][i]= Fore.WHITE+"%"+'\x1b[0m'
            matrix[29][i]= Fore.GREEN+ Back.GREEN+"%"+'\x1b[0m'

    def  createBarH2(self,matrix):
    
        for i in range(200):
            #matrix[29][i]=random.randint(0,9)
            #matrix[28][i]=random.randint(0,9)
            # matrix[0][i]= Fore.WHITE+"%"+'\x1b[0m'
            # matrix[0][i]= Fore.GREEN + Back.GREEN+"%"+'\x1b[0m'
            matrix[0][i]= Fore.MAGENTA+Back.MAGENTA+"%" + '\x1b[0m'


    def createBarV1(self, matrix):
        for i in range(30):
            #matrix[0][i]=random.randint(0,9)
            #matrix[1][i]=random.randint(0,9)
            # matrix[0][i]= Fore.WHITE+"%" +'\x1b[0m'
            matrix[i][0]= Fore.MAGENTA+Back.MAGENTA+"%" + '\x1b[0m'

    def createBarV2(self, matrix):
        for i in range(30):
            #matrix[0][i]=random.randint(0,9)
            #matrix[1][i]=random.randint(0,9)
            # matrix[0][i]= Fore.WHITE+"%" +'\x1b[0m'
            matrix[i][199]= Fore.MAGENTA+Back.MAGENTA+"%" + '\x1b[0m'
