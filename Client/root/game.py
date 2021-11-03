#find;

			"MyShopPriceList"		: self.__PrivateShop_PriceList,
		}

#add below;

		if app.ENABLE_GUILD_HISTORY:
			serverCommandList["lonca_gecmis_temizle"] = self.gecmistemizle
			serverCommandList["lonca_gecmis_ekle"] = self.lonca_gecmis_ekle
			serverCommandList["getinputbegin"] = self.__Inputget1
			serverCommandList["getinputend"] = self.__Inputget2
			serverCommandList["getinput"] = self.__Inputget3

#add to bottom;

	if app.ENABLE_GUILD_HISTORY:
		def gecmistemizle(self):
			import constInfo
			constInfo.lonca_gecmis_list = []

		def lonca_gecmis_ekle(self, lonca, tarih):
			import constInfo
			constInfo.lonca_gecmis_list.append("#"+lonca+"#"+tarih)

		def __Inputget1(self):
			constInfo.INPUT = 1
			constInfo.INPUT_IGNORE = 1

		def __Inputget2(self):
			constInfo.INPUT = 0
			constInfo.INPUT_IGNORE = 0

		def __Inputget3(self): 
			net.SendQuestInputStringPacket("1")