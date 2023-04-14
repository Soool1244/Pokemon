class Game:
    def __init__(self):
        # --- INIT --- 
        import pygame, os, data.player, data.tiles
        pygame.init()
        # --- CONSTANTS ---
        self.screen = pygame.display.set_mode((720, 480))
        self.running = True
        self.FPS = 60
        self.clock = pygame.time.Clock()
        # --- DISPLAY ---
        pygame.display.set_caption("Pokèmon Yellow 2")
        pygame.display.set_icon(pygame.image.load(os.getcwd()+"/sprites/icon.png"))
        # --- PLAYER ---
        self.player = pygame.image.load(os.getcwd()+"\\sprites\\sprites\\red.png").convert()
        self.player.set_colorkey(pygame.Color(255,255,255))
        # --- MAPS ---
        self.test_file = os.getcwd()+"\\maps\\test.tmx"
        self.test = data.tiles.Tilemap(self.test_file)
    
    def run(self):
        import data.keypress as keycheck, data.color as color, pygame
        while self.running:
            # Update Keys
            dt = self.clock.tick(self.FPS) / 1000
            keycheck.keypressedcheck()
            # Clear the screen and draw
            self.screen.fill(color.WHITE)
            self.test.render(self.screen, self.player, 16)
            pygame.display.update()