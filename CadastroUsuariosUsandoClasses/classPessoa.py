class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    def setNome(self, nome):
        self.nome = nome
        
    def setIdade(self, idade):
        self.idade = idade
        
    def setSexo(self, sexo):
        self.sexo = sexo
        
    def getNome():
        return self.nome
        
    def getIdade():
        return self.idade
        
    def getSexo():
        return self.sexo
