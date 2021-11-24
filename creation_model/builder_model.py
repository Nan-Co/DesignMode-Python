# -*- coding: utf-8 -*-
"""建造者模式
这个模式用的频率比较高。

适用场景：
1、构造一个对象需要很多参数。
2、构造一个对象需要复杂的步骤。
3、构造一个对象需要按照某个顺序。

"""

class PersonBuilder(object):

	def __init__(self):
		self.Name = "未知"
		self.Age = 18
		self.Sex = "男"
		
	def SetName(self, v):
		self.Name = v
		return self

	def SetAge(self, v):
		self.Age = v
		return self
	
	def SetSex(self, v):
		self.Sex = v
		return self
	
	def Build(self):
		return Person(self)

class Person(object):
		
	def __init__(self, oBuilder):
		self.Name = oBuilder.Name
		self.Age = oBuilder.Age
		self.Sex = oBuilder.Sex

oPlayer = (PersonBuilder()
		.SetName("NanCo")
		.SetAge(19)
		.SetSex("男")
		.Build())

print oPlayer.Name