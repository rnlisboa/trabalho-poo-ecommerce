class PedidoItem:
    def __init__(self, id, produto_id, pedido_id, quantidade, preco_total):
        self._id = id
        self._produto_id = produto_id
        self._pedido_id = pedido_id
        self._quantidade = quantidade
        self._preco_total = preco_total

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    def get_produto_id(self):
        return self._produto_id

    def set_produto_id(self, value):
        self._produto_id = value

    def get_pedido_id(self):
        return self._pedido_id

    def set_pedido_id(self, value):
        self._pedido_id = value

    def get_quantidade(self):
        return self._quantidade

    def set_quantidade(self, value):
        self._quantidade = value

    def get_preco_total(self):
        return self._preco_total

    def set_preco_total(self, value):
        self._preco_total = value

    def __str__(self):
        return f"{self._id}-{self._produto_id}-{self._preco_total}"
