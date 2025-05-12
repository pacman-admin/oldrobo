'''
Copyright (c) 2020-2025 Langdon Staab, 2020-2022 Edison Wang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
print("Welcome to the Sudoku (数独) program")
try:
    import sys, os
    from random import randint, shuffle, sample
    from time import sleep
    from halo import Halo

    writePath = os.getcwd()
    writePath = writePath.replace('program_files', '')
    
    spinner = Halo(text='Loading', spinner='dots')
    counter = 0
    t1 = ''
    t2 = ''
    side = 9
    base = 3
    symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    printText = ['']
    printStr = ''
    wordStr = ''
    nums = []
    run = 1
    myrunning = True
    sy = 'g'
    difficulty = 'h'
    hardNum = 5
    printGrid = []
    ansStr = ''
    #initialise empty 9 by 9 grid
    grid = []

    def formatProb(grid2):
        printStr2 = ''
        nums = []
        for r in range(0,9):
            nums.append([])
            for c in range(0,10):
                nums[r].append('')
                if c == 0:
                  curNum = ''
                else:
                  curNum = str(grid2[r][c-1])
                  if curNum == '0':
                    curNum = ' '
                nums[r][c] += curNum
        printStr2 += f'\n{line0}'
        for r in range(1,side+1):
          t1 = ( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))))
          t2 = ([line2,line3,line4][(r%side==0)+(r%base==0)])
          printStr2 += f"\n{t1}\n{t2}"
        return printStr2
          
    def expandLine(line):
        return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:13]

    def gridInit():
      global grid
      grid = []
      grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
      grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
      grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
      grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
      grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
      grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
      grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
      grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
      grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    gridInit()


    class switch(object):
        value = None
        def __new__(class_, value):
            class_.value = value
            return True

    def case(*args):
        return any((arg == switch.value for arg in args))

    #A function to check if the grid is full
    def checkGrid(grid):
      for row in range(0,9):
          for col in range(0,9):
            if grid[row][col]==0:
              return False

      #We have a complete grid!
      return True

    #A backtracking/recursive function to check all possible combinations of numbers until a solution is found

    line0  = expandLine("╔═══╤═══╦═══╗")
    line1  = expandLine("║ . │ . ║ . ║")
    line2  = expandLine("╟───┼───╫───╢")
    line3  = expandLine("╠═══╪═══╬═══╣")
    line4  = expandLine("╚═══╧═══╩═══╝")

    numberList=[1,2,3,4,5,6,7,8,9]
    #shuffle(numberList)

    #A backtracking/recursive function to check all possible combinations of numbers until a solution is found
    def solveGrid(grid):
      global counter
      #Find next empty cell
      for i in range(0,81):
        row=i//9
        col=i%9
        if grid[row][col]==0:
          for value in range (1,10):
            #Check that this value has not already be used on this row
            if not(value in grid[row]):
              #Check that this value has not already be used on this column
              if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
                #Identify which of the 9 squares we are working on
                square=[]
                if row<3:
                  if col<3:
                    square=[grid[i][0:3] for i in range(0,3)]
                  elif col<6:
                    square=[grid[i][3:6] for i in range(0,3)]
                  else:  
                    square=[grid[i][6:9] for i in range(0,3)]
                elif row<6:
                  if col<3:
                    square=[grid[i][0:3] for i in range(3,6)]
                  elif col<6:
                    square=[grid[i][3:6] for i in range(3,6)]
                  else:  
                    square=[grid[i][6:9] for i in range(3,6)]
                else:
                  if col<3:
                    square=[grid[i][0:3] for i in range(6,9)]
                  elif col<6:
                    square=[grid[i][3:6] for i in range(6,9)]
                  else:  
                    square=[grid[i][6:9] for i in range(6,9)]
                #Check that this value has not already be used on this 3x3 square
                if not value in (square[0] + square[1] + square[2]):
                  grid[row][col]=value
                  if checkGrid(grid):
                    counter+=1
                    break
                  else:
                    if solveGrid(grid):
                      return True
          break
      grid[row][col]=0  
    def fillGrid(grid):
      global counter
      #Find next empty cell
      for i in range(0,81):
        row=i//9
        col=i%9
        if grid[row][col]==0:
          shuffle(numberList)
          for value in numberList:
            #Check that this value has not already be used on this row
            if not(value in grid[row]):
              #Check that this value has not already be used on this column
              if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
                #Identify which of the 9 squares we are working on
                square=[]
                if row<3:
                  if col<3:
                    square=[grid[i][0:3] for i in range(0,3)]
                  elif col<6:
                    square=[grid[i][3:6] for i in range(0,3)]
                  else:
                    square=[grid[i][6:9] for i in range(0,3)]
                elif row<6:
                  if col<3:
                    square=[grid[i][0:3] for i in range(3,6)]
                  elif col<6:
                    square=[grid[i][3:6] for i in range(3,6)]
                  else:
                    square=[grid[i][6:9] for i in range(3,6)]
                else:
                  if col<3:
                    square=[grid[i][0:3] for i in range(6,9)]
                  elif col<6:
                    square=[grid[i][3:6] for i in range(6,9)]
                  else:
                    square=[grid[i][6:9] for i in range(6,9)]
                #Check that this value has not already be used on this 3x3 square
                if not value in (square[0] + square[1] + square[2]):
                  grid[row][col]=value
                  if checkGrid(grid):
                    return True
                  else:
                    if fillGrid(grid):
                      return True
          break
      grid[row][col]=0
except ImportError as e:
    print("Import error.")
    print(e)
    pass
except Exception as e:
    print("An error has occured")
    print(e)
    pass

def makeSudoku(run):
    global counter
    global hardNum
    for i in range(run):
        #Generate a Fully Solved Grid
        print("Creating grid...")
        fillGrid(grid)
        #myPen.getscreen().update()
        sleep(0.01)
        ansStr = formatProb(grid)

        #Start Removing Numbers one by one

        #A higher number of attempts will end up removing more numbers from the grid
        #Potentially resulting in more difficiult grids to solve!
        print("Removing select numbers...")
        spinner.start()

        attempts = hardNum
        counter=1
        while attempts>0:
          #Select a random cell that is not already empty
          row = randint(0,8)
          col = randint(0,8)
          while grid[row][col]==0:
            row = randint(0,8)
            col = randint(0,8)
          #Remember its cell value in case we need to put it back
          backup = grid[row][col]
          grid[row][col]=0
          #Take a full copy of the grid
          copyGrid = []
          curNum = 0
          for r in range(0,9):
            copyGrid.append([])
            for c in range(0,9):
                copyGrid[r].append(grid[r][c])


          #Count the number of solutions that this grid has (using a backtracking approach implemented in the solveGrid() function)
          counter=0
          solveGrid(copyGrid)
          #If the number of solution is different from 1 then we need to cancel the change by putting the value we took away back in the grid
          if counter!=1:
            grid[row][col]=backup
            #We could stop here, but we can also have another attempt with a different cell just to try to remove more numbers
            attempts -= 1

        spinner.stop()
        print("Sudoku Grid Ready")
        

        
        printStr = formatProb(grid)
        if i%2 == 1 and i != 0 and not i >= run-1:
            for j in range(0, 16):
                printStr += '\n'
                ansStr += '\n'


        print(f'\n{printStr}\n')
        try:
            with open(f'{writePath}/sudoku.txt', 'a', encoding='utf-8') as printF:
                printF.write(printStr)
            with open(f"{writePath}/sudokuAnswer.txt", 'a', encoding='utf-8')as ansF:
                ansF.write(ansStr)
        except UnicodeEncodeError:
            print("Possible write error")
            wordStr = printStr
            for x in range(100):
                wordStr.replace('╦', '|')
                wordStr.replace('╗', '|')
                wordStr.replace('╔', '|')
                wordStr.replace('╫', 'H')
                wordStr.replace('╬', '|')
                wordStr.replace('╤', 'T')
                wordStr.replace('│', '|')
                wordStr.replace('┼', 't')

                wordStr.replace('─', '-')
                wordStr.replace('─', '-')
                wordStr.replace('║', '|')
                wordStr.replace('║', '|')
                wordStr.replace('═', '=')
                wordStr.replace('═', '=')
            
            with open(f'{writePath}sudoku.txt', 'a') as printF:
                printF.write(wordStr)

            print(wordStr)
        
        
        if run > 1:
            gridInit()
            printStr = ''


while myrunning:
  try:
    numOfProbs = 1
    sy = input("Type 'q' to quit, 'm' to make a new grid,\na number to make many sudokus, or any other key to continue")
    if sy == 'q':
      myrunning = False
      print('Exiting...')
      sleep(0.2)
      sys.exit(0)
    elif sy == 'm':
      gridInit()
      continue
    elif sy.isdigit():
        numOfProbs = int(sy)
    if True:
      myrunning = True
      difficulty = input('''Enter difficulty, type 'a' for answer, 'b' for beginner, 'm' for medium,
'h' for hard, 'e' for evil, or 'ENTER' to use the previous one''')
      while switch(difficulty):
        if case('b'):
          hardNum = 1
          print("You have selected beginner")
          break
        if case('m'):
          hardNum = 2
          print("You have selected medium")
          break
        if case('h'):
          hardNum = 5
          print("You have selected hard")
          break
        if case('e'):
          hardNum = 12
          print("You have selected evil")
          break
        if case('a'):
          hardNum = 0
          break
        if case(''):
            break
        hardNum = 'a'
        raise Exception('You entered an incorrect difficulty setting.')
    makeSudoku(numOfProbs)
    gridInit()
    difficulty = 'll'
  
      
  except KeyboardInterrupt:
      spinner.stop()
      print("Operation aborted by user\n")
      continue
  except SystemExit as status:
    sys.exit(status)
    
  except Exception as e:
    print("An error has occured.")
    print(e)

  
