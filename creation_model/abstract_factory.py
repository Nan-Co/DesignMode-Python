# -*- coding: utf-8 -*-
"""抽象工厂模式

抽象工厂模式是围绕一个超级工厂创建其他工厂，每个具体工厂都能按照
工厂模式提供相应的对象

假如你有一款游戏需要同时跑在IOS和Android，在两个平台上创建的角色和怪物不同。
这里简化一下不生成对象，仅生产字符串。
那么有：	GameFactory

IOSGameFactory		AndroidGameFactory
"""

class GameFactory(object):

	def CreatePlayer(self):
		return ""

	def CreateMonster(self):
		return ""

class IOSGameFactory(GameFactory):

	def CreatePlayer(self):
		return "ios player"
	
	def CreateMonster(self):
		return "ios monster"

class AndroidGameFactory(GameFactory):

	def CreatePlayer(self):
		return "android player"

	def CreateMonster(self):
		return "android monster"


def Main(sMode):
	if sMode == "IOS":
		oGame = IOSGameFactory()
	elif sMode == "Android":
		oGame = AndroidGameFactory()
	else:
		oGame = GameFactory()

	print "create game player:%s,monster:%s" % (oGame.CreatePlayer(), oGame.CreatePlayer())
	
Main("IOS")			#>>> create game player:ios player,monster:ios player
Main("Android")		#>>> create game player:android player,monster:android player
Main("HongMeng")	#>>create game player:,monster: