# Slider 8 Puzzle

The purpose of this program is to solve 3x3 slider puzzles. If the puzzle is solvable,  
it is guaranteed to find the best possible solution for that specific search.  

### How does it work?

The user either selects the option to input the starting state (Ex: 783415602),  
or have the program generate a random starting state. The randomly generated  
starting states will always be solvable due to the fact that the generator  
starts with the goal state and applies a random number of valid moves to the  
board which results in a solvable puzzle every time.  

Once a starting state option has been selected, the user is then prompted to  
select which type of search they would like to perform.  

The options are as follows:  
[1] Breadth First Search  
[2] Depth First Search  
[3] A* Misplaced Tiles  
[4] A* Manhattan Distance  
[5] All  

After choosing one of these options, the program will proceed to find the valid  
solution with the shortest possible path. Once complete, the user will be shown  
the final path of the search (Unless depth first search was chosen. In that case  
the path is far too long.). The user will then be prompted if they would like to  
perform another search.  

There is also a test option on the first menu. If the user selects this option,  
the program will proceed to run each type of search ten times. Every type of  
search will use the same starting state and the starting state will change  
after all of the searches are complete. Once the test is complete,  
a CSV (Comma Seperated Values) file is generated and saved in the project  
directory. This file can be opened in Excel to view the results.  

### Usage

There are two options to download the source code.  
**Option 1**: Click the green 'Clone/Download' button and download the zip file.  
Extract the files and then you can open the project in your favorite IDE  
such as PyCharm.  

**Option 2**: Click the green 'Clone/Download' button and copy the http path.  
open the command prompt or terminal and navigate to where you want the code  
to be stored. Then type 'git clone {URL}'. When this is complete, you can  
cd into the project and type the command 'python .\main.py' to run the program.  
You also have the option of opening the project in your favorite IDE like in  
option 1.  
