from Tkinter import *
from ttk import *
import View

class TFSPanel(Frame):
	def __init__(this,parent,position):
		Frame.__init__(this,parent)
		if position=='right':
			this.pack(fill=BOTH, expand=1)
		else:
			this.pack(fill=BOTH, expand=1)

		label = Label(this,text='text')
		label.pack()

		treeview = Treeview(this)
		treeview.pack(fill=BOTH, expand=1)