import os,string
from tkinter import *
from tkinter import filedialog

class Root(Tk):
	filename = ""
	def __init__(self, stage):
		super(Root, self).__init__()
		self.labelFrame = Label(self, text="HashApp", font=("Arial Bold", 25))
		self.labelFrame.grid(column=0, row=0)

		if stage == "Path":
			self.pathButton()
		else:
			self.lineButton()

	def lineButton(self):
		self.label = Label(self, text = "Great! Now please write down the lines you want to comment, comma (',') separated and with  '-' when you declare continuous line range (for example: 1,3,9-21,35): ", font=("Arial Bold", 10))
		self.label.grid(column = 0, row = 1)
		self.content = StringVar()
		entry = Entry(self, textvariable=self.content).grid(column = 0, row = 2)
		self.button = Button(self, text = "DONE", bg="black", fg="white",command = self.done)
		self.button.grid(column = 0, row = 3)

	def done(self):
		self.lines = self.content.get()
		self.content.set(self.lines)
		self.destroy()

	def pathButton(self):
		self.button = Button(self, text = "Choose the file you want to comment", bg="black", fg="white",command = self.fileDialog)
		self.button.grid(column = 0, row = 1)

	def fileDialog(self):
		self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype = \
		(("jpeg files","*.*"),("all files","*.*")) )
		self.destroy()

root1 = Root("Path")
root1.title("HashApp")
root1.mainloop()

filename=root1.filename

with open(filename) as f:
        content = f.readlines()
content = [x for x in content]
f.close()

# lineList contains every line we want to comment
root2 = Root("Lines")
root2.title("HashApp")
root2.mainloop()

lines=root2.lines

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
