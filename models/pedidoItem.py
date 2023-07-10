class PedidoItem: 
    def __init__(self,id, produto_id, pedido_id, quantidade, preco_total):
        self.id = id
        self.produto_id = produto_id
        self.pedido_id = pedido_id
        self.quantidade = quantidade
        self.preco_total = preco_total

    def __str__():
        return f"{self.id}-{self.produto_id}-{self.preco_total}"