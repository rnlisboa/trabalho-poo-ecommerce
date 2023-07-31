import os, json
from datetime import datetime
from NPedido import NPedido
from NCategoria import NCategoria
from NPedidoItem import NPedidoItem
from NProduto import NProduto
from NCliente import NCliente
from NUsuario import NUsuario

class Ecommerce:
    def __init__(self):
        self.usuario_logado = False
        self.is_admin = True
        self.usuario_id = ''

    def menu(self):
        while True:
            self.is_logged()
            self.is_user_admin()  

            print("""
            +--------------------------+
            | Bem vindo ao PyCommerce! |
            +--------------------------+
            
            """)

            if self.usuario_logado and self.is_admin:
                print("""
                +-------------+
                | MENU ADMIN! |
                +-------------+
                
                """)
                opcao = self.menu_admin()
                try:
                    
                    if opcao == 1:
                        num = int(input("Escolha uma ação: "))
                        if num == 1: self.listar_categorias()
                            
                        if num == 2: self.criar_categoria()
                        
                        if num == 3: self.atualizar_categoria()
                            
                        if num == 4: self.remover_categoria()
                            

                    if opcao == 2:        
                        num = int(input("Escolha uma ação: "))
                        if num == 1: self.listar_produtos()
                            
                        if num == 2: self.ver_produto()

                        if num == 3: self.criar_produto()
                    
                        if num == 4: self.atualizar_produto()
                    
                        if num == 5: self.remover_produto()

                    if opcao == 3: 
                        self.sair()
                        self.usuario_logado = False
                    
                    if opcao == 4: break
                        
                except ValueError:
                        print("Apenas números.")
                

            if not self.usuario_logado:
                print("""
                +-----------------+
                | MENU VISITANTE! |
                +-----------------+
                
                """)
                opcao = self.menu_visitante()
                try:
                    
                    if opcao == 1:
                        try:
                            num = int(input("Escolha uma ação:"))
                            if num == 1: self.listar_categorias()
                        except ValueError:
                            print("Apenas números.")

                    if opcao == 2:
                        try:
                            num = int(input("Escolha uma ação: "))
                            if num == 1: self.listar_produtos()
                            if num == 2: self.ver_produtos_categoria()
                        except ValueError:
                            print("Apenas números.")

                    if opcao == 3: self.cadastrar_usuario()
                    
                    if opcao == 4: self.login()

                    if opcao == 5: break

                except ValueError:
                    print("Apenas números.")
            
            if self.usuario_logado and not self.is_admin:
                print("""
                +-----------------+
                | MENU CLIENTE!   |
                +-----------------+
                
                """)
                opcao = self.menu_usuario()
                try:
                        
                        if opcao == 1:
                            num = int(input("Escolha uma ação: ")) 
                            if num == 1: self.listar_categorias()

                        if opcao == 2:
                            num = int(input("Escolha uma ação: ")) 
                            if num == 1: self.listar_produtos()
                            if num == 2: self.ver_produtos_categoria()
                            s_n = int(input("Deseja ver detalhes de um produto?  1- SIM | 2- NÃO "))
                            if s_n == 1:
                                self.ver_produto()
                                a_n = int(input("Deseja adicionar produto ao carrinho?  1- SIM | 2- NÃO "))
                                if a_n == 1: self.criar_pedido_items()
                        if opcao == 3: 
                            self.menu_conta()
                            try:
                                num = int(input("Escolha uma ação: ")) 
                                opt = int(input("O que deseja fazer? "))
                                if num == 1: self.atualizar_usuario()
                                if num == 2: self.remover_conta()
                            except ValueError:
                                print("Apenas números.")

                        if opcao == 4: 
                            self.menu_carrinho()
                            self.listar_pedidos()
                            num = int(input("Escolha uma ação: ")) 
                            if num == 1:
                                
                                opc = self.menu_pedido()
                                if opc == 1: self.remover_pedido()
                                if opc == 2: self.realizar_compra()
                                if opc == 3: self.ver_pedido_items()

                        if opcao == 5: 
                            self.sair()
                            self.usuario_logado = False
                        
                        if opcao == 6: break
                except ValueError:
                        print("Apenas números.")
    def menu_admin(self):
        print("""
        +------------------+
        |   1- CATEGORIAS  |
        +------------------+
        |   2- PRODUTOS    |
        +------------------+
        |   3- SAIR        |
        +------------------+
        |   4- ENCERRAR    |
        +------------------+

        """)   
        try:
            opcao = int(input("O que deseja gerenciar/fazer? "))
            if opcao not in [1, 2, 3, 4]: return "Opção não consta."
            if opcao == 1:
                print("""
                +------------------+
                |    CATEGORIAS    |
                +------------------+
                |   1-  LISTAR     |
                |   2- CADASTRAR   |
                |   3- ATUALIZAR   |
                |   4-  EXCLUIR    |
                +------------------+
                """)
                
            if opcao == 2:
                print("""
                +------------------+
                |    PRODUTOS      |
                +------------------+
                |   01-  LISTAR    |
                |   02-   VER      |
                |   03- CADASTRAR  |
                |   04- ATUALIZAR  |
                |   05-  EXCLUIR   |
                +------------------+
                """)
            
            return opcao
        
        except ValueError:
            return "Apenas números."
    
    def menu_visitante(self):
        print("""
        +------------------+
        |   1- CATEGORIAS  |
        +------------------+
        |   2- PRODUTOS    |
        +------------------+
        |   3- CRIAR CONTA |
        +------------------+
        |   4- LOGIN       |
        +------------------+
        |   5- ENCERRAR    |
        +------------------+
        """) 
        try:
            opcao = int(input("O que deseja ver/fazer? "))
            if opcao not in [1, 2, 3, 4, 5]: return "Opção não consta."
            if opcao == 1:
                print("""
                +------------------+
                |    CATEGORIAS    |
                +------------------+
                |   1-  LISTAR     |
                +------------------+
                """)
            if opcao == 2:
                print("""
                +------------------+
                |    PRODUTOS      |
                +------------------+
                |   01- LISTAR     |
                |       TODOS      |
                +------------------+
                |   02- LISTAR     |
                |  POR CATEGORIA   |
                +------------------+
                
                """)
            if opcao == 3:
                print("""
                +--------------------------+
                |    PÁGINA DE CADASTRO    |
                +--------------------------+
                """)
            if opcao == 4:
                print("""
                +------------------------+
                |    PÁGINA DE LOGIN     |
                +------------------------+
                """)
            return opcao
        except ValueError:
            return "Apenas números."
    
    def menu_usuario(self):
        print("""
        +------------------+
        |   1- CATEGORIAS  |
        +------------------+
        |   2- PRODUTOS    |
        +------------------+
        |   3- CONTA       |
        +------------------+
        |   4- CARRINHO    |
        +------------------+
        |   5- SAIR        |
        +------------------+
        |   6- ENCERRAR    |
        +------------------+
        """)
        try:
            opcao = int(input("O que deseja ver? "))
            if opcao not in [1, 2, 3, 4,5,6]: return "Opção não consta."
            if opcao == 1:
                print("""
                +------------------+
                |    CATEGORIAS    |
                +------------------+
                |   1-  LISTAR     |
                +------------------+
                """)
            if opcao == 2:
                print("""
                
                +------------------+
                |    PRODUTOS      |
                +------------------+
                |   01- LISTAR     |
                |       TODOS      |
                +------------------+
                |   02- LISTAR     |
                |  POR CATEGORIA   |
                +------------------+

                """)
            if opcao == 3:
                print("""
                +-------------------------+
                |  ADMNISTRAÇÃO DA CONTA  |
                +-------------------------+
                """)
            if opcao == 4:
                print("""
                +------------------+
                |     CARRINHO     |
                +------------------+              
                """)
            return opcao
        except ValueError:
            return "Apenas números."

    def menu_carrinho(self):
        print("""
        +------------------+
        |   1- VER PEDIDO  |
        +------------------+
        """)
    
    def menu_pedido(self):
        print("""
        +------------------+
        |   1- REMOVER     |
        |      PEDIDO      |
        +------------------+
        |  2- REALIZAR     |
        |      COMPRA      |
        +------------------+
        |  3- VER          |
        |    DETALHES      |
        +------------------+
        """)
        try:
            p_opcoes = int(input("Escolha uma opção: \n"))
            return p_opcoes
        except ValueError:
            return "Apenas números."
    
    def menu_conta(self):
        print("""
        +-----------------------+
        |   1- ATUALIZAR CONTA  |
        +-----------------------+
        |   2- REMOVER CONTA    |
        +-----------------------+ 
        """)
    
    def listar_categorias(self):
        categorias = NCategoria().listar()
        if len(categorias) == 0: 
            print("Sem categorias.")
        else:
            for categoria_id in categorias:
                print(f"id:{categorias[categoria_id]['id']} - descrição: {categorias[categoria_id]['descricao']}")

    def criar_categoria(self):
        desc = input("Informe a descição: ")
        cad = NCategoria().cadastrar(desc)
        print(cad)

    def atualizar_categoria(self):
        self.listar_categorias()
        id_c = input("Informe o id da categoria: ")
        desc = input("Informe a descrição: ")
        cad = NCategoria().atualizar(id_c, desc)
        print(cad)

    def remover_categoria(self):
        self.listar_categorias()
        id_c = input("Informe o id da categoria: ")
        cad = NCategoria().excluir(id_c)
        print(cad)
    
    def listar_produtos(self):
        produtos = NProduto().listar()
        
        for id_p in produtos:
            print(f"id: {id_p}")
            print(f"descrição: {produtos[id_p]['descricao']}")
            print(f"estoque: {produtos[id_p]['estoque']}")
            print(f"preço: {produtos[id_p]['preco']}")
            print('----------------------------')
    
    def ver_produto(self):
        id_p = input("Informe o id do produto que deseja ver: ")
        produto = NProduto().ver(id_p)
        if produto:
            print(f"id: {id_p}")
            print(f"descrição: {produto['descricao']}")
            print(f"estoque: {produto['estoque']}")
            print(f"preço: {produto['preco']}")
        else:
            print("Não encontrado.")
                                
    def ver_produtos_categoria(self):
        self.listar_categorias()
        id_c = input("Informe o id da categoria: ")
        produtos = NProduto().listar()
        p_por_c = [produto for produto in produtos if produtos[produto]['categoria_id'] == id_c]
        for prod in p_por_c:
            print(f"id: {prod}")
            print(f"descrição: {prod['descrição']}")
            print(f"estoque: {prod['estoque']}")
            print(f"preço: {prod['preco']}")

    def criar_produto(self):
        d = input("Descrição: ")
        e = int(input("Estoque: "))
        p = float(input("Preço: "))
        print("Id da categoria: ")
        print("Categorias: ")
        self.listar_categorias()
        c = input("Qual categoria? ")
        prod = NProduto().cadastrar(d, e, p, c)
        print(prod)

    def atualizar_produto(self):
        self.listar_produtos()
        id = input("Id do produto: ")
        d = input("Descrição: ")
        e = int(input("Estoque: "))
        p = float(input("Preço: "))
        print("Id da categoria: ")
        print("Categorias: ")
        self.listar_categorias()
        c = input("Qual categoria? ")
        prod = NProduto().atualizar(id, d, e, p, c)
        print(prod)
    
    def remover_produto(self):
        self.listar_produtos()
        id = input("Id do produto: ")
        prod = NProduto().excluir(id)
        print(prod)
    
    def listar_pedidos(self):
        pedidos = NPedido().listar()
        session = self.ler_arquivo('session.json')
        meus = [p for p in pedidos if pedidos[p]['cliente_id'] == session['client']]
    
        if len(meus) == 0: 
            print("Carrinho vazio.")
        else:
            for p in meus:
                pedido = NPedido().ver(p)
                if not pedido['finalizado']:
                    print(f"""+------------------------------------------------------------------------------+
                        | id: {pedido['id']} - preço total: {pedido['preco_total']} - data: {pedido['data']}   |
                        +------------------------------------------------------------------------------+""")
        
    def remover_pedido(self):
        id = input("Informe o id: ")
        p = NPedido().excluir(id)
        print(p)
    
    def criar_pedido(self):
        pass
    
    def realizar_compra(self):
        id = input("Informe o id: ")
        p = NPedido().fechar_pedido(id)
        print(p)
    
    def criar_pedido_items(self):
        data_hora_atual = datetime.now()
        data = data_hora_atual.strftime("%d/%m/%Y %H:%M")
        session = self.ler_arquivo('session.json')
        id_p = input("Informe novamente o id do produto: ")
        qtd = int(input("Informe a quantidade: "))

        produto = NProduto().ver(id_p)
        preco_total = produto['preco'] * qtd

        pedido = NPedido().cadastrar(session['client'], preco_total, data)
   
        if 'id' in pedido.keys():
            item = NPedidoItem().cadastrar(id_p, pedido['id'], qtd)
            print(f"MENSAGEM DE ITEM: {item}")
        else:
            print(F"MENSAGEM DE PRODUTO: {pedido}")
    
    def atualizar_pedido_items(self):
        pass
    
    def remover_pedido_items(self):
        pass
    
    def ver_pedido_items(self):
        d = int(input("Informe o id do pedido: "))
        items = NPedidoItem().listar()
        meus = [item for item in items if items[item]['pedido_id'] == d]
        print(meus)
        for m in meus:
            p = NProduto().ver(m)
            print(f"""
            Produto: {p['descricao']} - Quantidade: {meus[p]['quantidade']} Preço total: {meus[p]['preco_total']}
            """)
    
    def listar_pedido_items(self):
        pass
    
    def listar_usuarios(self):
        usuarios = NUsuarios().listar()
        for u in usuarios:
            print(f"id: {usuarios[u]['id']} - nome: {usuarios[u]['nome']}")

    def remover_conta(self):
        id = input("Id: ")
        u = NCliente().excluir(id)
        print(u)

    def atualizar_usuario(self):
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        cpf = input("CPF: ")
        idd = input("Id: ")
        u = NCliente().atualizar(idd, nome, email, senha, cpf)
        print(u)

    def cadastrar_usuario(self):
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        cpf = input("CPF: ")

        u = NCliente().cadastrar(nome, email, senha, cpf)
        print(u)
    
    def login(self):
        email = input("Digite o email: ")
        senha = input("Digite a senha: ")
        usuarios = NUsuario().listar()
        clientes = NCliente().listar()
        user = [u for u in usuarios if usuarios[u]['email'] == email]
         
        if len(user) > 0:
            u = NUsuario().ver_usuario(user[0])
            client = [c for c in clientes if clientes[c]['usuario'] == u['data']['id']]
           
            if email == u['data']['email'] and senha == u['data']['senha']:
                self.grava_arquivo(u['data']['id'],u['data']['is_admin'],client[0])
                self.usuario_logado = True
                print("""
                
                LOGIN REALIZADO COM SUCESSO!
                
                """)
            else:
                print("Dados inválidos.")
    def is_logged(self):
        session = self.ler_arquivo('session.json')
        if 'id' in session.keys() and session['id'] != '':

            self.usuario_logado = True 
        else:
            self.usuario_logado = False
    
    def is_user_admin(self):
        session = self.ler_arquivo('session.json')
        if 'is_admin' in session.keys():
            if session['id'] != '':
                self.is_admin = session['is_admin']
    
    def set_user_id(self):
        session = self.ler_arquivo('session.json')
        self.usuario_id = session['user_id']

    def sair(self):
        self.grava_arquivo()
        self.usuario_logado = False
    
    @staticmethod
    def grava_arquivo(id='', is_admin='', client=''):
        diretorio_atual = os.path.dirname(os.path.realpath(__file__))
        arquivo_nome = diretorio_atual +  f'\\base_dados\\session.json' 
        dict_u = {"id": id, "is_admin": is_admin, "client": client}
        
        objeto = json.dumps(dict_u, indent = 4)
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

Ecommerce().menu()