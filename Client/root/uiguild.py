#add;

if app.ENABLE_GUILD_HISTORY:
	import uiloncagecmis

#find;

			page.Children.append(generalEnableCheckBox)

#add below;

			if app.ENABLE_GUILD_HISTORY:
				if str(player.GetMainCharacterName()) == str(guild.GetGuildMasterName()):
					loncagecmisi = ui.MakeButton(page, 340, yPos, "", "d:/ymir work/ui/game/windows/", "messenger_guild_01.sub", "messenger_guild_02.sub", "messenger_guild_03.sub")
					loncagecmisi.SetEvent(ui.__mem_func__(self.loncagemisinebak), inverseLineIndex)
					loncagecmisi.SetToolTipText("Lonca Geçmiþi")
					page.Children.append(loncagecmisi)

#find again;

			memberSlotList.append(generalEnableCheckBox)

#add below;

			if app.ENABLE_GUILD_HISTORY:
				if str(player.GetMainCharacterName()) == str(guild.GetGuildMasterName()):
					memberSlotList.append(loncagecmisi)

#find again;

	def __MakeBaseInfoPage(self):

#add above;

	if app.ENABLE_GUILD_HISTORY:
		def loncagemisinebak(self, index):
			page = self.pageWindow["MEMBER"]
			memberlist = page.memberDict[index]
			if str(memberlist[0].GetText()) == "" or str(memberlist[0].GetText()) == " ":
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Geçersiz seçim.")
			else:
				constInfo.lonca_gecmis_isim = str(memberlist[0].GetText())
				constInfo.lonca_gecmis_list = []
				net.SendChatPacket("/lonca_gecmis " + str(constInfo.lonca_gecmis_isim))
				self.gecmis=uiloncagecmis.LoncaGecmisSelectDialog()
				self.gecmis.Open()