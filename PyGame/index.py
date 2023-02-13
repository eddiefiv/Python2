import sys
import os
import pygame

from sprite import Player, Wall

# Init screen and size
width, height = 600, 600
screen = pygame.display.set_mode((width , height))

# Define sprite groups
player_sprites = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()

# Create sprites and add them to groups
player = Player((200, 200), (20, 20), screen)
wall = Wall((300, 300), (20, 150), (width, height))
player_sprites.add(player)
wall_sprites.add(wall)

# Start clock
clock = pygame.time.Clock()

# Running loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Add screen details and draw sprites
    screen.fill("black")
    player_sprites.draw(screen)
    wall_sprites.draw(screen)

    # Update player data every tick
    main_player = None
    for player in player_sprites:
        player.movement_enabled = True
        player.set_collision_group(wall_sprites)
        main_player = player
    player_sprites.update()
    pygame.display.update()

    # Set clock tick to 60 ticks
    clock.tick(60)