from selectors import EVENT_READ
import sys
import pygame
from tpscreen_vide_settings import EcranSettings

##ce fichier creer un ecran de jeu vide 
class JustEcranVide:
    """cette classe est une classe globale pour gerer les actifs et comportements du jeu"""
    def __init__(self):
        """initialisation et creation des ressources du jeu"""
        pygame.init()
        self.monsettings = EcranSettings()
        self.screen = pygame.display.set_mode((self.monsettings.screen_width,self.monsettings.screen_height))
        #self.screen = pygame.display.setmode((0,0), pygame.FULLSCREEN)
        self.monsettings.screen_width = self.screen.get_rect().width
        self.monsettings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('just_lecran_vide_de_test')
        #definission de la couleur de larriere plan
        self.bg_color = (240,250,200)
    
    
    def run_screen_game(self):
        """cette methode permet de demarrer la boucle principal du jeu"""
        while True:
            self._check_events()
            self._update_screen()
    
    def _check_events(self):
        """methode utiliser pour detecter et surveiler les évenements du clavier et de la souris"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
            elif  event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
                
                 
    
    def _check_keydown_event(self,event):
        """repondre a la pression dune touche """
        if event.key == pygame.K_RIGHT:
        #alors imprimer lattribut de event.key correspondant
            event = pygame.K_RIGHT
            print(f"{event}")
        elif event.key == pygame.K_LEFT:
        #alors imprimer lattribut de event.key correspondant
            event = pygame.K_LEFT
            print(f"{event}")
        elif event.key == pygame.K_q:
        #alors imprimer lattribut de event.key correspondant
            event = pygame.K_q
            print(f"{event}")
            sys.exit()    
            
        
                 
    def _update_screen(self):
        """methode utiliser pour a chaque fois mettre a jour lecran"""
        self.screen.fill(self.monsettings.bg_color)
        #rendre lecran le plus recement dessinné visible
        pygame.display.flip()
    
    
    
if __name__ == '__main__':
    #creons une instance de jeu puis lançons le jeu
    ai = JustEcranVide()
    ai.run_screen_game()
        
           
        
        
        
