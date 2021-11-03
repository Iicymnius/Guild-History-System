//find;

struct command_info cmd_info[] =

//add above;

#ifdef ENABLE_GUILD_HISTORY
ACMD(do_lonca_gecmis);
#endif

//find again;

		{ "\n",						NULL,					0,			POS_DEAD,	GM_IMPLEMENTOR	}

//add above;

#ifdef ENABLE_GUILD_HISTORY
		{ "lonca_gecmi",			do_inputall,			0,			POS_DEAD,	GM_PLAYER	},
		{ "lonca_gecmis",			do_lonca_gecmis,		0,			POS_DEAD,	GM_PLAYER	},
#endif