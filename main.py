#import asyncio
import pygame
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

alien = Enemy(screen)
alien.set_material("assets/alien.png")

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

    for entity in get_all_entities():
            if entity.paint:
                try:
                    entity.paint()
                except Exception as e:
                    print(f"Erreur sur ENTITY:paint : {entity}: {type(e).__name__} - {e}")

            if entity.think:
                try:
                    entity.think()
                except Exception as e:
                    print(f"Erreur sur ENTITY:tick : {entity} : {type(e).__name__} - {e}")


    # Debug Mode
    drawText(police1, f"{clock.get_fps()}FPS", (0, 0, 0), (0, 0))
    drawText(police1, f"Temps en secondes :{time.time()}", (0, 0, 0), (0, 20))
    score = f"Score : {get_score()}"
    w, _ = police1.size(score)
    drawText(police1, score, (0, 0, 0), (screen.get_width() - w - 20, 0))
    # -----------------------------

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
