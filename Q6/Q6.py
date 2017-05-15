import numpy as np
import math
class Ship:
	def __init__(self,lasers, shields, hull, name):
		self.lasers=lasers
		self.shields=shields
		self.hull=hull
		self.name=name
	def get_shot(self, strnth):
		if (self.shields>=strnth):
			self.shields=self.shields-strnth
		elif 0<self.shields<strnth:
			self.hull=(self.hull-(strnth-self.shields)/2)
			self.shields=0
		else: 
			self.hull=self.hull-(strnth/2)
	def Shoot(self, target):
		shot = target.get_shot(self.lasers)
		if shot is not(None):
			return 'lasers, the shot was dodged!'
		else: 
			return 'lasers'
	def check_dead(self):
		if (self.hull<=0):
			return True
		else:
			return False
	def get_hull(self):
		return self.hull
	def get_status(self):
		return "shields at power level" + self.shields, "hull at strength level" + self.hull

class Speeder(Ship):
	def __init__(self,lasers, shields, hull, name):
		Ship.__init__(self, lasers, shields, hull, name)
	def get_shot(self, strnth):
		if (np.random.rand()>0.5):
			if (self.shields>=strnth):
				self.shields=self.shields-strnth
			elif 0<self.shields<strnth:
				self.hull=(self.hull-(strnth-self.shields)/2)
				self.shields=0
			else: 
				self.hull=self.hull-(strnth/2)
		else:
			return 'dodged!'
				
				

class Warship(Ship):
	def __init__(self,lasers, shields, hull, name, missiles):
		Ship.__init__(self, lasers, shields, hull, name)
		self.missiles=missiles
	def Shoot(self, target):
		if (np.random.rand())>0.7:
			shot=target.get_shot(self.missiles)
			if shot is not(None):
				return 'missiles, the shot was dodged!'
			else: 
				return 'missiles'
		else:
			shot=target.get_shot(self.lasers)
			if shot is not(None):
				return 'lasers, the shot was dodged!'
			else: 
				return 'lasers'

def check_dead(target):
	if (target.hull<=0):
		return True
	else:
		return False


D_Star=Warship(30, 130, 26, 'The Death Star', 160)
NCC_1701=Ship(20,  60, 50, 'The USS Enterprise')
Rick=Speeder(30, 100, 40, 'Rick Sanchez')
NCC_74656=Ship(20,  60, 50, 'The USS Voyager')
Nimbus=Ship(20,  60, 50, 'Zap Brannigan')

players=np.asarray([D_Star, NCC_1701, NCC_74656, Rick, Nimbus])

def play(players):
	print 'BATTLE LOG:'
	while len(players)>1:
		target=players[math.ceil((len(players)-1)*np.random.rand())]
		shot = players[0].Shoot(target)
		print players[0].name + " shot " + target.name + ' with ' + str(shot)
		if not(target.check_dead()):
			players=np.append(np.asarray(players[1:(len(players))]),(np.asarray(players[0])))
		else:
			players = np.append(np.asarray(players[1:(len(players))]),(np.asarray(players[0])))
			players = np.delete(players, np.where(players==target)[0][0])
			print target.name + ' blew up'
	print "The winner is " + players[0].name
		
		



	
	
