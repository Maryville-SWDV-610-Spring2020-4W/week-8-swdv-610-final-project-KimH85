from clLoader import Loader
import random
class Sudoku:
    def __init__(self):
        self.size = 9
        self.puzzle = []
        self.loader = Loader()
        
    #create the sudoku board based on user input
    def createUserVersion(self):
        
        print("\nCreate your own board - valid entries are 1 - %d or 'nothing' for the blank" % (self.size))
        
        #interate through 9 versions of a row
        for i in range(0,self.size):
            r = []
            self.puzzle.append(r) #add new row to puzzle
            
            #iterate through 9 versions of a column
            for j in range(0,self.size):
                
                #enter in each square's value
                while True:
                    try:
                        val = input("Enter value for square %d %d: " % (i+1, j+1))
                        if val == "":
                            r.append(0)
                            break
                        else:
                            if int(val) < 1 or int(val) > 9:
                                print("Must enter an integer between 1-9 or leave blank. Try again.\n")
        
                            else:
                                r.append(int(val))
                                break                        
                    except:
                        print("Must enter an integer between 1-9 or leave blank. Try again.\n")
        
        
        
        #create the file 
        while True:
            try:
                fileName = input('What do you want to call this puzzle? ')

                #save the content entered into a file name that the user enters
                f = open(fileName+'.txt', 'x')
                break

            except:
                print('Invalid file name.  Try again.')
            
        #create each line and write to the file
        for r in self.puzzle:
            line = ''
            for c in r:
                if line == '':
                    line = str(c)
                else:
                    line = line+','+str(c)

            f.write(line+'\r')
        
        f.close()
        return fileName+'.txt'
    
    #sets up the sudoku puzzle
    def setupSudoku(self, fileName):
        
        #opening the file storing the puzzle
        puzzleFile = open(fileName, 'r')
        
        for l in puzzleFile:
            rList = []
            newRow = l.strip()
            
            #load each column into row and append to the row list
            for c in newRow:
                
                if c != ',':
                    rList.append(int(c))
            
            self.puzzle.append(rList)

        puzzleFile.close()

    #prints the sudoku board
    def displaySudoku(self):
        
        #loop through the rows
        for r in range(0,self.size):
            
            #for each row determine if about to print next square
            #if so show the square top / bottom border
            if r % 3 == 0:
                print()
                print('===='*self.size)
            else:
                print()
            
            #loop through the columns within the row
            for c in range(0,self.size):
                #if number is 0 - do not print anything.  otherwise show number in puzzle
                #also for each column determine if about to print next square. if so, show border
                print(" " if self.puzzle[r][c] == 0 else self.puzzle[r][c], end=" \u2016 " if c % 3 == 2 else "   ")
                        
        print()
        print('===='*self.size)
        
    #recursively called with new puzzle board to evaluate
    def solveSudoku(self):
        
        #returns row,col of next empty block in puzzle
        next_to_assign = self.getNextUnassigned()
        
        if next_to_assign[0] == -1:
            return True
        
        empty_block_row = next_to_assign[0]
        empty_block_col = next_to_assign[1]
        
        #loop 1-9 looking for a valid valud to put in empty block
        for next_number_to_try in range(1,10):
            
            #determine if valid value
            if self.checkIsValid(next_number_to_try, empty_block_row, empty_block_col):
                
                #if valid, then set that block with the new number
                self.puzzle[empty_block_row][empty_block_col] = next_number_to_try
                
                #recursively call with new puzzle update
                if self.solveSudoku():
                    return True
                
                #if we get here - reset the unassigned square to 0.
                #get next number to try in the unassigned square
                self.puzzle[empty_block_row][empty_block_col]=0
        
        #if get here - next unassigned square was not solved.
        #this will then start to unwind to the prior square solution - updating it to
        #next value.  This is a form of a backtracking algorithm that uses recursive calls
        #to placehold each square's value and where in the loop it continues
        return False
    
    #loops through each row/column looking for value=0
    #returns row/col combination when found.
    #if not found, returns -1,-1
    def getNextUnassigned(self):
        for r in range(0,self.size):
            for c in range (0,self.size):
                
                if self.puzzle[r][c] == 0: #block with no number assigned
                    return [r,c]
        
        #did not find any unassigned blocks
        return [-1, -1]

    #loops row/col/square looking for that number.  If found,
    #returns that the value is invalid.  Else returns that it is valid.
    def checkIsValid(self, n, r, c):
        
        #checking in each column in the 'r' for value matching 'n'
        for each_col_in_row in range(0,self.size):
            
            #found match - makes the number invalid.
            if self.puzzle[r][each_col_in_row] == n:
                return False
            
        #checking in each row in the 'c' for value matching 'n'
        for each_row_in_col in range(0,self.size):
            
            #found match - makes the number invalid.
            if self.puzzle[each_row_in_col][c] == n:
                return False
        
        #determine what block 'r','c' fall in
        block_row_start = r//3 * 3
        block_col_start = c//3 * 3;
        
        #checking in block for value matching 'n'
        for each_row_in_block in range(block_row_start,block_row_start + 3):
            for each_col_in_block in range(block_col_start,block_col_start + 3):

                #found match - makes the number invalid.
                if self.puzzle[each_row_in_block][each_col_in_block]==n:
                    return False
                
        #number is valid
        return True

    def startLoader(self):
        self.loader.start()

    def stopLoader(self):
        self.loader.stop()