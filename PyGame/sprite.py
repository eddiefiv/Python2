import pygame

from enum import Enum

class Direction(Enum):
    LEFT = "Left"
    RIGHT = "Right"
    UP = "Up"
    DOWN = "Down"

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size, world_size):
        super().__init__()
        self.pos = pos
        self.image = pygame.Surface((size[0] , size[1]))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft = pos)
        self.world_bounds = world_size
        self.x_velocity = 0
        self.y_velocity = 0
        self.movement_enabled = True
        self.allow_outofbounds = False
        self.has_collision = True

    def move(self, direction: Direction):
        if direction == Direction.UP:
           self.validate_pos((self.pos[0], self.pos[1] - 10))
        if direction == Direction.DOWN:
            self.validate_pos((self.pos[0], self.pos[1] + 10))
        if direction == Direction.LEFT:
            self.validate_pos((self.pos[0] - 10, self.pos[1]))
        if direction == Direction.RIGHT:
            self.validate_pos((self.pos[0] + 10, self.pos[1]))

    def validate_pos(self, pos):
        # Check for collision
        collision = self.check_collision(pos)

        # If all checks pass, set final pos to checked pos
        if not collision:
            self.pos = pos

    def check_collision(self, pos):
        if not self.allow_outofbounds:
            if pos[0] <= 0:
                self.pos = (0, self.pos[1])
                return True
            if pos[1] <= 0:
                self.pos = (self.pos[0], 0)
                return True
            if pos[0] >= self.world_bounds[0] - self.rect.size[0]:
                self.pos = (self.world_bounds[0] - self.rect.size[0], self.pos[1])
                return True
            if pos[1] >= self.world_bounds[1] - self.rect.size[1]:
                self.pos = (self.pos[0], self.world_bounds[1] - self.rect.size[1])
                return True
        if self.has_collision:
            for sprite in self.collision_group:
                if self.rect.colliderect(sprite.rect) and sprite.has_collision:
                    # Player right collides with sprite left
                    if (pos[0] - self.rect.size[0]) >= ((sprite.pos[0]) and (pos[0] - self.rect.size[0] <= (sprite.pos[0] + sprite.rect.size[0]))):
                        print("Collided with left")
                        self.pos = ((sprite.pos[0] - self.rect.size[0]), pos[1])
                        return True
                    # Player left collides with sprite right
                    if (pos[0] <= (sprite.pos[0] + sprite.rect.size[0])):
                        print("Collided with right")
                        #TODO: Check over this, idk if its right or not yet tbh
                        self.pos = ((sprite.pos[0] + sprite.rect.size[0]), pos[1])
        return False
    
    def set_collision_group(self, group):
        self.collision_group = group
    
    def set_velocity(self, x: int, y: int):
        self.x_velocity = x
        self.y_velocity = y

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.movement_enabled:
            self.move(Direction.RIGHT)
        if keys[pygame.K_LEFT] and self.movement_enabled:
            self.move(Direction.LEFT)
        if keys[pygame.K_UP] and self.movement_enabled:
            self.move(Direction.UP)
        if keys[pygame.K_DOWN] and self.movement_enabled:
            self.move(Direction.DOWN)

    def update(self):
        self.get_input()
        self.last_pos = self.pos
        self.check_collision(self.pos)
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, size, world_size):
        super().__init__()
        self.pos = pos
        self.image = pygame.Surface((size[0] , size[1]))
        self.image.fill("cyan")
        self.rect = self.image.get_rect(topleft = pos)
        self.x_velocity = 0
        self.y_velocity = 0
        self.movement_enabled = False
        self.allow_outofbounds = False
        self.has_collision = True

    