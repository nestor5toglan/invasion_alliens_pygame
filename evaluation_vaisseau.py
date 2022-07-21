import pygame

class EvaluationVaisseau:
    """Une classe pour gérer le vaisseau ou le personnage principale de mon jeu"""
    def __init__(self,ai_jeux):
        """initialisation du vaisseau ou de mon personnage et mise en place de position de départ"""
        self.screen = ai_jeux.screen
        self.screen_rect = ai_jeux.screen.get_rect()
    
    #Charger limage du vaisseau ou du personnage puis donnée son rect
        self.image = pygame.image.load('images/blooper.bmp')
        self.rect = self.image.get_rect()
    #démarrer chaque nouveau navire en bas au centre de lecran
    
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme_1(self):
        """déssiner le vaisseau ou mon acteur personnage à son emplacement actuel"""
        self.screen.blit(self.image, self.rect)
        