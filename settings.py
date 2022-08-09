


class Settings:
    """class pour stocker tous les parametres pour Alien Invasion"""
    
    def __init__(self):
        """initialisation des parametre du jeu"""
        #parametre décran
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        #parametre du navire 
        self.ship_speed = 1.5
        
        #paramettre de bullet (puces)## donc ce paramettre crée des puces gris de 3px qui se deplacent lentement par rapport au navire
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        
        
        
        
        