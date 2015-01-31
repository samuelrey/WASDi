import wx
import os

paths = {
				'A':""
			}
			
class MyFrame(wx.Frame):			
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(400,200))
		
		# self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)								# Makes the text editing space in center of space
		self.CreateStatusBar()																	# Creates status bar at bottom of frame
		
		filemenu = wx.Menu()																	# Creates file menu
		menuOpen = filemenu.Append(wx.ID_OPEN, "Open", "Open a file to edit")					# Adds open button to file menu with appropriate status
		self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)											# Binds open button to OnOpen event
		
		menuSave = filemenu.Append(wx.ID_SAVE, "Save", "Save file")								# Adds save button to file menu with appropriate status
		self.Bind(wx.EVT_MENU, self.OnSave, menuSave)											# Binds save button to OnSave event
		
		menuAbout = filemenu.Append(wx.ID_ABOUT, "About", "Information about this program")		# Adds about button to file menu with appropriate status
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)											# Binds about button to OnAbout event
		
		filemenu.AppendSeparator()																# Adds separator before next button
		menuExit = filemenu.Append(wx.ID_EXIT, "Exit", "Terminate the program")					# Adds exit button to file menu with appropriate status
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)											# Binds exit button to OnExit event
		
		menuBar = wx.MenuBar()																	# Creates menu bar
		menuBar.Append(filemenu, "&File")														# Adds file menu to menu bar
		self.SetMenuBar(menuBar)																# Sets the frame's menu bar
		
		self.Show(True)
		
	def OnAbout(self, e):
		dialog = wx.MessageDialog(self, "A light text editor", "About luxicon")
		dialog.ShowModal()
		dialog.Destroy()
		
	def OnExit(self, e):
		self.Close(True)
		
	def OnOpen(self, e):
		self.directory = ""
		dialog = wx.FileDialog(self, "Choose a file", self.directory, "", "*.*", wx.OPEN)
		if (dialog.ShowModal() == wx.ID_OK):
			self.filename = dialog.GetFilename()
			self.directory = dialog.GetDirectory()
			paths['A'] = os.path.join(self.directory, self.filename)
		print "A has the path " + paths['A']
		dialog.Destroy()
		
	def OnSave(self, e):
		self.directory = ""
		dialog = wx.FileDialog(self, "Choose a file", self.directory, "", "*.*", wx.SAVE | wx.OVERWRITE_PROMPT)
		if (dialog.ShowModal() == wx.ID_OK):
			contents = self.control.GetValue()
			self.filename = dialog.GetFilename()
			self.directory = dialog.GetDirectory()
			f = open(os.path.join(self.directory, self.filename), "w")
			f.write(contents)
			f.close()
		dialog.Destroy()
	
app = wx.App(False)
frame = MyFrame(None, "luxicon")
app.MainLoop()
