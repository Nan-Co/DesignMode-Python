# -*- coding: utf-8 -*-
"""命令模式

需求场景：
如在软件安装时记录用户勾选的所有偏好，存储在一个Commnad对象中，
在完成安装后，Command对象运行execute方法。

核心思想：将请求封装为对象

三个角色：
Command：命令对象，创建不同的命令
Receiver：参数接受者，具体逻辑的执行者
Invoker：调用命令的对象，由他来存放命令对象并执行。

"""

class Command(object):
		
	def execute(self):
		pass

def AddExpCommand(Command):

	def __init__(self, people):
		self._people = people
		
	def execute(self):
		self._people.AddExp(10)

def AddGoldCommand(Command):
	
	def __init__(self, people):
		self._people = people
	
	def execute(self):
		self._people.AddGold(10)

class People(object):
	
	def __init__(self):
		self._gold = 0
		self._exp = 0

	def AddGold(self, v):
		self._gold = v

	def AddExp(self, v):
		self._exp = v

class Invoker(object):

	def __init__(self):
		self._cmd = []
	
	def AddCmd(self, cmd):
		self._cmd.append(cmd)
	
	def ExecAll(self):
		for cmd in self._cmd:
			cmd.execute()

invoker = Invoker()
people = People()

invoker.AddCmd(AddExpCommand(people))
invoker.AddCmd(AddGoldCommand(people))

invoker.ExecAll()