import os, json
from categoria import Categoria 

class NCategoria:
    def __init__(self):
        categorias = []
    
    def listar(self):
        return self.ler_arquivo('categorias.json')
    
    def ver(self, id):
        categorias = self.listar()
        for categoria_id in categorias:
            if categoria_id == id:
                return categorias[categoria_id]
    
    def cadastrar(self, descricao):
        categorias = self.listar()
        lista_categorias = list(categorias.values())
        
        if len(descricao) < 0 : return "Minimo de três caracteres para descrição."
        
        for categoria in lista_categorias: 
            if categoria['descricao'] == descricao: return "Descrição ja existe."
        categoria_id = len(lista_categorias) + 1

        nova_cat = Categoria(categoria_id, descricao)

        nova_lista = []
        for categoria in categorias:
            c = Categoria(categorias[categoria]['id'], categorias[categoria]['descricao'])
            nova_lista.append(c)
        nova_lista.append(nova_cat)
        self.grava_arquivo(nova_lista, 'categorias.json')
        return "Categoria cadastrada com sucesso!"
    
    def atualizar(self, categoria_id, descricao):
        categorias = self.listar()
        if categoria_id not in categorias.keys(): return "Categoria não encontrada"

        categoria_antigo = categorias[categoria_id]

        if descricao == '': descricao = categoria_antigo['descricao']
      
        categorias[categoria_id]['descricao'] = descricao
        
        
        nova_lista = []
        for categoria_id in categorias:
            c = Categoria(
            categorias[categoria_id]['id'],
            categorias[categoria_id]['descricao']
            )
            nova_lista.append(c)
        
        self.grava_arquivo(nova_lista, 'categorias.json')
        return "Categoria atualizada com sucesso!"
    
    def excluir(self):
        categorias = self.listar()

        del categorias[id]
        nova_lista = []
        for categoria_id in categorias:
            c = Categoria(
            categorias[categoria_id]['id'],
            categorias[categoria_id]['descricao']
            )
            nova_lista.append(c)
        
        self.grava_arquivo(nova_lista, 'categorias.json')
        return "categoria removido com sucesso!"
    
    @staticmethod
    def grava_arquivo(categorias: list, arquivo: str):
        diretorio_atual = os.path.dirname(os.path.realpath(__file__))
        arquivo_nome = diretorio_atual +  f'\\base_dados\\{arquivo}' 
        dict_categorias = {}
        for categoria in categorias:
            key = categoria.get_id()
            dict_categorias[key] = {
                "id": categoria.get_id(),
                "descricao": categoria.get_descricao()
            }
        
        objeto = json.dumps(dict_categorias, indent = 4)
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
                    categorias = json.loads(lista)
                else:
                    categorias = {}
            return categorias
        except Exception as e:
            return {}