import pygame

def Clamp(value, min_value, max_value):
    if value > max_value:
        value = max_value
    elif value < min_value:
        value = min_value
    
    return value

all_entities = []
def get_all_entities():
    return all_entities

class Entity(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.health = 100
        self.image = None
        self.collision_bounds = None
        self.position = (0, 0)
        self.blacklist = []

        all_entities.append(self)
    
    def is_player(self):
        return False
    
    def is_npc(self):
        return False
    
    def set_health(self, health):
        if not health or type(health) != int or health < 0:
            return
        
        self.health = health
        
    def get_health(self):
        return self.health
    
    def set_material(self, picture:str, scale=None):
        if not picture or len(picture) == 0:
            return

        try:
            self.image = pygame.image.load(picture, "")
            
            if self.image and scale != None and type(scale) == tuple:
                self.image = pygame.transform.scale(self.image, scale)

            self.collision_bounds = self.image.get_rect()
        except:
            pass
        
    def get_material(self):
        return self.image
    
    def think(self): 
        if not self.collision_bounds:
            return

        for entity in all_entities:
            if entity == self or self.blacklist and entity in self.blacklist:
                continue
                
            if not entity.collision_bounds:
                continue
    
            if entity.collision_bounds.colliderect(self.collision_bounds):
                self.on_collision_bounds(entity)
    
    def paint(self):
        screen = self.screen
        if not screen:
            return

        picture = self.get_material()
        if not picture or not self.position:
            return
        
        screen.blit(picture, self.position)

    def on_collision_bounds(self, target):
        pass
    
    def set_pos(self, position):
        if not position or type(position) != tuple or type(position[0]) != int or type(position[1]) != int:
            return
        
        self.position = position
        if self.collision_bounds:
            self.collision_bounds.topleft = position # Update Collision Bounds
    
    def get_pos(self):
        return self.position
    
    def remove(self):
        all_entities.remove(self)
        del self