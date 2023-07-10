class Produto:
    def __init__(self,id, descricao, estoque, preco, categoria_id):
        self.id = id
        self.descricao = descricao
        self.estoque = estoque
        self.preco = preco
        self.categoria_id = categoria_id

    def __str__():
        return f"{self.id}-{self.descricao}-{self.preco}"