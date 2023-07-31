import os, json
from pedidoItem import PedidoItem
from NPedido import NPedido
from NProduto import NProduto
class NPedidoItem:
    def __init__(self):
        pedido_item = []
    
    def listar(self):
        return self.ler_arquivo('pedidoItem.json')
    
    def ver(self):
        pedidoItems = self.listar()
        for pedidoItem_id in pedidoItems:
            if pedidoItem_id == id:
                return pedidoItems[pedidoItem_id]
    
    def cadastrar(self, produto_id, pedido_id, quantidade):
        pedidos_item = self.listar()
        if produto_id not in NProduto().listar().keys(): return "Produto não encontrado"
        if quantidade < 0: return "Quantidade inválida."
        produto = NProduto().ver(produto_id)
        estoque_antigo = produto['estoque']
        novo_estoque = estoque_antigo - quantidade
        if novo_estoque < 0: return "Quantidade insuficiente para o seu pedido."
        NProduto().atualizar(produto_id, '', novo_estoque, '','')
        
        preco_total = produto['preco'] * quantidade
        
        id = len(pedidos_item) + 1
        novo_pedido = PedidoItem(id, produto_id, pedido_id, quantidade, preco_total)
        nova_lista = []
        for pedido_item_id in pedidos_item:
            p = PedidoItem(
            pedido_items[pedido_item_id]['id'],
            pedido_items[pedido_item_id]['produto_id'],
            pedido_items[pedido_item_id]['pedido_id'],
            pedido_items[pedido_item_id]['quantidade'],
            pedido_items[pedido_item_id]['preco_total']
            )
            nova_lista.append(p)
        nova_lista.append(novo_pedido)

        self.grava_arquivo(nova_lista, 'pedidoItem.json')
        return "Item cadastrado com sucesso!"
    
    def atualizar(self, id, quantidade):
        items = self.listar()
        item = self.ver(id)

        if not item: return "Item não encontrado"

        if quantidade < 0: return "Quantidade inválida."
        items[id]['quantidade'] = quantidade
        nova_lista = []
        for pedido_item_id in pedido_items:
            p = PedidoItem(
            pedido_items[pedido_item_id]['id'],
            pedido_items[pedido_item_id]['produto_id'],
            pedido_items[pedido_item_id]['pedido_id'],
            pedido_items[pedido_item_id]['quantidade'],
            pedido_items[pedido_item_id]['preco_total']
            )
            nova_lista.append(p)
        self.grava_arquivo(nova_lista, 'pedidoItem.json')
        return "Item cadastrado com sucesso!"
    
    def excluir(self, id):
        items = self.listar()
        del items[id]
        for pedido_item_id in pedido_items:
            p = PedidoItem(
            pedido_items[pedido_item_id]['id'],
            pedido_items[pedido_item_id]['produto_id'],
            pedido_items[pedido_item_id]['pedido_id'],
            pedido_items[pedido_item_id]['quantidade'],
            pedido_items[pedido_item_id]['preco_total']
            )
            nova_lista.append(p)
        self.grava_arquivo(nova_lista, 'pedidoItem.json')
        return "Item removido com sucesso!"
    @staticmethod
    def grava_arquivo(items: list, arquivo: str):
        diretorio_atual = os.path.dirname(os.path.realpath(__file__))
        arquivo_nome = diretorio_atual +  f'\\base_dados\\{arquivo}' 
        dict_item = {}
        for item in items: 
            key = item.get_id()
            dict_item[key] = {
                "id": item.get_id(),
                "produto_id": item.get_produto_id(),
                "pedido_id": item.get_pedido_id(),
                "quantidade": item.get_quantidade(),
                "preco_total": item.get_preco_total()
            }
        
        objeto = json.dumps(dict_item, indent = 4)
        with open(arquivo_nome, 'w', encoding='utf-8') as f:
            f.write(objeto)

    @staticmethod
    def ler_arquivo(arquivo):
        diretorio_atual = os.path.dirname(os.path.realpath(__file__))
        arquivo_nome = diretorio_atual +  f'\\base_dados\\{arquivo}'
        try:
            with open(arquivo_nome, 'r', encoding='utf-8') as f:
                lista = f.read()
                if lista != '':
                    item = json.loads(lista)
                else:
                    item = {}
            return item
        except Exception as e:
            return {}