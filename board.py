import os
from colorama import * #Fore, Back, init


class Board:

    def __init__(self,rows,columns):
        self.__rows=rows
        self.__columns=columns
        self.__matrix=[]

    def getMatrix(self):
        return self.__matrix
    def setMatrix(self,grid):
        self.__matrix=grid

    def createboard(self):

        for i in range(self.__rows):
            temp = []
            for j in range(self.__columns):
                temp.append(" ")
            self.__matrix.append(temp)
    
    def printLines(self):

        boardstring=""
        for i in range(self.__rows):
            for j in range(self.__columns):
                if(self.__matrix[i][j] == "r"):
                    for t in range(j,j+5):
                        boardstring = boardstring + Fore.RED + self.__matrix[i][t] + Style.RESET_ALL + ''
                    # j = j+5
                
                elif(self.__matrix[i][j] == "b"):
                    for t in range(j,j+5):
                        boardstring = boardstring + Fore.BLUE + self.__matrix[i][t] + Style.RESET_ALL + ''
                    # j = j+5

                elif(self.__matrix[i][j] == "y"):
                    for t in range(j,j+5):
                        boardstring = boardstring + Fore.YELLOW + self.__matrix[i][t] + Style.RESET_ALL + ''
                    # j = j+5
                
                elif(self.__matrix[i][j] == "U"):
                    for t in range(j,j+5):
                        boardstring = boardstring + self.__matrix[i][t] + Style.RESET_ALL + ''
                
                elif(self.__matrix[i][j] == "T"):
                    boardstring = boardstring + Fore.GREEN + self.__matrix[i][j] + Style.RESET_ALL + ''

                elif(self.__matrix[i][j] != "*"):
                    boardstring=boardstring+self.__matrix[i][j]
                #print(self.__matrix[i][j], end="")
            #print()
            boardstring=boardstring+"\n"
    
        print(boardstring)
        print(Style.RESET_ALL,end = '')

    def printboard(self):
        self.printLines()
        # print(self.__matrix[10][107])
        # print(self.__matrix[10][108])


    
        