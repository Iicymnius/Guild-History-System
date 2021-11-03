import uiScriptLocale

window = {
	"name" : "gecmiswindow",

	"x" : SCREEN_WIDTH - 250,
	"y" : SCREEN_HEIGHT - 400 - 50,

	"style" : ("movable", "float",),

	"width" : 250,
	"height" : 300,

	"children" :
	(

		{
			"name" : "board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 250,
			"height" : 300,
			"title" : "Lonca Geçmiþi",
		},
		{
			"name" : "yuzdelik",
			"type" : "text",

			"x" : 110,
			"y" : 130,

			"text" : "%",
		},
		{
			"name" : "ScrollBar",
			"type" : "scrollbar",

			"x" : 27,
			"y" : 40,
			"size" : 220,
			"horizontal_align" : "right",
		},
		{
			"name" : "cancel",
			"type" : "button",

			"x" : 190,
			"y" : 265,

			"width" : 41,
			"height" : 21,

			"text" : "Kapat",

			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},
		{
			"name" : "refresh",
			"type" : "button",

			"x" : 15,
			"y" : 265,

			"width" : 41,
			"height" : 21,

			"text" : "Çýkar",
			"tooltip_text" : "Oyuncuyu Loncadan At",
			"tooltip_x" : 0,
			"tooltip_y" : 35,

			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},
	)
}