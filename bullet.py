import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Cette class permet de gérer les balles tirées du navires"""
    
    def __init__(self,ai_game):
        """creons une balle a la position actuelle du vaisseau"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        #creer un bullet a (0,0) de coordonnée puis definissons la position correct
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        #stocker la position de la balle sous la forme de valeur decimal
        self.y = float(self.rect.y)
        
    def update(self):
        """déplacer les bullets (balles) vers le haut de lecran"""
         #mettre a jour la position decimale du bullet 
        self.y -= self.settings.bullet_speed
         #mettre a jour la position du rect
        self.rect.y = self.y
    
    def draw_bullet(self):
        """dessiner le bullet (balle) a lecran"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
         
        
        
        
        