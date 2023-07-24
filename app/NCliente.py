import json
import os
from cliente import Cliente
from NUsuario import NUsuario
class NCliente:
    def __init__(self):
        self.clientes = self.ler_arquivo('cliente.json')
    
    def listar(self):
        return self.clientes
    
    def ver(self, id):
        for cliente in self.clientes:
            if cliente.get_id() == id:
                return cliente
        return None
    
    def cadastrar(self, nome, email, senha, cpf):
        clientes = self.listar()
        list_clientes = list(clientes.values())
        novos_clientes = []
        
        usuario = NUsuario().cadastrar(nome, email, senha)

        id_cliente = len(list_clientes) + 1
        novo_cliente = Cliente(id_cliente, usuario["data"]["usuario"].get_id(), cpf)
        for cliente in list_clientes:
            c = Cliente(cliente['id'], cliente['usuario_id'], cliente['cpf'])
            novos_clientes.append(c)
        novos_clientes.append(novo_cliente)

        self.grava_arquivo(novos_clientes, 'clientes.json')
        return {"data":{"message": "Cliente cadastrado com sucesso!", "cliente": novo_cliente}, "status": "201"}
    
    def atualizar(self, id, nome, email, senha, cpf):
        cliente = self.ver(id)
        if cliente:
            if nome:
                cliente.set_nome(nome)
            if email:
                cliente.set_email(email)
            if senha:
                cliente.set_senha(senha)
            if cpf:
                cliente.set_cpf(cpf)
            self.grava_arquivo(self.clientes, 'cliente.json')
            return {"message": "Cliente atualizado com sucesso!", "status": "200"}
        else:
            return {"message": "Cliente não encontrado.", "status": "400"}
    
    def excluir(self, id):
        cliente = self.ver(id)
        if cliente:
            self.clientes.remove(cliente)
            self.grava_arquivo(self.clientes, 'cliente.json')
            return {"message": "Cliente removido com sucesso!", "status": "200"}
        else:
            return {"message": "Cliente não encontrado.", "status": "400"}
    
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
n_cliente = NCliente()
while True:
    print("1 - Listar clientes")
    print("2 - Ver um cliente")
    print("3 - Cadastrar cliente")
    print("4 - Remover cliente")
    print("5 - Atualizar cliente")
    print("6 - Sair")
    opt = input("O que deseja fazer? ")
    
    if opt == '1':
        clientes = n_cliente.listar()
        for cliente in clientes:
            print(cliente)
    elif opt == '2':
        id = int(input("ID do cliente: "))
        cliente = n_cliente.ver(id)
        if cliente:
            print(cliente)
        else:
            print("Cliente não encontrado.")
    elif opt == '3':
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        cpf = input("CPF: ")
        resposta = n_cliente.cadastrar(nome, email, senha, cpf)
        print(resposta["data"])
    elif opt == '4':
        id = int(input("ID do cliente: "))
        resposta = n_cliente.excluir(id)
        print(resposta["data"])
    elif opt == '5':
        id = int(input("ID do cliente: "))
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        cpf = input("CPF: ")
        resposta = n_cliente.atualizar(id, nome, email, senha, cpf)
        print(resposta["data"])
    elif opt == '6':
        break
    else:
        print("Opção inválida. Tente novamente.")