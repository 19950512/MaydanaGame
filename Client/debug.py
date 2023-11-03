import pygame
pygame.init()
font = pygame.font.SysFont('Arial', 30)

def debug(info, y = 100, x = 100):

    """
    text = font.render(info, True, 'white')
    screen = pygame.display.get_surface()
    screen.blit(text, (x, y))
    pygame.display.update()
    """

    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'white')
    debug_rect = debug_surf.get_rect(topright = (x, y))

    pygame.draw.rect(display_surface, 'black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)