import math
import pygame

from projectile import BaseProjectile

from enum import Enum

from utils.direction import Direction

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size, screen: pygame.Surface):
        super().__init__()
        self.pos = pos
        self.screen = screen
        self.image = pygame.Surface((size[0] , size[1]))
        self.image.fill("cyan")
        self.rect = self.image.get_rect(topleft = pos)
        self.rect_pixels = []
        self.world_bounds = (screen.get_width, screen.get_height)
        self.projectile_group = pygame.sprite.Group()
        self.x_velocity = 0
        self.y_velocity = 0
        self.direction = Direction.STATIC
        self.facing = Direction.RIGHT
        self.movement_enabled = True
        self.allow_outofbounds = False
        self.has_collision = True

    def set_rect_pixels(self):
        for x in range(self.rect.topleft[0], self.rect.topright[0] + 1):
            for y in range(self.rect.topright[1], self.rect.bottomright[1] + 1):
                self.rect_pixels.append((x, y))

    def move(self, direction: Direction) -> tuple[int, int, pygame.Rect,  int, int, Direction]:
        """
        Takes in an input direction, and returns:
        Tuple[int, int, int, int, Direction]
        int: new x pos
        int: new y pos
        rect: new rect
        int: new x velocity
        int: new y velocity
        Direction: new Direction
        """
        if direction == Direction.UP:
            new_rect = self.rect
            new_rect.y -= 10
            return (self.pos[0], self.pos[1] - 10, new_rect, 0, 10, Direction.UP)
        if direction == Direction.DOWN:
            new_rect = self.rect
            new_rect.y += 10
            return (self.pos[0], self.pos[1] + 10, new_rect, 0, 10, Direction.DOWN)
        if direction == Direction.LEFT:
            new_rect = self.rect
            new_rect.x -= 10
            return (self.pos[0] - 10, self.pos[1], new_rect, -10, 0, Direction.LEFT)
        if direction == Direction.RIGHT:
            new_rect = self.rect
            new_rect.x += 10
            return (self.pos[0] + 10, self.pos[1], new_rect, 10, 0, Direction.RIGHT)
        if direction == Direction.UP_LEFT:
            self.validate_pos((self.pos[0] - 10, self.pos[1] - 10), self.rect)
            self.x_velocity = -10
            self.y_velocity = -10
        if direction == Direction.UP_RIGHT:
            self.validate_pos((self.pos[0] + 10, self.pos[1] - 10), self.rect)
            self.x_velocity = 10
            self.y_velocity = -10
        if direction == Direction.DOWN_LEFT:
            self.validate_pos((self.pos[0] - 10, self.pos[1] + 10), self.rect)
            self.x_velocity = -10
            self.y_velocity = 10
        if direction == Direction.DOWN_RIGHT:
            self.validate_pos((self.pos[0] + 10, self.pos[1] + 10), self.rect)
            self.x_velocity = 10
            self.y_velocity = 10

    def validate_pos(self, pos, rect):
        # Check for collision
        #print(f"Validating pos: {pos}")
        collision = self.check_collision(pos, rect)

        # If all checks pass, set final pos to checked pos
        if not collision:
            return pos
        return self.last_pos

    def check_collision(self, pos, rect):
        if not self.allow_outofbounds:
            if pos[0] <= 0:
                self.pos = (1, self.pos[1])
                return True
            if pos[1] <= 0:
                self.pos = (self.pos[0], 1)
                return True
            if pos[0] >= self.world_bounds[0] - self.rect.size[0]:
                self.pos = ((self.world_bounds[0] - self.rect.size[0]) - 1, self.pos[1])
                return True
            if pos[1] >= self.world_bounds[1] - self.rect.size[1]:
                self.pos = (self.pos[0], (self.world_bounds[1] - self.rect.size[1]) - 1)
                return True
        if self.has_collision:
            #TODO: Player corner collision
            for sprite in self.collision_group:
                if rect.colliderect(sprite.rect) and sprite.has_collision:
                    if ((rect.right, (rect.topright[1] + math.floor(self.rect.size[1] / 2))) in sprite.rect_pixels):
                        #self.pos = (sprite.rect.left - self.rect.size[0], self.pos[1])
                        return True
                    # Player left collides with sprite right
                    elif ((rect.left, (rect.topleft[1] + math.floor(self.rect.size[1] / 2))) in sprite.rect_pixels):
                        #self.pos = (sprite.rect.right, self.pos[1])
                        return True
                    # Player bottom collides with sprite top
                    elif (((rect.bottomleft[0] + math.floor(rect.size[0] / 2)), rect.bottom)):
                        #self.pos = (self.pos[0], sprite.rect.top - self.rect.size[1])
                        return True
                    # Player top collides with sprite bottom
                    elif (((rect.topleft[0] + math.floor(rect.size[0] / 2)), rect.top)):
                        #self.pos = (self.pos[0], sprite.rect.bottom)
                        return True
                return False
        return False
    
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
            self.facing = Direction.DOWN
            movement = self.move(Direction.RIGHT)
            return movement
        # Left
        if keys[pygame.K_a] and self.movement_enabled:
            movement = self.move(Direction.LEFT)
            return movement
        # Up
        if keys[pygame.K_w] and self.movement_enabled:
            movement = self.move(Direction.UP)
            return movement
        # Down
        if keys[pygame.K_s] and self.movement_enabled:
            movement = self.move(Direction.DOWN)
            return movement
        if keys[pygame.K_SPACE]:
            new_proj = BaseProjectile(self, (5, 5), self.screen)
        # Invalid inputs
        if not any(keys):
            return (self.pos[0], self.pos[1], self.rect, 0, 0, Direction.STATIC)

    def update(self):
        # Return future movement positions
        data = self.get_input()
        self.last_pos = self.pos
        #print(f"Current pos: {self.pos}")
        # Validate the future positions to make sure they are possible movements before actually setting them
        new_pos = self.validate_pos((data[0], data[1]), data[2])
        # Update the position with either the old position due to an invalid move or the newly validated position
        self.pos = new_pos
        #print(f"New pos: {new_pos}")
        # Update the visible rectangle
        self.rect.x = new_pos[0]
        self.rect.y = new_pos[1]

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, size, world_size):
        super().__init__()
        self.pos = pos
        self.image = pygame.Surface((size[0] , size[1]))
        self.image.fill("gray")
        self.rect = self.image.get_rect(topleft = pos)
        self.rect_pixels = []
        self.x_velocity = 0
        self.y_velocity = 0
        self.movement_enabled = False
        self.allow_outofbounds = False
        self.has_collision = True

        self.set_rect_pixels()

    def set_rect_pixels(self):
        for x in range(self.rect.topleft[0], self.rect.topright[0] + 1):
            for y in range(self.rect.topright[1], self.rect.bottomright[1] + 1):
                self.rect_pixels.append((x, y))