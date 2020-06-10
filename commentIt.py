import readline,os,string

# filename is the path to the file we want to comment
filename = input("Welcome! Now please type the path to the file you want to comment: " )

with open(filename) as f:
        content = f.readlines()
content = [x for x in content]
f.close()

# lineList contains every line we want to comment
lines = input("Great! Now please write down the lines you want to comment, comma (',') separated and with  '-' when you declare continuous line range (for example: 1,3,9-21,35): ")
individualLines = lines.split(",")

lineList = []
for i in individualLines:
	if '-' in i:
		x = i.split("-")[0]
		y = i.split("-")[1]
		tempList = list(range(int(x),int(y)+1))
		for j in tempList:
			lineList.append(j)
	else:
		lineList.append(int(i))

# Now let's modify the line

commentedText = []
i=0
for c in content:
	i = i + 1
	if i in lineList:
		temp = "#" + c
		commentedText.append(temp)
	else:
		commentedText.append(c)

with open(filename, 'w+') as f:
    for item in commentedText:
        f.write("%s" % item)
f.close()

#######TASKS#######
## 1. The path should be absolute
##	  It should also be both Linux and Windows compatible
## 2. Error handling messages
## 3. Clear the Code (will be github contributed)
## 4. Test cases
