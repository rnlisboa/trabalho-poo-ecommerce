class Usuario:
    def __init__(self,id, nome, email, senha, is_admin=False):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.is_admin = is_admin

    def __str__():
        return f"{self.id}-{self.nome}"