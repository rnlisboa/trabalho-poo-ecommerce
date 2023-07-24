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
        resposta_usuario = NUsuario().cadastrar(id, nome, email, senha)
        return resposta_usuario
    
    def excluir(self, id):
        resposta_usuario = NUsuario().cadastrar(id)
        return resposta_usuario
    
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
n_cliente = NCliente().ver(2)
print(n_cliente)
# while True:
#     print("1 - Listar clientes")
#     print("2 - Ver um cliente")
#     print("3 - Cadastrar cliente")
#     print("4 - Remover cliente")
#     print("5 - Atualizar cliente")
#     print("6 - Sair")
#     opt = input("O que deseja fazer? ")
    
#     if opt == '1':
#         clientes = n_cliente.listar()
#         for cliente in clientes:
#             print(cliente)
#     elif opt == '2':
#         id = int(input("ID do cliente: "))
#         cliente = n_cliente.ver(id)
#         if cliente:
#             print(cliente)
#         else:
#             print("Cliente não encontrado.")
#     elif opt == '3':
#         nome = input("Nome: ")
#         email = input("Email: ")
#         senha = input("Senha: ")
#         cpf = input("CPF: ")
#         resposta = n_cliente.cadastrar(nome, email, senha, cpf)
#         print(resposta)
#     elif opt == '4':
#         id = int(input("ID do cliente: "))
#         resposta = n_cliente.excluir(id)
#         print(resposta)
#     elif opt == '5':
#         id = int(input("ID do cliente: "))
#         nome = input("Nome: ")
#         email = input("Email: ")
#         senha = input("Senha: ")
#         cpf = input("CPF: ")
#         resposta = n_cliente.atualizar(id, nome, email, senha, cpf)
#         print(resposta)
#     elif opt == '6':
#         break
#     else:
#         print("Opção inválida. Tente novamente.")