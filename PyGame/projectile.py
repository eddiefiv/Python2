import math
import pygame

from utils.direction import Direction

class BaseProjectile(pygame.sprite.Sprite):
    def __init__(self, parent, size, screen: pygame.Surface):
        super().__init__()
        self.parent = parent
        self.screen = screen
        self.pos = parent.rect.center
        self.image = pygame.Surface((size[0] , size[1]))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft = self.pos)
        self.rect_pixels = []
        self.world_bounds = (screen.get_wdith, screen.get_height)
        self.collision_group = parent.collision_group
        self.x_velocity = 5
        self.y_velocity = 5
        self.allow_outofbounds = False

    def fire(self, orig: tuple[int, int], facing: Direction):
        if Direction == Direction.UP:
            while self.check_collision(self.pos, self.rect):


    def check_collision(self, pos, rect):
        if not self.allow_outofbounds:
            if pos[0] <= 0:
                return True
            if pos[1] <= 0:
                return True
            if pos[0] >= self.world_bounds[0] - self.rect.size[0]:
                return True
            if pos[1] >= self.world_bounds[1] - self.rect.size[1]:
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

    def draw(self):


    #def update(self):
