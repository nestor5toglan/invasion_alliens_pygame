import pygame

class Ship:
    """Une class pour gérer le vaisseau"""
    def __init__(self, ai_game):
        """initialisation du vaisseaux et mise en place de sa position de départ """
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        self.screen_rect = ai_game.screen.get_rect()
        
        #charger limage du navire puis obtener son rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #démarrer chaque nouveau navire en bas au centre de l'ecran
        self.rect.midbottom = self.screen_rect.midbottom
        
        #stocker une valeur décimale pour la position horizontale du navire
        self.x = float(self.rect.x)
        
        #drapeau pour suivre le mouvement
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """mettre a jour la position du navire en fonction des drapeau de mouvement"""
        #mettre a jour la valeur x du navire pas le rect 
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            
            #self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #mettre a jour lobjet rect de self.x.
        self.rect.x = self.x
            #self.rect.x -= 1
        
    def blitme(self):
        """Déssiner le vaisseau a son emplacement actuel"""
        self.screen.blit(self.image, self.rect)
        
        