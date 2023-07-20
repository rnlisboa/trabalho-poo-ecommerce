class Categoria:
    def __init__(self, id, descricao):
        self._id = id
        self._descricao = descricao

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    def __str__(self):
        return f"{self.id} - {self.descricao}"

