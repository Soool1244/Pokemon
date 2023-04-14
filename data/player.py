import pygame
class Player:
    def __init__(self,  sprite):
        self.pos = [0,0]
        self.pressed = pygame.key.get_pressed()
        self.sprite = sprite
    
    def update(self, map):
        if self.pressed[pygame.K_LEFT]:
            self.pos[0] -= 16
        elif self.pressed[pygame.K_RIGHT]:
            self.pos[0] += 16
        elif self.pressed[pygame.K_UP]:
            self.pos[1] -= 16
        elif self.pressed[pygame.K_DOWN]:
            self.pos[1] -= 16
        map.get_object_by_name("Player").x += self.pos[0]
        map.get_object_by_name("Player").y += self.pos[1]