class Cliente:
    def __init__(self, id, usuario_id, cpf):
        self._id = id
        self._usuario = usuario_id
        self._cpf = cpf

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    def get_usuario(self):
        return self._usuario

    def set_usuario(self, value):
        self._usuario = value

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, value):
        self._cpf = value

    def __str__(self):
        return f"{self._id} - {self._cpf}"
