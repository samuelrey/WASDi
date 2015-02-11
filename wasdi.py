import wx		# For the user interface
import wx.media	# For the media controllers
import os		# For setting new file paths

paths = {
					32:"/home/lux/Projects/WASDi/Music/606/clean/bd01.wav",			# Default file paths.
					119:"/home/lux/Projects/WASDi/Music/606/cassete 1/sn06.wav",	# Can be overwritten.
					97:"/home/lux/Projects/WASDi/Music/Game Boy/sfx07.wav",			# Uses w-a-s-d-<space>.
					115:"/home/lux/Projects/WASDi/Music/606/clean/ch12.wav",		# Keys are symbolic of ASCII values. a != A
					100:"/home/lux/Projects/WASDi/Music/Game Boy/arp01.wav"			# Can use more keys, includng modifiers.
		}
		
controllers = {
					32:0,							# Links <space> with media controller 0. 
					119:1,							# Each key has its own media controller.
					97:2,							# May be inefficient in terms of space.
					115:3,							# However, using a single media controller leads to the interruption of samples.
					100:4							# Can be mapped ergonomically. q-a-z share one media controller
			  }
		
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, title="WASDi", size=(200,200))	# Initialize the frame
		
		self.mctr0 = wx.media.MediaCtrl(self, id=0, style=wx.SIMPLE_BORDER)		# Create 5 media controllers with different id's.
		self.mctr1 = wx.media.MediaCtrl(self, id=1, style=wx.SIMPLE_BORDER)		# 
		self.mctr2 = wx.media.MediaCtrl(self, id=2, style=wx.SIMPLE_BORDER)		#
		self.mctr3 = wx.media.MediaCtrl(self, id=3, style=wx.SIMPLE_BORDER)		#
		self.mctr4 = wx.media.MediaCtrl(self, id=4, style=wx.SIMPLE_BORDER)		#
		
		self.panel = wx.Panel(self, wx.ID_ANY)		# Create panel.
		self.panel.Bind(wx.EVT_CHAR, self.OnKey)	# Bind character events on the panel to the OnKey method.
		self.panel.SetFocus()						# Set focus onto the panel.
		
		self.CreateStatusBar()						# Create status bar at the bottom of the frame.
		
		menubar = wx.MenuBar()						# Create menu bar at the top of the frame.
		filemenu = wx.Menu()						# Create file menu to occupy menu bar.
		editmenu = wx.Menu()						# Create edit menu to occupy menu bar.
		
		load_w = editmenu.Append(119, "Load W", "Set a new path for this key")			# Menu option to load new file path to w key.
		load_a = editmenu.Append(97, "Load A", "Set a new path for this key")			# All the paths can be changed.
		load_s = editmenu.Append(115, "Load S", "Set a new path for this key")			# This approach adds options to the edit menu.
		load_d = editmenu.Append(100, "Load D", "Set a new path for this key")			# It limits the key options to the presets.
		load__ = editmenu.Append(32, "Load Space", "Set a new path for this key")		# It also occupies more space. 
		about = filemenu.Append(wx.ID_ABOUT, "About", "Information about this program")	# Places about option in the file menu.
		exit = filemenu.Append(wx.ID_EXIT, "Exit", "Terminate program")					# Places exit option in the file menu.
		
		menubar.Append(filemenu, "File")			# Places file menu and edit menu in the menu bar.
		menubar.Append(editmenu, "Edit")			#
		
		self.Bind(wx.EVT_MENU, self.OnLoad, load_w)	# Binds the menu items to their respective methods.
		self.Bind(wx.EVT_MENU, self.OnLoad, load_a)	# The load_a option is bound to OnLoad.
		self.Bind(wx.EVT_MENU, self.OnLoad, load_s)	#
		self.Bind(wx.EVT_MENU, self.OnLoad, load_d)	#
		self.Bind(wx.EVT_MENU, self.OnLoad, load__)	#
		self.Bind(wx.EVT_MENU, self.OnAbout, about)	# The about option is bout to OnAbout.
		self.Bind(wx.EVT_MENU, self.OnExit, exit)	#
		
		self.SetMenuBar(menubar)					# Sets the menu bar to menubar.
		self.Centre()								# Centers the frame.
		self.Show(True)								# Makes the frame.
		
######################################################
# Called when a key is pressed. Checks that the key  #
# has a respective path. Attempts to load the path   #
# into a media controller and play the sample.	 	 #
######################################################
	def OnKey(self, event):
		keycode = event.GetKeyCode()
		if self.CheckKey(keycode):
			self.Load(keycode)
			self.Play(keycode)
	
######################################################
# Traverses dictionary of paths searching for the    #
# corresponding key. Returns True if there exists    #
# such a key, False otherwise.                       #
######################################################	
	def CheckKey(self, keycode):
		for key in paths.keys():
			if keycode == key:
				return True
		return False
		
######################################################
# Searches for the media controller with matching id #
# and loads the path. Displays error if unable to    #
# load path.                                         #
######################################################
	def Load(self, keycode):
		if not self.FindWindowById(controllers[keycode]).Load(paths[keycode]):
			wx.MessageBox("Unable to load %s" % paths[keycode], "ERROR", wx.ICON_ERROR|wx.OK)
			
######################################################
# Searches for the media controller with matching id #
# and plays the audio sample.                        #
######################################################
	def Play(self, keycode):
		self.FindWindowById(controllers[keycode]).Play()
		
######################################################
# Prompts user to select a new file to bind to the   #
# key of choice. Rewrites the previous filepath in   #
# the dictionary.                                    #
######################################################
	def OnLoad(self, event):
		dialog = wx.FileDialog(self, message="Choose a media file",
							   defaultDir=os.getcwd(), defaultFile="",
							   style=wx.OPEN|wx.CHANGE_DIR)
		if dialog.ShowModal() == wx.ID_OK:
			paths[event.GetId()] = dialog.GetPath()
		dialog.Destroy()
		
######################################################
# Displays information about the application.        #
######################################################
	def OnAbout(self, event):
		dialog = wx.MessageDialog(self, "Awesome sauce in a 200x200 window.", "WASDi", wx.OK)
		dialog.ShowModal()
		dialog.Destroy()
		
######################################################
# Closes the program.                                #
######################################################
	def OnExit(self, event):
		self.Close(True)
		
class MainApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame()
        self.SetTopWindow(self.frame)
        return True

if __name__ == "__main__":
    app = MainApp()
    app.MainLoop()
