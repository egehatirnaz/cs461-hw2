"""
	CS461 Fall 2019 Homework 2 
	Authors: Faruk Ege Hatırnaz
			 Shabnam Sadigova
			 Sıla İnci
			 Dilara Halavurt
			 Doğukan Aydın

	Date: 	 07.11.2019
"""
class States:
	def __init__(self, x, y, b):
		self.situation = x + "M" + y + "C" + b
		self.x = x
		self.y = y
		self.b = b
	def __init__(self, situation):
		self.x = situation[0:1]
		self.y = situation[2:3]
		self.b = situation[5:]

	def update_situation(self,x,y,b):
		self.situation = x + "M" + y + "C" + b

	def is_safe():
		if(x>=0 && y>=0 && (6 - x)>=0 && (6 - y)>= 0 && (6-x)>=(6-y) && (x >= y)):
			return True
		else:
			return False
			
