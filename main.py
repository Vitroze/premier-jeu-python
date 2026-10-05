import asyncio
import pygame

pygame.init()
screen = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Mon jeu")
clock = pygame.time.Clock()


async def main():
    # Position et vitesse du joueur
    x, y = 240, 180
    vitesse = 4

    running = True
    while running:
        # 1. Evenements : fermeture de la fenetre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Deplacement avec les fleches du clavier
        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT]:
            x -= vitesse
        if touches[pygame.K_RIGHT]:
            x += vitesse
        if touches[pygame.K_UP]:
            y -= vitesse
        if touches[pygame.K_DOWN]:
            y += vitesse

        # 3. Dessin
        screen.fill((30, 30, 40))
        pygame.draw.circle(screen, (124, 92, 255), (x, y), 20)
        pygame.display.flip()

        # 4. Laisse le navigateur respirer (obligatoire), 60 images par seconde
        await asyncio.sleep(0)
        clock.tick(60)

    pygame.quit()


asyncio.run(main())
