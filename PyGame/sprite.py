import math
import pygame

from enum import Enum
from utils.direction import Direction
from utils.custom_sprite import Sprite as CustomSprite

class Player(CustomSprite):
    def __init__(self, pos, size, world_size):
        super().__init__(pos, size, world_size)

    def set_collision_group(self, group):
        self.collision_group = group

    def set_velocity(self, x: int, y: int):
        self.x_velocity = x
        self.y_velocity = y

    def get_input(self):
        """
        Depending on the direction pressed, return future position values to be checked for collision
        """
        keys = pygame.key.get_pressed()
        # Right
        if keys[pygame.K_d] and self.movement_enabled:
            movement = self.move(Direction.RIGHT, 10)
            return movement
        # Left
        if keys[pygame.K_a] and self.movement_enabled:
            movement = self.move(Direction.LEFT, 10)
            return movement
        # Up
        if keys[pygame.K_w] and self.movement_enabled:
            movement = self.move(Direction.UP, 10)
            return movement
        # Down
        if keys[pygame.K_s] and self.movement_enabled:
            movement = self.move(Direction.DOWN, 10)
            return movement
        if keys[pygame.K_SPACE] and not self.jumping:
            self.jump()
            return None
        # Invalid inputs
        if not any(keys):
            return (self.pos[0], self.pos[1], self.rect, 0, 0, Direction.STATIC)

    def jump(self):
        new_y_pos = self.pos[1] - self.jump_height
        self.pos = (self.pos[0], new_y_pos)
        self.y_velocity -= self.y_gravity
        if self.y_velocity < -self.jump_height:
            self.jumping = False
            self.y_velocity = self.jump_height

    def update(self):
        super().update()
        # Return future movement positions
        data = self.get_input()
        self.last_pos = self.pos
        #print(f"Current pos: {self.pos}")
        # Validate the future positions to make sure they are possible movements before actually setting them
        if data == None:
            pass
        else:
            new_pos = self.validate_pos((data[0], data[1]), data[2])
            # Update the position with either the old position due to an invalid move or the newly validated position
            self.pos = new_pos
            #print(f"New pos: {new_pos}")
            # Update the visible rectangle
            self.rect.x = new_pos[0]
            self.rect.y = new_pos[1]

class Wall(CustomSprite):
    def __init__(self, pos, size, world_size):
        super().__init__(pos, size, world_size)
        self.image.fill("cyan")
        self.movement_enabled = False
        self.has_collision = True
        self.gravity = False