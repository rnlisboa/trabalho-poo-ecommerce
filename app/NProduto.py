import os, json
from produto import Produto  
from NCategoria import NCategoria

class NProduto:
    def __init__(self):
        self._produtos = []
    
    def listar(self):
        return self.ler_arquivo('produtos.json')
    
    def ver(self, id):
        produtos = self.listar()
        for produto_id in produtos:
            if produto_id == id:
                return produtos[produto_id]
        
    
    def cadastrar(self, descricao: str, estoque: int, preco: float, categoria_id: str):
        categoria = NCategoria().ver(categoria_id)
        if not categoria: return "Categoria não encontrada"

        if len(descricao) < 0 : return "Minimo de três caracteres para descrição."
        if  estoque < 0 or preco < 0.0: return "estoque e preço devem ser maiores que zero"
        
        produtos = self.listar()
        id = len(produtos) + 1
        novo_produto = Produto(id, descricao, estoque, preco, categoria_id)

        nova_lista = []
        for produto_id in produtos:
            p = Produto(
            produtos[produto_id]['id'],
            produtos[produto_id]['descricao'],
            produtos[produto_id]['estoque'],
            produtos[produto_id]['preco'],
            produtos[produto_id]['categoria_id']
            )
            nova_lista.append(p)
        nova_lista.append(novo_produto)

        self.grava_arquivo(nova_lista, 'produtos.json')
        return "Produto cadastrado com sucesso!"

    
    def atualizar(self, produto_id, descricao: str, estoque: int, preco: float, categoria_id: int):
        produtos = self.listar()
        categoria = NCategoria().ver(categoria_id)
        if produto_id not in produtos.keys(): return "Produto não encontrado"
        if not categoria: return "Categoria não encontrada"

        produto_antigo = produtos[produto_id]

        if descricao == '': descricao = produto_antigo['descricao']
        if estoque == '': estoque = produto_antigo['estoque']
        if preco == '': preco = produto_antigo['preco']
        if categoria_id == '': categoria_id = categoria_id['preco']

        if  estoque < 0 or preco < 0.0: return "estoque e preço devem ser maiores que zero"
    
        produtos[produto_id]['descricao'] = descricao
        produtos[produto_id]['estoque'] = estoque
        produtos[produto_id]['preco'] = preco
        produtos[produto_id]['categoria_id'] = categoria_id
        
        nova_lista = []
        for produto_id in produtos:
            p = Produto(
            produtos[produto_id]['id'],
            produtos[produto_id]['descricao'],
            produtos[produto_id]['estoque'],
            produtos[produto_id]['preco'],
            produtos[produto_id]['categoria_id']
            )
            nova_lista.append(p)
        
        self.grava_arquivo(nova_lista, 'produtos.json')
        return "Produto atualizado com sucesso!"



    def excluir(self, id):
        produtos = self.listar()

        del produtos[id]
        nova_lista = []
        for produto_id in produtos:
            p = Produto(
            produtos[produto_id]['id'],
            produtos[produto_id]['descricao'],
            produtos[produto_id]['estoque'],
            produtos[produto_id]['preco'],
            produtos[produto_id]['categoria_id']
            )
            nova_lista.append(p)
        
        self.grava_arquivo(nova_lista, 'produtos.json')
        return "Produto removido com sucesso!"
        
    
    @staticmethod
    def grava_arquivo(produtos: list, arquivo: str):
        diretorio_atual = os.path.dirname(os.path.realpath(__file__))
        arquivo_nome = diretorio_atual +  f'\\base_dados\\{arquivo}' 
        dict_produtos = {}
        for produto in produtos:
            key = produto.get_id()
            dict_produtos[key] = {
                "id": produto.get_id(),
                "descricao": produto.get_descricao(),
                "estoque": produto.get_estoque(),
                "preco": produto.get_preco(),
                "categoria_id": produto.get_categoria_id()
            }
        
        objeto = json.dumps(dict_produtos, indent = 4)
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
                    produtos = json.loads(lista)
                else:
                    produtos = {}
            return produtos
        except Exception as e:
            return {}
