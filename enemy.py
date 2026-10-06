from entity import *
from utils import *
import time
import random

class Enemy(Entity):
    def __init__(self, screen):
        super().__init__(screen)
        self.armor = None
        self.speed = 8
        self.cooldown_position = time.time()
        
    def update_position(self, no_cooldown=False):
        if time.time() < self.cooldown_position and not no_cooldown:
            return

        self.cooldown_position = time.time() + random.randint(2, 10)
        self.set_pos((random.randint(0, self.screen.get_width() - self.get_material().get_width()),
                    random.randint(0, self.screen.get_height() - self.get_material().get_height()))
                   )
        
    def think(self):
        super().think()
        self.update_position()
    
    def on_collision_bounds(self, target):
        super().on_collision_bounds(target)
        
        if target.is_player():
            self.update_position(True)
            add_score()
    
    def set_armor(self, armor):
        if not armor or type(armor) != int or armor < 0:
            return
        
        self.armor = armor
    
    def get_armor(self):
        return self.armor
    
    def set_speed(self, speed):
        if not speed or type(speed) != int or speed < 0:
            return
        
        self.speed = speed
        
    def get_speed(self):
        return self.speed
    
    def is_npc(self):
        return True