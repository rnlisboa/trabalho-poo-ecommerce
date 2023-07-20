class Usuario:
    def __init__(self, id, nome, email, senha, is_admin=False):
        self._id = id
        self._nome = nome
        self._email = email
        self._senha = senha
        self._is_admin = is_admin

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

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

    def get_is_admin(self):
        return self._is_admin

    def set_admin(self, value):
        self._is_admin = value

    def __str__(self):
        return f"{self._id}-{self._nome}"
