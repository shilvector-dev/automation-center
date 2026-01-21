#Cérebro primário do Centro de Automações KhanesIA

MODOS_VALIDOS = ["off", "acompanhando", "trabalhando"]

class Engine:
    def __init__(self):
        self.modo = "OFF"
    
    def mudar_modo(self, novo_modo):
        self.modo = novo_modo
    
    def get_modo(self):
        return self.modo