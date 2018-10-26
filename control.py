class Control:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def exibir_menu(self):
        #Acionar o metodo da classe
        self.view.exibir_menu()

    #Metodo para recuperar lista
    def get_lista_compras(self):
        return self.model.get_lista_compras()

