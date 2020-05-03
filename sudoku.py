from clSudoku import *
import os, random 
def main():
    s = Sudoku()
    
    #give user option to create their own board 
    ans = input("\nType Y if you wish to create your own board. Otherwise, continue by pressing any key. ")
    
    #if user wants to create their own, it will be saved as a file in folder
    if ans.lower() == 'y':
        fileName = s.createUserVersion() #creates and saves new sudoku board
        
    #if user wants to select a puzzle that is already available...
    else:
        fileName = input("Name of a puzzle?  If want to select random puzzle, press <ENTER> ")
        
        #user wants a random selected file
        if fileName == "":
            while True:
                
                #hidden files should be ignored.  Therefore needing to check
                #first character of file name.  If not . then we have a valid file
                try:
                    fileName = random.choice(os.listdir("."))
                    if fileName[0] != '.' and fileName.endswith('.txt'):
                        break
                except:
                    print("No files exist. Create one or move in a txt file from the program folder.")
                    return
         
        else:
             fileName = fileName + ".txt"
             
    #creates the board. 
    s.setupSudoku(fileName)
                
    #show the board
    s.displaySudoku()
    print("\nPuzzle file:", fileName)
    input("Take a look at puzzle before I solve it! <ENTER> to continue... " )

    #start the spinner and solve then turn off spinner
    s.startLoader()        
    solved = s.solveSudoku()
    s.stopLoader()
    
    #if solved - show resolved board
    if solved == True:
        print()
        print("\n\nSOLVED")
        s.displaySudoku()
        
    #else show that the board cannot be solved
    else:
        print("Do not waste time with this puzzle!  There is no solution.")
    
            
main()
