import wx
import wx.media
import os

paths = {
					32:"/home/lux/Projects/WASDi/Music/606/clean/bd01.wav",
					119:"/home/lux/Projects/WASDi/Music/606/cassete 1/sn06.wav",
					97:"/home/lux/Projects/WASDi/Music/Game Boy/sfx07.wav",
					115:"/home/lux/Projects/WASDi/Music/606/clean/ch12.wav",
					100:"/home/lux/Projects/WASDi/Music/Game Boy/arp01.wav"
		}
		
controllers = {
					32:0,
					119:1,
					97:2,
					115:3,
					100:4
			  }
		
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, title="WASDi", size=(200,200))
		
		self.mctr0 = wx.media.MediaCtrl(self, id=0, style=wx.SIMPLE_BORDER)
		self.mctr1 = wx.media.MediaCtrl(self, id=1, style=wx.SIMPLE_BORDER)
		self.mctr2 = wx.media.MediaCtrl(self, id=2, style=wx.SIMPLE_BORDER)
		self.mctr3 = wx.media.MediaCtrl(self, id=3, style=wx.SIMPLE_BORDER)
		self.mctr4 = wx.media.MediaCtrl(self, id=4, style=wx.SIMPLE_BORDER)
		
		self.panel = wx.Panel(self, wx.ID_ANY)
		self.panel.Bind(wx.EVT_CHAR, self.OnKey)
		self.panel.SetFocus()
		
		self.CreateStatusBar()
		
		menubar = wx.MenuBar()
		filemenu = wx.Menu()
		
		about = filemenu.Append(wx.ID_ABOUT, "About", "Information about this program")
		exit = filemenu.Append(wx.ID_EXIT, "Exit", "Terminate program")
		
		menubar.Append(filemenu, "File")
		
		self.Bind(wx.EVT_MENU, self.OnAbout, about)
		self.Bind(wx.EVT_MENU, self.OnExit, exit)
		
		self.SetMenuBar(menubar)
		self.Centre()
		self.Show(True)
		
	def OnKey(self, event):
		keycode = event.GetKeyCode()
		if self.CheckKey(keycode):
			self.Load(keycode)
			self.Play(keycode)
				
	def CheckKey(self, keycode):
		for key in paths.keys():
			if keycode == key:
				return True
		return False
		
	def Load(self, keycode):
		if not self.FindWindowById(controllers[keycode]).Load(paths[keycode]):
			wx.MessageBox("Unable to load %s" % paths[keycode], "ERROR", wx.ICON_ERROR|wx.OK)
			
	def Play(self, keycode):
		self.FindWindowById(controllers[keycode]).Play()
			
	def OnAbout(self, event):
		dialog = wx.MessageDialog(self, "A light drum pad", "WASDi")
		dialog.ShowModal()
		dialog.Destroy()
		
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
