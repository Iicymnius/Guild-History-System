import app
import ui
import localeInfo
import uiScriptLocale
import constInfo
import event
import chat
import time
import net
import interfaceModule
import uiguild
import event
import player

gecmislist = None

class PopupDialog(ui.ScriptWindow):
	def __init__(self, parent):
		print "NEW POPUP WINDOW   ----------------------------------------------------------------------------"	
		ui.ScriptWindow.__init__(self)

		self.__Load()
		self.__Bind()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print "---------------------------------------------------------------------------- DELETE POPUP WINDOW"

	def __Load(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/PopupDialog.py")
		except:
			import exception
			exception.Abort("PopupDialog.__Load")

	def __Bind(self):
		try:
			self.textLine=self.GetChild("message")
			self.okButton=self.GetChild("accept")
		except:
			import exception
			exception.Abort("PopupDialog.__Bind")

		self.okButton.SetEvent(ui.__mem_func__(self.__OnOK))

	def Open(self, msg):
		self.textLine.SetText(msg)
		self.SetCenterPosition()
		self.Show()
		self.SetTop()

	def __OnOK(self):
		self.Hide()

class LoncaGecmisSelectDialog(ui.ScriptWindow):
	def __init__(self):
		print "NEW MARK LIST WINDOW   ----------------------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)

		self.selectEvent=None
		self.isLoaded=0
		self.yenile=0
		self.ilk = 0
		self.yuzdekac = 0
		self.interface=None
		net.SendChatPacket("/lonca_gecmis " + str(constInfo.lonca_gecmis_isim))

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print "---------------------------------------------------------------------------- DELETE MARK LIST WINDOW"

	def Show(self):
		if self.isLoaded==0:
			self.isLoaded=1

			self.__Load()
			
		self.__ClearFileList()

		ui.ScriptWindow.Show(self)

	def Open(self):
		self.ilk = 0
		self.Show()
		self.SetCenterPosition()
		self.SetTop()

	def Close(self):
		self.popupDialog.Hide()
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def SAFE_SetSelectEvent(self, event):
		self.selectEvent=ui.__mem_func__(event)

	def __Creategecmislist(self):
		gecmislist=ui.ListBoxEx()
		gecmislist.SetParent(self)
		gecmislist.SetPosition(15, 50)
		gecmislist.Show()
		return gecmislist

	def __Load(self):
		self.popupDialog=PopupDialog(self)

		try:
			pyScrLoader = ui.PythonScriptLoader()
			if localeInfo.IsVIETNAM():
				pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "gecmiswindow.py")
			else:
				pyScrLoader.LoadScriptFile(self, "UIScript/gecmiswindow.py")
		except:
			import exception
			exception.Abort("gecmislist.__Load")

		try:
			self.gecmislist=self.__Creategecmislist()
			self.__ClearFileList()
			self.gecmislist.SetScrollBar(self.GetChild("ScrollBar"))

			self.board=self.GetChild("board")
			self.cancelButton=self.GetChild("cancel")
			self.refreshButton=self.GetChild("refresh")
			self.yuzde=self.GetChild("yuzdelik")
			self.yuzde.Hide()

		except:
			import exception
			exception.Abort("gecmislist.__Bind")

		self.cancelButton.SetEvent(ui.__mem_func__(self.__OnCancel))
		self.board.SetCloseEvent(ui.__mem_func__(self.__OnCancel))
		self.board.SetTitleName(constInfo.lonca_gecmis_isim + " Lonca Geçmiþi")
		self.refreshButton.SetEvent(ui.__mem_func__(self.__loncadancikar))

		self.UpdateRect()
		self.__ClearFileList()
		net.SendChatPacket("/lonca_gecmis " + str(constInfo.lonca_gecmis_isim))

		if len(constInfo.lonca_gecmis_list) != 0:
			for i in xrange(0, len(constInfo.lonca_gecmis_list)):
				self.gecmislist.AppendItem(markla(constInfo.lonca_gecmis_list[i].split("#")[1] + " Tarih: " + constInfo.lonca_gecmis_list[i].split("#")[2]))

	def __loncadancikar(self):
		secilen = constInfo.lonca_gecmis_isim
		my_name = player.GetName()
		if secilen == my_name:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Kendini loncadan atamazsýn.")
			return
		net.SendGuildRemoveMemberPacket(secilen)
		chat.AppendChat(chat.CHAT_TYPE_INFO, secilen+" loncadan çýkarýldý.")

	def __PopupMessage(self, msg):
		self.popupDialog.Open(msg)

	def __kapahepsini(self):
		self.GetChild("ScrollBar").Hide()
		self.GetChild("yuzdelik").Show()

	def __OnCancel(self):
		self.Hide()

	def OnUpdate(self):
		if self.ilk == 1:
			if self.yenile > app.GetTime():
				return
			else:
				self.__ClearFileList()
				net.SendChatPacket("/lonca_gecmis " + str(constInfo.lonca_gecmis_isim))

				for i in xrange(0, len(constInfo.lonca_gecmis_list)):
					self.gecmislist.AppendItem(markla(constInfo.lonca_gecmis_list[i].split("#")[1] + " Tarih: " + constInfo.lonca_gecmis_list[i].split("#")[2]))

				if self.gecmislist.IsEmpty():
					self.__PopupMessage("Lonca bilgisi girilmemiþ.")

				self.yenile = app.GetTime()+30
		else:
			if self.yuzdekac < 102:
				self.__kapahepsini()
				self.GetChild("yuzdelik").SetFontName("Tahoma:25")
				self.GetChild("yuzdelik").SetText("%"+str(self.yuzdekac))
				self.yuzdekac += 1
			else:
				self.GetChild("yuzdelik").Hide()
				self.GetChild("ScrollBar").Show()
				self.ilk = 1
				self.yuzdekac = 0

	def __ClearFileList(self):
		self.gecmislist.RemoveAllItems()

	def __AppendFile(self, fileName):
		self.gecmislist.AppendItem(markla(fileName))

class markla(ui.ListBoxEx.Item):
	def __init__(self, fileName):
		ui.ListBoxEx.Item.__init__(self)
		self.imgWidth=0
		self.imgHeight=0
		self.canLoad=0
		self.textLine=self.__CreateTextLine(fileName)
		self.imgBox=self.__CreateImageBox()

	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)

	def GetText(self):
		return self.textLine.GetText()

	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self, 20 + 6*len(self.textLine.GetText()) + 4, height)

	def __CreateTextLine(self, fileName):
		textLine=ui.TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(20, 0)
		textLine.SetText(fileName)
		textLine.Show()
		return textLine

	def __CreateImageBox(self):
		imgBox=ui.ImageBox()
		imgBox.AddFlag("not_pick")
		imgBox.SetParent(self)
		imgBox.SetPosition(0, 2)
		imgBox.LoadImage("d:/ymir work/guildlogo.tga")
		imgBox.Show()
		return imgBox
