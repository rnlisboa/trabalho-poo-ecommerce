class Categoria:
    def __init__(self, id, descricao):
        self._id = id
        self._descricao = descricao

    
    def get_id(self):
        return self._id

    
    def set_id(self, value):
        self._id = value

    
    def get_descricao(self):
        return self._descricao

    
    def set_descricao(self, value):
        self._descricao = value

    def __str__(self):
        return f"{self.id} - {self.descricao}"

