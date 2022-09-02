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
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.evalusettings.screen_width = self.screen.get_rect().width
        self.evalusettings.screen_height = self.screen.get_rect().height

        self.evaluationvaisseau = EvaluationVaisseau(self)
        pygame.display.set_caption("EvaluationALienInvasion")
        self.bg_color = (255,255,255)
        
    
    
    def evaluation_run_game(self):
        """Démarrer la boucle principale du jeu"""
        #Surveiller les évenements du clavier et de la souris
        while True:
            self._check_events()
            self.evaluationvaisseau.evalu_update() #changement 1
            self._update_screen()
        
    def _check_events(self):
        """cette fonction est utilisée pour surveiller les évènements de la souris et du clavier """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #appel de la fonction _check_keydown_event effective suite a lécoute et a la pression dune touche correspondant au clavier
            elif event.type == pygame.KEYDOWN:
                #appellons la procedure a effectuée  de _check_keydown_event
                self._check_keydown_event(event)
            #appel de la fonction _check_keyup_event effective suite a lécoute et au relachement dune touche correspondant au clavier
            elif event.type == pygame.KEYUP:
                 #appellons la procedure a effectuée de _check_keyup_event
                 self._check_keyup_event(event)

                

                 
    
    #decomposition par methode de _check_events(changement1) ajout de fonction complet _check_keydown_event
    def _check_keydown_event(self, event):
        """repondre a la pression dune touche en suivant uniquement le drapeau ici"""
        if event.key == pygame.K_RIGHT:
        #déplacer le navire vers la droite
            self.evaluationvaisseau.moving_right = True
        #sinon si cest le contraire alors deplacer le navire vers la gauche
        elif event.key == pygame.K_LEFT:
            self.evaluationvaisseau.moving_left = True
        #sinon si cest vers le haut deplacer deplacer le navire vers le haut
        elif event.key == pygame.K_UP:
            self.evaluationvaisseau.moving_top = True
        #sinon si cest vers le bas deplacer deplacer le navire vers le bas
        elif event.key == pygame.K_DOWN:
            self.evaluationvaisseau.moving_bottom = True

        #sinon si cest un appuis sur la touche 'q' alors fermer la console de jeux
        elif event.key == pygame.K_q:
            sys.exit()    
        
        
    #decomposition par methode de _check_events(changement1) ajout de fonction complet  _check_keyup_event   
    
    def _check_keyup_event(self, event): #changement1 
        """repondre au communiquer dune clé cest à dire au relachement dune touche en suivant le drapeau uniquement ici """
        #si la touche droite est relacher # alors on met le drapeau a false et la boucle qui fait bouger le navire a droite  sarrete
        if event.key == pygame.K_RIGHT:
            self.evaluationvaisseau.moving_right = False
        
            
        #si la touche gauche est relacher # alors on met le drapeau a false et la boucle qui fait bouger le navire a gauche sarrete
        elif event.key == pygame.K_LEFT:
            self.evaluationvaisseau.moving_left = False
        #si la touche haut est relacher # alors on met le drapeau a false et la boucle qui fait bouger le navire en haut sarrete
        elif event.key == pygame.K_UP:
            self.evaluationvaisseau.moving_top = False
        #si la touche basse est relacher # alors on met le drapeau a false et la boucle qui fait bouger le navire le bas sarrete
        elif event.key == pygame.K_DOWN:
            self.evaluationvaisseau.moving_bottom = False

            
            
    
                 
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
        
    