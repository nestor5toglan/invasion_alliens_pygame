
class EvaluationSettingsAlien:
    """Cette classe va être utilisé pour stocker tous les paramettre du jeu EvaluationAlienInvasion"""
    def __init__(self):
        """Initialisation des parametre du jeu"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,255)
        #parametre du vaisseau (vitesse)
        self.vaisseau_speed = 1.5 #changement1