class Cliente:
    def __init__(self, id, usuario, nome, email, senha, cpf):
        self._id = id
        self._usuario = usuario
        self._nome = nome
        self._email = email
        self._senha = senha
        self._cpf = cpf

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    def get_usuario(self):
        return self._usuario

    def set_usuario(self, value):
        self._usuario = value

    def get_nome(self):
        return self._nome

    def set_nome(self, value):
        self._nome = value

    def get_email(self):
        return self._email

    def set_email(self, value):
        self._email = value

    def get_senha(self):
        return self._senha

    def set_senha(self, value):
        self._senha = value

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, value):
        self._cpf = value

    def __str__(self):
        return f"{self._id} - {self._nome}"
