import wx

class Interface(wx.Frame):
    def __init__(self, parent, title):
        super(Interface, self).__init__(parent, title=title)

        # Show the window on screen
        self.setup()
        self.Show()

    def setup(self):
        box = wx.BoxSizer(wx.VERTICAL)
        self.textbox = wx.TextCtrl(self, style=wx.TE_RIGHT)
        box.Add(self.textbox, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4) #need to make this a text label not a text box
        grid = wx.GridSizer(5, 5, 10, 10) #probably want to scale buttons better

        grid.AddMany([
            (wx.Button(self, label='browse'), 0, wx.EXPAND), #need to add event handler to code below to choose file (commented out)
            (wx.Button(self, label='run'), 0, wx.EXPAND), #needs event handler to run optimizer.py script
        ])

        box.Add(grid, proportion=1, flag=wx.EXPAND)
        self.SetSizer(box)


if __name__ == '__main__':
    # Create the application object
    app = wx.App()
    Interface(None, title='Third Shift')

    app.MainLoop()

# def onButton(event):
#     print("Button pressed.")
 
# app = wx.App()
 
# frame = wx.Frame(None, -1, 'win.py')
# frame.SetSize(0,0,200,50)
 
# # Create open file dialog
# openFileDialog = wx.FileDialog(frame, "Open", "", "", 
#                                       "Python files (*.py)|*.py", 
#                                        wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
 
# openFileDialog.ShowModal()
# print(openFileDialog.GetPath())
# openFileDialog.Destroy()