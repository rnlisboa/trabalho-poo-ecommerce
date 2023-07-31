import os, json
from pedido import Pedido
from NCliente import NCliente

class NPedido:
    def __init__(self):
        self.pedidos = []
    
    def listar(self):
        return self.ler_arquivo('pedidos.json')
    
    def ver(self, id):
        pedidos = self.listar()
        for pedido_id in pedidos:
            if pedido_id == id:
                return pedidos[pedido_id]
    
    def cadastrar(self, cliente_id, preco_total, data):
        pedidos = self.listar()
        clientes = NCliente().listar()
        if cliente_id not in clientes.keys(): return "Cliente não encontrado"
        if preco_total < 0.0: return "Preço total inválido"

        novo_pedido = Pedido(len(pedidos) + 1, cliente_id, preco_total, data)
        nova_lista = []
        for pedido_id in pedidos:
            p = Pedido(
            pedidos[pedido_id]['id'],
            pedidos[pedido_id]['cliente_id'],
            pedidos[pedido_id]['preco_total'],
            pedidos[pedido_id]['data'],
            pedidos[pedido_id]['finalizado']
            )
            nova_lista.append(p)
        nova_lista.append(novo_pedido)

        self.grava_arquivo(nova_lista, 'pedidos.json')
        return {"message":"Pedido cadastrado com sucesso!", "id": novo_pedido.get_id()}
    
    def atualizar(self, pedido_id, preco_total):
        pedidos = self.listar()

        if pedido_id not in pedidos.keys(): return "pedido não encontrado"
 

        pedido_antigo = pedidos[pedido_id]

        pedidos[pedido_id]['preco_total'] = preco_total
        
        nova_lista = []
        for pedido_id in pedidos:
            p = pedido(
            pedidos[pedido_id]['id'],
            pedidos[pedido_id]['cliente_id'],
            pedidos[pedido_id]['preco_total'],
            pedidos[pedido_id]['data'],
            pedidos[pedido_id]['finalizado']
            )
            nova_lista.append(p)
        
        self.grava_arquivo(nova_lista, 'pedidos.json')
        return "Pedido atualizado com sucesso!"

    def fechar_pedido(self, pedido_id: str):
        pedidos = self.listar()
        
        if pedido_id not in pedidos.keys(): return "Pedido não encontrado."

        pedidos[pedido_id]['finalizado'] = True

        novos_pedidos = []
        for pedido in pedidos:
            p = pedido(
            pedidos[pedido_id]['id'],
            pedidos[pedido_id]['cliente_id'],
            pedidos[pedido_id]['preco_total'],
            pedidos[pedido_id]['data'],
            pedidos[pedido_id]['finalizado']
            )
            novos_pedidos.append(p)
        self.grava_arquivo(novos_pedidos, 'pedidos.json')
        return "Pedido fechado com sucesso!"

    def excluir(self, id):
        pedidos = self.listar()
        if len(pedidos) == 0: return "Lista vazia."
        del pedidos[id]
        nova_lista = []
        for pedido_id in pedidos:
            p = pedido(
            pedidos[pedido_id]['id'],
            pedidos[pedido_id]['cliente_id'],
            pedidos[pedido_id]['preco_total'],
            pedidos[pedido_id]['data'],
            pedidos[pedido_id]['finalizado']
            )
            nova_lista.append(p)
        
        self.grava_arquivo(nova_lista, 'pedidos.json')
        return "Pedido removido com sucesso!"
    
    @staticmethod
    def grava_arquivo(pedidos: list, arquivo: str):
        diretorio_atual = os.path.dirname(os.path.realpath(__file__))
        arquivo_nome = diretorio_atual +  f'\\base_dados\\{arquivo}' 
        dict_pedidos = {}
        for pedido in pedidos:
            key = pedido.get_id()
            dict_pedidos[key] = {
                "id": pedido.get_id(),
                "cliente_id": pedido.get_cliente_id(),
                "preco_total": pedido.get_preco_total(),
                "data": pedido.get_data(),
                "finalizado": pedido.is_finalizado()
            }
        
        objeto = json.dumps(dict_pedidos, indent = 4)
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
                    pedidos = json.loads(lista)
                else:
                    pedidos = {}
            return pedidos
        except Exception as e:
            return {}

