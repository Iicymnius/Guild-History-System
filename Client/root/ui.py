#find;

class CandidateListBox(ListBoxEx):

#add above;

if app.ENABLE_GUILD_HISTORY:
	class ListBox_Scroll_LoncaGecmisiListesi(Window):
		TEMPORARY_PLACE = 3
		def __init__(self, layer = "UI"):
			Window.__init__(self, layer)
			self.overLine = -1
			self.selectedLine = -1
			self.width = 0
			self.height = 0
			self.stepSize = 100
			self.basePos = 0
			self.showLineCount = 0
			self.itemCenterAlign = True
			self.itemList = []
			self.GuildName = []
			self.Date = []
			self.Resim = []

			self.keyDict = {}
			self.textDict = {}
			self.event = lambda *arg: None

		def __del__(self):
			Window.__del__(self)

		def SetWidth(self, width):
			self.SetSize(width, self.height)

		def SetSize(self, width, height):
			Window.SetSize(self, width, height)
			self.width = width
			self.height = height

		def SetTextCenterAlign(self, flag):
			self.itemCenterAlign = flag

		def SetBasePos(self, pos):
			self.basePos = pos
			self._LocateItem()

		def ClearItem(self):
			self.keyDict = {}
			self.textDict = {}
			self.itemList = []
			self.GuildName = []
			self.Date = []
			self.Resim = []
			self.overLine = -1
			self.selectedLine = -1

		def InsertItem(self, number, GuildName, Date):

			self.keyDict[len(self.itemList)] = number
			self.textDict[len(self.itemList)] = number

			x_ek = 80

			ResimCek = ImageBox()
			ResimCek.AddFlag("not_pick")
			ResimCek.SetParent(self)
			ResimCek.SetPosition(9, 5)
			ResimCek.LoadImage("d:/ymir work/guild/lonca_bg.png")
			ResimCek.Show()

			GuildNameText = TextLine()
			GuildNameText.SetParent(self)
			GuildNameText.SetPosition(20,6)
			GuildNameText.SetText(str(GuildName))
			GuildNameText.Show()

			DateText = TextLine()
			DateText.SetParent(self)
			DateText.SetPosition(100, 6)
			DateText.SetText(str(Date))
			DateText.Show()

			self.itemList.append(GuildNameText)
			self.Resim.append(ResimCek)
			self.GuildName.append(GuildNameText)
			self.Date.append(DateText)

			self._LocateItem()

		def ChangeItem(self, number, text, tooltipText, textlineText, width):
			for key, value in self.keyDict.items():
				if value == number:
					self.textDict[key] = text + tooltipText + textlineText + width

					if number < len(self.itemList):
						self.itemList[key].SetText(text)

					return

		def _LocateItem(self):
			skipCount = self.basePos
			yPos = 0
			self.showLineCount = 0

			for i in xrange(0, len(self.itemList)):
				GuildNameText = self.GuildName[i]
				DateText = self.Date[i]
				ResimCek = self.Resim[i]

				ResimCek.SetPosition(11,yPos)
				GuildNameText.SetPosition(28,yPos + 2)
				DateText.SetPosition(102,yPos + 2)

				if skipCount > 0:
					skipCount -= 1
					continue

				yPos += 23

				if yPos <= self.GetHeight():
					self.showLineCount += 1
					GuildNameText.Show()
					DateText.Show()
					ResimCek.Show()
				else:
					GuildNameText.Hide()
					DateText.Hide()
					ResimCek.Hide()

		def ArrangeItem(self):
			self.SetSize(self.width)
			self.SetSize(self.width, len(self.itemList) * 9)
			self._LocateItem()

		def GetViewItemCount(self):
			return self.showLineCount

		def GetItemCount(self):
			return len(self.itemList)

		def SetEvent(self, event):
			self.event = event

		def SelectItem(self, line):

			if not self.keyDict.has_key(line):
				return

			if line == self.selectedLine:
				return

		def GetSelectedItem(self):
			return self.keyDict.get(self.selectedLine, 0)

		def OnMouseLeftButtonDown(self):
			if self.overLine < 0:
				return

		def OnMouseLeftButtonUp(self):
			if self.overLine >= 0:
				pass

		def OnUpdate(self):
			if self.IsIn():
				pass

		def OnRender(self):
			xRender, yRender = self.GetGlobalPosition()
			yRender -= self.TEMPORARY_PLACE
			widthRender = self.width
			heightRender = self.height + self.TEMPORARY_PLACE*2

			if localeInfo.IsCIBN10:
				if -1 != self.overLine and self.keyDict[self.overLine] != -1:
					grp.SetColor(HALF_WHITE_COLOR)
					grp.RenderBar(xRender + 2, yRender + self.overLine*self.stepSize + 4, self.width - 3, self.stepSize)

				if -1 != self.selectedLine and self.keyDict[self.selectedLine] != -1:
					if self.selectedLine >= self.basePos:
						if self.selectedLine - self.basePos < self.showLineCount:
							grp.SetColor(SELECT_COLOR)
							grp.RenderBar(xRender + 2 - 50, yRender + (self.selectedLine-self.basePos)*self.stepSize + 4, self.width - 3, self.stepSize - 50)

			else:
				if -1 != self.overLine:
					pass

				if -1 != self.selectedLine:
					pass

	class ListBox_Scroll_LoncaGecmisiListesiEKLE(ListBox_Scroll_LoncaGecmisiListesi):
		def __init__(self):
			ListBox_Scroll_LoncaGecmisiListesi.__init__(self)
			
			self.viewItemCount=9
			self.basePos=0
			self.itemHeight=15
			self.itemStep=20
			self.showLineCount = 0
			self.scrollBar = ScrollBar()
			self.scrollBar.SetParent(self)
			self.scrollBar.SetScrollEvent(self.__OnScroll)
			self.scrollBar.Hide()

		def SetSize(self, width, height):
			ListBox_Scroll_LoncaGecmisiListesi.SetSize(self, width - ScrollBar.SCROLLBAR_WIDTH, height)
			Window.SetSize(self, width, height)

			self.scrollBar.SetPosition(width - ScrollBar.SCROLLBAR_WIDTH - 8 - 3 - 9, 0)
			self.scrollBar.SetScrollBarSize(height)

		def ClearItem(self):
			ListBox_Scroll_LoncaGecmisiListesi.ClearItem(self)
			self.scrollBar.SetPos(0)

		def _LocateItem(self):
			ListBox_Scroll_LoncaGecmisiListesi._LocateItem(self)

			if self.showLineCount < len(self.itemList):
				self.scrollBar.SetMiddleBarSize(float(self.GetViewItemCount())/self.GetItemCount())
				self.scrollBar.Show()
			else:
				self.scrollBar.Hide()

		def SetScrollBar(self, scrollBar):
			scrollBar.SetScrollEvent(__mem_func__(self.__OnScroll))
			self.scrollBar=scrollBar

		def __OnScroll(self):
			scrollLen = self.GetItemCount()-self.GetViewItemCount()
			if scrollLen < 0:
				scrollLen = 0
			self.SetBasePos(int(self.scrollBar.GetPos()*scrollLen))

		def __GetScrollLen(self):
			scrollLen=self.__GetItemCount()-self.__GetViewItemCount()
			if scrollLen<0:
				return 0

			return scrollLen

		def __GetViewItemCount(self):
			return self.viewItemCount

		def __GetItemCount(self):
			return len(self.itemList)

		def GetItemViewCoord(self, pos, itemWidth):
			if localeInfo.IsARABIC():
				return (self.GetWidth()-itemWidth-10, (pos-self.basePos)*self.itemStep)
			else:
				return (0, (pos-self.basePos)*self.itemStep)

		def __IsInViewRange(self, pos):
			if pos<self.basePos:
				return 0
			if pos>=self.basePos+self.viewItemCount:
				return 0
			return 1

#find again;

				self.LoadElementListBoxEx(parent.Children[Index], ElementValue, parent)

#add below;

			elif app.ENABLE_GUILD_HISTORY and Type == "listbox_scroll_loncagecmisilistesi":
				parent.Children[Index] = ListBox_Scroll_LoncaGecmisiListesiEKLE()
				parent.Children[Index].SetParent(parent)
				self.LoadElementListBox(parent.Children[Index], ElementValue, parent)