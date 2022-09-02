import sys 
import pygame
from sideways_settings  import Settings

#creation dune fenetre pygamme vide en creant une classe  pour representer le jeu 

class SidewayShooter:
    """classe globale pour gerer les actifs  et les comportements du jeu """
    def __init__(self):
        """initialisation  du jeu et creation des ressources """
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("The Sideway Shooter")
        #
        #definition de la couleur de larriere plan 
        self.bg_color = (222,222,222)

    def run_game(self):
        """demarrer la boucle principale du jeu """

