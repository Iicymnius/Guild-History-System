//find;

#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM", 0);
#endif

//add below;

#ifdef ENABLE_GUILD_HISTORY
	PyModule_AddIntConstant(poModule, "ENABLE_GUILD_HISTORY", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_GUILD_HISTORY", 0);
#endif