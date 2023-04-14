import pytmx, pygame
from pytmx.util_pygame import load_pygame

class Tilemap:
    def __init__(self, file):
        self.map = load_pygame(file)
        self.width = self.map.tilewidth
        self.height = self.map.tileheight
        self.collision = self.map.get_layer_by_name('Collision')
        self.CAMERA = self.map.get_object_by_name("Player")
        self.tiles = []

    def render(self, screen, player, tisi):
        self.pos = [0,0]
        self.pressed = pygame.key.get_pressed()

        if self.pressed[pygame.K_LEFT]: self.pos[0] += 2
        elif self.pressed[pygame.K_RIGHT]: self.pos[0] -= 2
        if self.pressed[pygame.K_UP]: self.pos[1] += 2
        elif self.pressed[pygame.K_DOWN]: self.pos[1] -= 2

        x = self.map.get_object_by_name("Player").x+self.pos[0]
        y = self.map.get_object_by_name("Player").y+self.pos[1]
        w = self.map.get_object_by_name("Player").width
        h = self.map.get_object_by_name("Player").height
        playerrec = pygame.Rect([x,y,w,h])
        if (playerrec.collidelistall(self.tiles)): self.pos = [0,0]

        self.posx = self.CAMERA.x+(screen.get_width()/2)
        self.posy = self.CAMERA.y+(screen.get_height()/2)

        for layer in self.map.layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                self.tiles = []
                for x, y, tile in layer.tiles():
                    tile = pygame.transform.scale(tile,(tisi,tisi))
                    if (tile): screen.blit(tile, [(x * tisi - self.posx)+192, (y * tisi - self.posy)+210])
                for tile in self.collision:
                    if (tile): self.tiles.append(pygame.Rect([(x*self.width), (y*self.height), self.width, self.height]))

            elif isinstance(layer, pytmx.TiledObjectGroup):
                for object in layer:
                    if (object.type=='Player'):
                        player = pygame.transform.scale(player,(32,192))
                        screen.blit(player, [screen.get_width()/2,screen.get_height()/2],(0,0,32,32))
                        