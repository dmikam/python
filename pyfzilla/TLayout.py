from Tkinter import *
import View

class TLayout(Frame):
  def __init__(this,parent):
    Frame.__init__(this,parent)

    # Main menu
    this.menu = Menu(parent)
    filemenu = Menu(this.menu, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    this.menu.add_cascade(label="File", menu=filemenu)

    # this.toolbar = View.TToolbar()

    this.vertical = PanedWindow(this, orient=VERTICAL, sashwidth=6,sashpad=0,sashrelief=RAISED)
    this.vertical.pack(fill=BOTH, expand=1)

    # Main part of the window where are the files panes situated
    this.files = PanedWindow(this.vertical,sashwidth=6,sashpad=0,sashrelief=RAISED)
    this.files.pack(fill=BOTH, expand=1)

    #Left file panel
    this.left = View.TFSPanel(this.files, position='left')
    this.left.grid(column=0,row=0)
    this.files.add(this.left)

    #right file panel
    this.right = View.TFSPanel(this.files, position='right')
    this.right.grid(column=1,row=0)

    this.files.add(this.right)

    this.vertical.add(this.files)

    # this.infoWindow = View.TInfoWindow()
    # this.vertical.add(this.info)

    # this.statusbar = View.TStatusbar()

    this.pack(fill=BOTH, expand=1)


def donothing():
  print "Do nothing"