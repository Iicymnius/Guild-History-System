//find;

		LogManager::instance().CharLog(ch, 0, "MAKE_GUILD", Log);

//add below;

#ifdef ENABLE_GUILD_HISTORY
		DBManager::instance().Query("INSERT INTO lonca_gecmis%s (isim, lonca, tarih) values('%s', '%s', CURDATE())", get_table_postfix(), ch->GetName(), cp.name);
#endif