from modelos.avaliacao import Avaliacao
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria): #constutor
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)#toda vez q criar um obj ele vai para a lista
        
        
    def __str__(self):#str ela pega o objeto e mostra em formato de texto
        return f' {self._nome} | {self.categoria}' #irá mostra as 2 info no print
    
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
            
    @property #modifica a forma que o atributo é lido
    def ativo(self):
        return '☒' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

  
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_notas = len(self._avaliacao)
        media = round (soma_das_notas/ qtd_notas, 1)
        return media 



