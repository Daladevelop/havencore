#!/usr/bin python
#coding=UTF-8
#========================================================================
# File: missile.py
#
# Author: Max Sidenstjärna
# Date: 2011-10-22
# Licens: GPL
#
# Comment:
#
#========================================================================

__copyright__ = "Copyright 2011, Daladevelop"
__license__   = "GPL"

from math import floor, radians, sin, cos
import pygame
import explosion
import entity
from rotsprite import RotSprite

class Missile(entity.Entity):

    """
    Generic class for all projectiles in the game.

    """

    def __init__(self, dict, filename, size):
        self.__dict__ = dict
        self.sprite = RotSprite(filename, size)
        self.sprite.set_direction(self.rot)

#    def __init__(self, (x, y), vel, rot, filename, size, parent):
#        entity.Entity.__init__(self, (x, y), size[0] / 2)
#        self.vel = vel
#        self.rot = rot
#        self.parent = parent
#        
#        self.sprite = rotsprite.RotSprite(filename, size)
#        self.sprite.set_direction(self.rot)

    def handle_input(self, event):
        pass

    def update(self):
#        for entity in self.collision_list:
#            if entity is not self.parent:
#                gameengine.add_entity(explosion.Explosion((self.x, self.y),
#                    "client/img/explosion2.png", (64, 64), 2))
#                self.alive = False

        self.x += self.vel * sin(radians(self.rot))
        self.y += self.vel * cos(radians(self.rot))

    def draw(self, screen):
        self.sprite.draw(screen, self.x, self.y)

    def __repr__(self):
        """Return a string representation of the instance."""
        return ('<%s(alive=%s, x=%0.2f, y=%0.2f, rot=%0.2f, vel=%0.2f)>' %
                (self.__class__.__name__, self.alive, self.x, self.y,
                    self.rot, self.vel))

# vim: ts=4 et tw=79 cc=+1
