//find;

	bool			WarpToPID(DWORD dwPID);

//add below;

#ifdef ENABLE_GUILD_HISTORY
	void			SetLastLoncaGecmisLastTime(int time) { m_dwLonGecLastTime = time; }
	int				GetLastLoncaGecmisLastTime() const { return m_dwLonGecLastTime; }
#endif

//find again;

	DWORD			m_dwStopTime;

//add below;

#ifdef ENABLE_GUILD_HISTORY
	int				m_dwLonGecLastTime;
#endif