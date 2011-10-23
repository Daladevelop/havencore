#!/usr/bin/python2
#coding=UTF-8
#--------------------------------------
#Name: vehicle.py
#Class for the vehicles, handles 
#input, update, draw...
#
#Gustav Fahlén, 2011-10-22
#-------------------------------------
import pygame
from pygame.locals import *
import entity
import math

class Vehicle(entity.Entity):
	#def __init__(self):
	#	self.x_pos=0.0
	#	self.ypos=0.0
	#	self.rotation=0
	#	self.rotation_torque=0

	def __init__(self, x_pos, y_pos, rotation):
		self.x_pos=x_pos
		self.y_pos=y_pos
		self.rotation=rotation
		self.rotation_torque=0
		self.velocity=0
	
	def handle_input(self, event):
		if event.type == KEYDOWN:
			if event.key == K_UP:
				self.velocity -= 5
			if event.key == K_DOWN:
				self.velocity += 5
			if event.key == K_RIGHT:
				self.rotation_torque -= 0.1
			if event.key == K_LEFT:
				self.rotation_torque += 0.1
		elif event.type == KEYUP:
			if event.key == K_UP:
				self.velocity += 5
			if event.key == K_DOWN:
				self.velocity -= 5
			if event.key == K_RIGHT:
				self.rotation_torque += 0.1
			if event.key == K_LEFT:
				self.rotation_torque -= 0.1
	
	def update(self, lst_ent):
		self.rotation += self.rotation_torque
		while self.rotation <= 360:
			self.rotation += 360
		while self.rotation >= 360:
			self.rotation -= 360

		self.x_pos+=(self.velocity * math.sin(self.rotation))
		self.y_pos+=(self.velocity * math.cos(self.rotation))
	
	def draw(self, screen):
		pygame.draw.circle(screen, pygame.Color(125,10,88), (int(self.x_pos), int(self.y_pos)), 20)

	def __repr__(self):
		return "rot: %.2f, pos: (%.2f, %.2f)" % (self.rotation, self.x_pos, self.y_pos)

# debug main
if __name__ == "__main__":
	print "test_main"
	V = Vehicle(4.0,11.0,90)
	print V

