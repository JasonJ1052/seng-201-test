import sys
import pygame


# 1. Must be done before anything else. Just call it and forget it.
pygame.init()

# 2. Create display "Surface"
screen = pygame.display.set_mode((800, 400))  # window size: 800 pixels wide, 400 pixels high.
pygame.display.set_caption('Runner')  # window title
clock = pygame.time.Clock()  # initialize the clock, which helps manage framerate.

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_font = pygame.font.Font('font/pixeltype.ttf', 50)
score_surface = score_font.render('My game', False, (64, 64, 64))
score_rect = score_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0


# Infinite game loop.
while True:
    for event in pygame.event.get():  # gives a list of ONGOING mouse clicks, key presses, and window events
        if event.type == pygame.QUIT:
            pygame.quit()  # opposite of pygame.init().
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20

    # TODO: Specify the contents to draw.
    # BLIT: Block Image Transfer
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(score_surface, score_rect)

    # move the snail
    snail_rect.x -= 4
    if snail_rect.right < 0:
        snail_rect.left = 800

    screen.blit(snail_surface, snail_rect)

    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 300:
        player_rect.bottom = 300

    screen.blit(player_surface, player_rect)

    if player_rect.colliderect(snail_rect):
        print("u ded dawg")


    pygame.display.update()  # tells pygame to redraw the contents of the display.
    clock.tick(60)  # pauses to ensure the game runs at most 60 frames per second (FPS)