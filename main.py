#import asyncio
import pygame
import random
import time
from entity import *
from player import *
from enemy import *
from utils import get_score

pygame.init() # Load component (collide, sprites, scene)
screen = pygame.display.set_mode((1080, 720)) # Size frame
pygame.display.set_caption("My first game") # Title
clock = pygame.time.Clock() # FPS (Frame Per Seconds)

# Load a background picture
background = pygame.image.load("assets/background.jpg")
background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

# Load Player
player = Player(screen)
player.set_material("assets/player.png", (100, 100))
running = True

# alien = pygame.image.load("assets/alien.png")
# alien_rect = alien.get_rect() # Create collision bounds

alien = Enemy(screen)
alien.set_material("assets/alien.png")
# def move(keys):
#     global player_x, player_y
    
#     speed = 8 if keys[pygame.K_LSHIFT] else 4
    
#     moves = {
#         pygame.K_LEFT: (-speed, 0),
#         pygame.K_RIGHT: (speed, 0),
#         pygame.K_UP: (0, -speed),
#         pygame.K_DOWN: (0, speed),
#     }
    
#     for key, (dx, dy) in moves.items():
#         if keys[key]:
#             player_x += dx
#             player_y += dy

#     player_x = Clamp(player_x, 0, screen.get_width() - player.get_width())
#     player_y = Clamp(player_y, 0, screen.get_height() - player.get_height())
#     player_rect.topleft = (player_x, player_y) # Update collision bounds

# def update_position_alien(no_cooldown=False):
#     global time_cooldown
#     if time.time() < time_cooldown and not no_cooldown:
#         return
    
#     global alien_x, alien_y
    
#     alien_x = random.randint(0, screen.get_width() - alien.get_width())
#     alien_y = random.randint(0, screen.get_height() - alien.get_height())
#     time_cooldown = time.time() + random.randint(2, 10)
#     alien_rect.topleft = (alien_x, alien_y) # Update Collision Bounds

pygame.font.init()
police1 = pygame.font.SysFont("Arial", 20)

def drawText(police, text, color=(0, 0, 0), pos=(0, 0)):
    text = police.render(text, 1, color)
    screen.blit(text, pos)

while running: # Game loop to update the screen in real time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.blit(background, (0, 0))
    # screen.blit(player, (player_x, player_y))

    # screen.blit(alien, (alien_x, alien_y))
    # update_position_alien()

    for entity in get_all_entities():
            if entity.paint:
                try:
                    entity.paint()
                except Exception as e:
                    print(f"Erreur sur ENTITY:paint : {entity}: {type(e).__name__} - {e}")

            if entity.tick:
                try:
                    entity.tick()
                except Exception as e:
                    print(f"Erreur sur ENTITY:tick : {entity} : {type(e).__name__} - {e}")


    # if player_rect.colliderect(alien_rect):
    #     update_position_alien(True)

    # Debug Mode
    #text = police1.render(f"{clock.get_fps()}FPS", 1, (0, 0, 0))
    #screen.blit(text, (0, 0))
    drawText(police1, f"{clock.get_fps()}FPS", (0, 0, 0), (0, 0))
    drawText(police1, f"Temps en secondes :{time.time()}", (0, 0, 0), (0, 20))
    score = f"Score : {get_score()}"
    w, _ = police1.size(score)
    drawText(police1, score, (0, 0, 0), (screen.get_width() - w - 20, 0))
    # -----------------------------

    clock.tick(60)

print("quit")
pygame.quit()

# async def main():
#     # Position et vitesse du joueur
#     x, y = 240, 180
#     vitesse = 4

#     running = True
#     while running:
#         # 1. Evenements : fermeture de la fenetre
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         # 2. Deplacement avec les fleches du clavier
#         touches = pygame.key.get_pressed()
#         if touches[pygame.K_LEFT]:
#             x -= vitesse
#         if touches[pygame.K_RIGHT]:
#             x += vitesse
#         if touches[pygame.K_UP]:
#             y -= vitesse
#         if touches[pygame.K_DOWN]:
#             y += vitesse

#         # 3. Dessin
#         screen.fill((30, 30, 40))
#         pygame.draw.circle(screen, (124, 92, 255), (x, y), 20)
#         pygame.display.flip()

#         # 4. Laisse le navigateur respirer (obligatoire), 60 images par seconde
#         await asyncio.sleep(0)
#         clock.tick(60) # Set FPS (60 fps)

#     pygame.quit() 

 
# asyncio.run(main())

