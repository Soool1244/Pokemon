def keypressedcheck():
    import pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if event.type == pygame.KEYDOWN:
            if event.key == 27:
                pygame.quit()
                exit()
