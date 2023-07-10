class Cliente:
    def __init__(self,id, usuario, nome, email, senha, cpf):
        self.id = id
        self.usuario = usuario
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf

    def __str__():
        return f"{self.id}-{self.nome}"