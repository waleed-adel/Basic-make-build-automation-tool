import sys
from progressRecipe import progressBar
 
# the max size of progress bar
# represents number of all the files that the makefile generates 
MAXSIZE = sys.argv[1]

  
if sys.argv[1].isalpha():
  print ("usage: progress.py MAXSIZE = "+MAXSIZE)
else: 
  # 1- open the file 
  progressFileHandler=open("progress.txt","r")
  
  # 2- read the contents and save it to variable
  # this var. will be the size of the bar
  progressBarSize=progressFileHandler.read()
  
  # 3- close the file after finishing all operation on it
  progressFileHandler.close()
  
  # 4- drawing the bar with customized text
  # The total width parameter represents the current terminal width. If the
  # parameter is set to an integer then the progress bar will use that,
  # otherwise it will attempt to determine the terminal width falling back to
  # 75 columns if the width cannot be determined.  
  bar = progressBar(maxValue=int(MAXSIZE), totalWidth=60)
  bar.updateAmount(int(progressBarSize))
  bar.draw()
  print()