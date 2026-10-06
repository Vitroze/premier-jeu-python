from entity import *
import pygame

class Player(Entity):
    def __init__(self, screen):
        super().__init__(screen)
        self.armor = None
        self.speed = 8
        
    def move(self):
        screen = self.screen
        if not screen:
            return

        keys = pygame.key.get_pressed()
        
        player_x, player_y = self.get_pos()[0], self.get_pos()[1]
        speed = self.set_speed(8 if keys[pygame.K_LSHIFT] else 4)
        
        moves = {
            pygame.K_LEFT: (-speed, 0),
            pygame.K_RIGHT: (speed, 0),
            pygame.K_UP: (0, -speed),
            pygame.K_DOWN: (0, speed),
        }

        for key, (dx, dy) in moves.items():
            if keys[key]:
                player_x += dx
                player_y += dy

        player_x = Clamp(player_x, 0, screen.get_width() - self.get_material().get_width())
        player_y = Clamp(player_y, 0, screen.get_height() - self.get_material().get_height())
        #player_rect.topleft = (player_x, player_y) # Update collision bounds
        
        self.set_pos((player_x, player_y))
        
    def think(self):
        super().think()
        self.move()
    
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
        return speed
        
    def get_speed(self):
        return self.speed
    
    def is_player(self):
        return True