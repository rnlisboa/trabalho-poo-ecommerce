class Pedido:
    def __init__(self, id, cliente_id, preco_total, data, finalizado=False):
        self._id = id
        self._cliente_id = cliente_id
        self._preco_total = preco_total
        self._data = data
        self._finalizado = finalizado

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    def get_cliente_id(self):
        return self._cliente_id

    def set_cliente_id(self, value):
        self._cliente_id = value

    def get_preco_total(self):
        return self._preco_total

    def set_preco_total(self, value):
        self._preco_total = value

    def get_data(self):
        return self._data

    def set_data(self, value):
        self._data = value

    def is_finalizado(self):
        return self._finalizado

    def set_finalizado(self, value):
        self._finalizado = value

    def __str__(self):
        return f"{self._id}-{self._cliente_id}-{self._preco_total}"
