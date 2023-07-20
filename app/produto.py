class Produto:
    def __init__(self, id, descricao, estoque, preco, categoria_id):
        self._id = id
        self._descricao = descricao
        self._estoque = estoque
        self._preco = preco
        self._categoria_id = categoria_id

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, value):
        self._descricao = value

    def get_estoque(self):
        return self._estoque

    def set_estoque(self, value):
        self._estoque = value

    def get_preco(self):
        return self._preco

    def set_preco(self, value):
        self._preco = value

    def get_categoria_id(self):
        return self._categoria_id

    def set_categoria_id(self, value):
        self._categoria_id = value

    def __str__(self):
        return f"{self._id}-{self._descricao}-{self._preco}"
