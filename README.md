# Basic make build automation tool
 With simple progress bar representation using make, python and batch all integrated with Eclipse.
 
 ## Steps:
 
 Step 0: Download our Final makefile environment from the following link:
		• https://drive.google.com/open?id=1E4031ShvNV4qow0DWqqnOqcRPZS8vy8Q
		
 Step 1: Progress Bar
	- Step 1.1 Progress Bar Model construction
		• Write file progress.bat to
		• read the value stored in progress.txt if it exists
		• Increment the read value
		• Store the new value in file progress.txt
		• If the file “progress.txt” does not exist then the batch file shall create it and write the value ‘1’ to it
		• End your script with an exit command
	- Step 1.2 Progress Bar View Construction
		• Write file progress.py to
		• Import the library progressBar.py (http://code.activestate.com/recipes/578228-progress-bar-class/
		• Read the input argument passed to progress.py which represents the maximum number for the progress bar
		• Don’t forget to validate your inputs (i.e the arguments passed to progress.py ), if not valid print 'usage: progress.py MAXSIZE'
		• Read the stored value in progress.txt
		• Draw the progress bar with value stored in progress.txt
	- Step 1.3 Progress Bar Controller Construction
		• Edit file makefile to
		• Call progress.bat each time it generates a file (Hint when calling the batch script use cmd /K "progress.bat").
		• Construct a variable containing all the files that the make file generates (i.e object files, dependency files, final application)
		• Call progress.py each time it generates a file with input argument “the number of all the files that the make file generates”
		• Reset the progress written in progress.txt (by writing 0) whenever you make clean or make all.
	
	- Check the output of the first step from the following path "ScreenShots/Step_1"
	
	- Step 2: Eclipse integration (The output of this step should be as shown below):
		• Step 2.1 Download “Grep Console” from eclipse marketplace
		• Step 2.2 Use the newly downloaded grep console
		• Write a regular expression that matches two capturing groups
		• The 1st capturing group is the progress bar
		• The 2nd capturing group is the progress percentage written after the progress bar
		• For the progress bar group make its forecolor the same as its background color (Anything except white)
		• For the progress percentage groups color it so that its forecolor and background color are different
		