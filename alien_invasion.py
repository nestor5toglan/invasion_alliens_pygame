from asyncio import events
from hashlib import new
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
##création dune fenetre  pygame vide en creant une classe pour representer le jeu

class AlienInvasion:
    """classe globale pour gerer les actifs et comportement du jeux"""
    
    def __init__(self):
        """Initialisation du jeu et creation des ressources """
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        #definissez  la couleur d'arriere plan
        self.bg_color = (230,230,230)
        self.bullets = pygame.sprite.Group() #changement 2 cette ligne permet de dessiner des balles a lecran a chaque passage de la boucle 
        
    
    
    
    
    def run_game(self):
        """Démarrer la boucle principale du jeu"""
        while True:
            #surveiller  les évenements du clavier et de la sourri
            self._check_events()
            self.ship.update()
            self._update_bullets()
           # #self.bullets.update()#changement2 mise a jour de la position des balles a chaque passage dans la boucle 
           # #faire disparaitre les balles qui napparaissent plus a lecran pour economiser de la memoire
           # #for bullet in self.bullets.copy():
           # #    if bullet.rect.bottom <= 0 :
           # #        self.bullets.remove(bullet)
           # #print(len(self.bullets))

            self._update_screen()
            
           
    
    def _check_events(self):
        """surveiller  les évenements du clavier et de la sourri"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
             #   if event.key == pygame.K_RIGHT:
              #      # déplacer le navire vers la droite
               #   self.ship.moving_right = True
                #déplacer le navire vers la gauche
                #elif event.key == pygame.K_LEFT:
                #    self.ship.moving_left = True
                    
            elif event.type ==  pygame.KEYUP:
                 self._check_keyup_events(event)

             #   if event.key == pygame.K_RIGHT:
              #      self.ship.moving_right = False
               # elif event.key == pygame.K_LEFT:
               #     self.ship.moving_left = False
##décomposition par méthode de _check_events
    def _check_keydown_events(self, event):
        """répondre a la pression dune touche"""
        if event.key == pygame.K_RIGHT:
       # déplacer le navire vers la droite
            self.ship.moving_right = True
       #déplacer le navire vers la gauche
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        

    def _check_keyup_events(self, event):
        """repondre aux communiquer de clé"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        
    #voici la methode self.fire_bullet() ici
    def _fire_bullet(self):
        """creez une nouvelle balle puis ajoutez la au groupe de balle"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
##décomposition par méthode de _check_events
 # ajout dune nouvelle méthode _update_bullets() pour garder la classe AlienInvasion bien organisée
    def _update_bullets(self):
        """mettre à jour la position des balles et se debarrasser des vieilles balles """
        #mettre a jour la position des balles
        self.bullets.update()#changement2 mise a jour de la position des balles a chaque passage dans la boucle 
        #faire disparaitre les balles qui napparaissent plus a lecran pour economiser de la memoire
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0 :
                self.bullets.remove(bullet)


  
    
    
    def _update_screen(self):
        """mettre a jour les images de lecran et basculer vers le nouvel ecran"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #rendre visible l'ecran le plus recemment déssiné
        pygame.display.flip()

        
if __name__=='__main__':
    #creer une instance de jeu puis lancer le jeu
    ai = AlienInvasion()
    ai.run_game()
    
    
                
        

