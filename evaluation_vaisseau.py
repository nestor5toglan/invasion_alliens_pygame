import pygame

class EvaluationVaisseau:
    """Une classe pour gérer le vaisseau ou le personnage principale de mon jeu"""
    def __init__(self,ai_jeux):
        """initialisation du vaisseau ou de mon personnage et mise en place de position de départ"""
        self.screen = ai_jeux.screen
        self.evalusettings = ai_jeux.evalusettings
        self.screen_rect = ai_jeux.screen.get_rect()
    
    #Charger limage du vaisseau ou du personnage puis donnée son rect
        self.image = pygame.image.load('images/blooper.bmp')
        self.rect = self.image.get_rect()
    #démarrer chaque nouveau navire en bas au centre de lecran
    
        self.rect.midbottom = self.screen_rect.midbottom
    #stocker une valeur decimal pour la positiion horizontale du vaisseau
        self.x = float(self.rect.x) #changement1
    #stocker une valeur decimal pour la positiion vertical du vaisseau
        self.y = float(self.rect.y) #changement1
    #initialisation de drapeau pour suivre et controler le mouvement du vaisseau
        self.moving_right = False #changement1
        self.moving_left = False  #changement1
        self.moving_top = False #changement1
        self.moving_bottom = False #changement1
   
            

    
    def evalu_update(self):#changement 1 cest une nouvelle fonction entierement ajoutée
        """mettre à jour la position du vaisseau en fonction du drapeau"""
         #mettre dabord a jour la valeur x vaisseau pas le rect
        if self.moving_right and self.rect.right <  self.screen_rect.right :
            self.x += self.evalusettings.vaisseau_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.evalusettings.vaisseau_speed
        if self.moving_top and self.rect.top > self.screen_rect.top:
            self.y -= self.evalusettings.vaisseau_speed
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom: 
            self.y += self.evalusettings.vaisseau_speed 
        #mettre a jour le self.x
        self.rect.x = self.x
        #mettre a jour le self.y
        self.rect.y = self.y
            
        
    
    
    def blitme_1(self):
        """déssiner le vaisseau ou mon acteur personnage à son emplacement actuel"""
        self.screen.blit(self.image, self.rect)
        