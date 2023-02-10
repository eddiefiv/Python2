import math
import pygame

from utils.direction import Direction

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, size, world_size):
        super().__init__()
        self.pos = pos
        self.image = pygame.Surface((size[0] , size[1]))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft = pos)
        self.rect_pixels = []
        self.world_bounds = world_size
        self.jump_height = 20
        self.x_velocity = 0
        self.y_velocity = self.jump_height
        self.x_gravity = 0
        self.y_gravity = 1
        self.jumping = False
        self.in_air = False
        self.direction = Direction.STATIC
        self.movement_enabled = True
        self.allow_outofbounds = False
        self.has_collision = True
        self.gravity = False

    def set_rect_pixels(self):
        for x in range(self.rect.topleft[0], self.rect.topright[0] + 1):
            for y in range(self.rect.topright[1], self.rect.bottomright[1] + 1):
                self.rect_pixels.append((x, y))

    def validate_pos(self, pos, rect):
        # Check for collision
        #print(f"Validating pos: {pos}")
        collision = self.check_collision(pos, rect)

        # If all checks pass, set final pos to checked pos
        if not collision:
            return pos
        return self.last_pos

    def move(self, direction: Direction, amount: int) -> tuple[int, int, pygame.Rect,  int, int, Direction]:
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
            new_rect.y -= amount
            return (self.pos[0], self.pos[1] - 10, new_rect, 0, 10, Direction.UP)
        if direction == Direction.DOWN:
            new_rect = self.rect
            new_rect.y += amount
            return (self.pos[0], self.pos[1] + 10, new_rect, 0, 10, Direction.DOWN)
        if direction == Direction.LEFT:
            new_rect = self.rect
            new_rect.x -= amount
            return (self.pos[0] - 10, self.pos[1], new_rect, -10, 0, Direction.LEFT)
        if direction == Direction.RIGHT:
            new_rect = self.rect
            new_rect.x += amount
            return (self.pos[0] + 10, self.pos[1], new_rect, 10, 0, Direction.RIGHT)
        if direction == Direction.UP_LEFT:
            self.validate_pos((self.pos[0] - 10, self.pos[1] - 10), self.rect)
            self.x_velocity = -amount
            self.y_velocity = -amount
        if direction == Direction.UP_RIGHT:
            self.validate_pos((self.pos[0] + 10, self.pos[1] - 10), self.rect)
            self.x_velocity = amount
            self.y_velocity = -amount
        if direction == Direction.DOWN_LEFT:
            self.validate_pos((self.pos[0] - 10, self.pos[1] + 10), self.rect)
            self.x_velocity = -amount
            self.y_velocity = amount
        if direction == Direction.DOWN_RIGHT:
            self.validate_pos((self.pos[0] + 10, self.pos[1] + 10), self.rect)
            self.x_velocity = amount
            self.y_velocity = amount

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

    def update(self):
        self.last_pos = self.pos
        if self.gravity:
            if self.direction == Direction.STATIC:
                movement = self.move(Direction.DOWN, 5)
                # Validate the future positions to make sure they are possible movements before actually setting them
                new_pos = self.validate_pos((movement[0], movement[1]), movement[2])
                # Update the position with either the old position due to an invalid move or the newly validated position
                self.pos = new_pos
                # Update the visible rectangle
                self.rect.x = new_pos[0]
                self.rect.y = new_pos[1]