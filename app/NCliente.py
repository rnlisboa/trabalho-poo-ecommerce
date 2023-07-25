import json
import os
from cliente import Cliente
from NUsuario import NUsuario
class NCliente:
    def __init__(self):
        self.clientes = self.ler_arquivo('clientes.json')
    
    def listar(self):
        return self.clientes
    
    def ver(self, id):
        clientes = list(self.listar().values())
        for cliente in clientes:
            if cliente['id'] == int(id):
                return cliente
        return None
    
    def cadastrar(self, nome, email, senha, cpf):
        resposta_usuario = NUsuario().cadastrar(nome, email, senha)
        
        
        usuario_id = resposta_usuario['usuario_id'] if 'usuario_id' in resposta_usuario else None
        if not usuario_id: return resposta_usuario
        
        clientes = self.listar()
        lista_clientes = list(clientes.values())
      
        cliente_id = len(lista_clientes) + 1
        novo_cliente = Cliente(cliente_id, usuario_id, cpf)
        nova_lista_clientes = []

        for cliente in lista_clientes:
            cliente = Cliente(cliente['id'], cliente['usuario'], cliente['cpf'])
            nova_lista_clientes.append(cliente)
  
        nova_lista_clientes.append(novo_cliente)
        
        self.grava_arquivo(nova_lista_clientes, "clientes.json")
        return "Cadastro realizado"
        
    
    def atualizar(self, id, nome, email, senha, cpf):
        clientes = self.listar()
        clientes_id = clientes.keys()
        if not id in clientes_id:
            return "Você não possui conta cliente."
        
        resposta_usuario = NUsuario().atualizar(id, nome, email, senha)
        if resposta_usuario["status"] == 400:
            return resposta_usuario["message"]

        lista_clientes = list(clientes.values())
        for cliente in lista_clientes:
            if cliente['id'] == int(id):
                cliente['cpf'] = cpf
        for i in list_usuarios:
            c = Cliente(i['id'], i['usuario'], i['cpf'])
        
        self.grava_arquivo(novos_clientes, 'clientes.json')
        return "Cliente atualizado com sucesso!"

    def excluir(self, id):
        clientes = self.listar()
        clientes_id = clientes.keys()
        if not id in clientes_id:
            return "Você não possui conta cliente."
        
        try:
            for cliente_id in clientes:
                if clientes[cliente_id]['id'] == int(id):
                    resposta_usuario = NUsuario().excluir(clientes[cliente_id]['usuario'])
            lista_clientes = list(self.listar().values())
            
            novos_clientes = [] 
            for cliente_a_remover in lista_clientes:
                if cliente_a_remover['id'] == int(id):
                    lista_clientes.remove(cliente_a_remover)
                    break
            for i in lista_clientes:
                c = Cliente(i['id'], i['usuario'], i['cpf'])
                novos_clientes.append(c)
            self.grava_arquivo(novos_clientes, 'clientes.json')
            
            return "Cliente removido com sucesso!"
        except: return "Erro ao remover cliente."    
        
    
    @staticmethod
    def grava_arquivo(clientes: list, arquivo: str):
        diretorio_atual = os.path.dirname(os.path.realpath(__file__))
        arquivo_nome = diretorio_atual + f'\\base_dados\\{arquivo}'
        dict_clientes = {}
        for cliente in clientes:
            key = cliente.get_id()
            dict_clientes[key] = {
                "id": cliente.get_id(),
                "usuario": cliente.get_usuario(),
                "cpf": cliente.get_cpf()
            }
        
        objeto = json.dumps(dict_clientes, indent=4)
        with open(arquivo_nome, 'w', encoding='utf-8') as f:
            f.write(objeto)

    @staticmethod
    def ler_arquivo(arquivo):
        diretorio_atual = os.path.dirname(os.path.realpath(__file__))
        arquivo_nome = diretorio_atual + f'\\base_dados\\{arquivo}'
        try:
            with open(arquivo_nome, 'r', encoding='utf-8') as f:
                lista = f.read()
                if lista != '':
                    clientes = json.loads(lista)
                else:
                    clientes = {}
            return clientes
        except:
            return {}

