import sys 
import pygame
from evaluation_settings import EvaluationSettingsAlien
from evaluation_vaisseau import EvaluationVaisseau


#créons une fenetre pygame avec un fond bleu

class EvaluationALienInvasion:
    """Cette classe est une classe globale pour gérer les actifs et les comportements globals du jeux"""
    def __init__(self):
        """Initialisation du jeu et création des ressources du jeu """
        pygame.init()
        self.evalusettings = EvaluationSettingsAlien()
        self.screen = pygame.display.set_mode((self.evalusettings.screen_width,self.evalusettings.screen_height))
        self.screen = pygame.display.set_mode((1000, 500))
        self.evaluationvaisseau = EvaluationVaisseau(self)
        pygame.display.set_caption("EvaluationALienInvasion")
        self.bg_color = (255,255,255)
        
    
    
    def evaluation_run_game(self):
        """Démarrer la boucle principale du jeu"""
        #Surveiller les évenements du clavier et de la souris
        while True:
            self._check_events()
            self._update_screen()
        
    def _check_events(self):
        """cette fonction est utilisée pour surveiller les évènements de la souris et du clavier """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                 
    def _update_screen(self):
        """cette fonction sera utilisé pour mettre a jour les images de lécran et de basculer vers un nouvel ecran"""
        self.screen.fill(self.evalusettings.bg_color)
        self.evaluationvaisseau.blitme_1()
        
       #rendre visible lécran récement déssiné
        pygame.display.flip()
       
        
if __name__=='__main__':
    #créons une instance de jeu puis lancer le jeu
    ai = EvaluationALienInvasion()
    ai.evaluation_run_game()
        
    