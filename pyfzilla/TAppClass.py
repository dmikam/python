from Tkinter import *
import View

class TAppClass(Tk):
  def __init__(this):
    Tk.__init__(this)
    this.geometry("750x500+300+300")
    this.layout = View.TLayout(this)

  def start(this):
    """
      Starts the application execution
    """
    this.config(menu=this.layout.menu)
    this.mainloop()