//find;

	RequestAddMember(pchInvitee, 15);

//add below;

#ifdef ENABLE_GUILD_HISTORY
	DBManager::instance().Query("INSERT INTO lonca_gecmis%s (isim, lonca, tarih) values('%s', '%s', CURDATE())", get_table_postfix(), pchInvitee->GetName(), GetName());
#endif