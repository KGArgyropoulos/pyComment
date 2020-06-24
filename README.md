**Comment python script's lines** \
Type down the lines you want to comment, comma (',') separated and with  '-' when you declare continuous line range\
(for example: 1,3,9-21,35)\
This will comment the lines 1,3,9,10,11,12,...20,21,35.\
You can also use this script if you just want to add a hashtag ("#") in front of some line in your text file.\
**Additional Note** \
With a slight code modification you can append anything you want in front of specific lines!\
Just open the source file (.py) \
Find and modify the line [temp = "#" + c] \
Change "#" with whatever you want to append in front of the line. \
E.g.: temp = "//" + c \
Save your changes and run it as explained below! \
FYI: This is actually the way you comment C programming language!

**_NOTE:_**  Windows version has Tkinter graphics

- commentIt.py is Linux compatible
    * execution command: $python3 commentIt.py
    * the Path is relevant to the folder where you downloaded the .py file
- commentWinIt.py is Windows compatible
    * execution command: $python commentWinIt.py
- commentWinIt.exe is the Windows executable
    * You will find it in https://github.com/KGArgyropoulos/pyComment/tree/master/commentWinIt/dist
    * Or! If you've already cloned this repo, the .exe will appear inside commentWinIt/dist/ folder.
    * double tap it to run!
