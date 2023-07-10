class Pedido:
    def __init__(self,id, cliente_id, preco_total, data, finalizado=False):
        self.id = id
        self.cliente_id = cliente_id
        self.preco_total = preco_total
        self.data = data
        self.finalizado = finalizado

    def __str__():
        return f"{self.id}-{self.cliente_id}-{self.preco_total}"