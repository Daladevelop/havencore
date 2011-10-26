#!/usr/bin/python2 -tt
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
import missile
import rotsprite
import math
from math import floor, radians

class Vehicle(entity.Entity):
    def __init__(self, x_pos, y_pos, rotation):
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.rotation=rotation
        self.rotation_torque=0
        self.velocity=0
        self.cars = rotsprite.RotSprite("img/car6_fixed.png", (80,80))
        self.carIndex = 0

    def handle_input(self, event):
        if event.type == KEYDOWN:
            if event.key == K_UP:
                self.velocity += 5.0
            if event.key == K_DOWN:
                self.velocity -= 5.0
            if event.key == K_RIGHT:
                self.rotation_torque -= 5.0
            if event.key == K_LEFT:
                self.rotation_torque += 5.0
            if event.key == K_SPACE:
                print "MISSILE AWAY"
                #self.ActiveMissile.append(missile.Missile(self.x_pos, self.y_pos, 12, self.rotation))
        elif event.type == KEYUP:
            if event.key == K_UP:
                self.velocity -= 5.0
            if event.key == K_DOWN:
                self.velocity += 5.0
            if event.key == K_RIGHT:
                self.rotation_torque += 5.0
            if event.key == K_LEFT:
                self.rotation_torque -= 5.0

    def update(self):
        self.rotation += self.rotation_torque
        while self.rotation < 0.0:
            self.rotation += 360.0
        while self.rotation >= 360.0:
            self.rotation -= 360.0
        self.x_pos+=(self.velocity * math.sin(radians(self.rotation)))
        self.y_pos+=(self.velocity * math.cos(radians(self.rotation)))
        self.cars.set_direction(self.rotation)

    def collide_detect(self, lst_ent):
        pass

    def draw(self, screen):
        self.cars.draw(screen, self.x_pos, self.y_pos)

    def __repr__(self):
        return "rot: %.2f, pos: (%.2f, %.2f)" % (self.rotation, self.x_pos, self.y_pos)

#
#   Unit test procedure
#
if __name__ == "__main__":
    print "test_main"
    V = Vehicle(4.0,11.0,90)
    print V

# vim: set ts=4 sw=4 et
