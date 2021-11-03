//find;

ACMD(do_user_horse_feed)

//add above;

#ifdef ENABLE_GUILD_HISTORY
ACMD(do_lonca_gecmis)
{
	if (quest::CQuestManager::instance().GetEventFlag("lonca_gecmis_disable") == 1)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Sistem þu an için devre dýþý.");
		return;
	}

	int iPulse = thecore_pulse();

	if (iPulse - ch->GetLastLoncaGecmisLastTime() < passes_per_sec * 2)
	{
		return;
	}

	ch->SetLastLoncaGecmisLastTime(iPulse);

	if (!ch || !ch->GetGuild() || ch->GetGuild()->GetMasterPID() != ch->GetPlayerID())
		return;

	char arg1[256];
	one_argument(argument, arg1, sizeof(arg1));

	if (!*arg1)
		return;

	char szEscapedName[1024];
	DBManager::instance().EscapeString(szEscapedName, sizeof(szEscapedName), arg1, strlen(arg1));

	char szQuery[1024];
	snprintf(szQuery, sizeof(szQuery), "SELECT lonca, tarih FROM player.lonca_gecmis WHERE isim = '%s' ORDER BY tarih DESC", szEscapedName);
	std::unique_ptr<SQLMsg> msg_(DBManager::instance().DirectQuery(szQuery));

	if (msg_->Get()->uiNumRows == 0)
		return;

	ch->ChatPacket(CHAT_TYPE_COMMAND, "lonca_gecmis_temizle");
	while (MYSQL_ROW row1 = mysql_fetch_row(msg_->Get()->pSQLResult))
		ch->ChatPacket(CHAT_TYPE_COMMAND, "lonca_gecmis_ekle %s %s", row1[0], row1[1]);
}
#endif