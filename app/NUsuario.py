import json
import os
from usuario import Usuario

class NUsuario:
    def __init__(self):
        self._usuarios = []

    def listar(self):
        
        return self.ler_arquivo('usuarios.json') 
    
    def ver_usuario(self, id):
        usuarios = self.ler_arquivo('usuarios.json')
        list_usuarios = list(usuarios.values())
        usuario = [user for user in list_usuarios if user['id'] == int(id)]
        try:
            user = usuario[0]
            return {"data":user, "status": "400"}
        except:
            return {"message":"Usuário não encontrado.", "status": "400"}
    
    def cadastrar(self, nome, email, senha):
        usuarios = self.ler_arquivo('usuarios.json')
        list_usuarios = list(usuarios.values())

        if '@' not in email: return {"message":"Formato de email inválido.", "status": "400"}
        email_ja_existe = [user for user in list_usuarios if user['email'] == email]
        
        if len(email_ja_existe) > 0: return {"message":"Email já cadastrado.", "status": "400"}
        
        if len(nome) < 3  or len(senha) < 8: return {"message":"Mínimo de 3 caracteres para nome e 8 para senha", "status": "400"}
        
        id =  len(list_usuarios) + 1
        usuario = Usuario(id, nome, email, senha)
        
        novos_usuarios = []
        for i in list_usuarios:
            u = Usuario(i['id'], i['nome'], i['email'], i['senha'])
            novos_usuarios.append(u)
        novos_usuarios.append(usuario)

        self.grava_arquivo(novos_usuarios, 'usuarios.json')
        return {"message": "Usuário cadastrado com sucesso!", "status": "201"}
    
    def atualizar(self, id, nome, email, senha):
        usuario = self.ver_usuario(id)['data']
        usuarios = self.ler_arquivo('usuarios.json')
        list_usuarios = list(usuarios.values())
       
        if senha != '':
            if len(senha) < 8: return {"message":"Mínimo de 8 para senha", "status": "400"}
        if senha == '':
            senha = usuario['senha'] 

        if email != '':
            if '@' not in email: return {"message":"Formato de email inválido.", "status": "400"}
            email_ja_existe = [user for user in list_usuarios if user['email'] == email]
            if len(email_ja_existe) > 0: 
                return {"message":"Email já cadastrado.", "status": "400"}
        if email == '':
            email = usuario['email']
        
        if nome != '':
            if len(nome) < 3:
                return {"message":"Mínimo de 3 caracteres para nome", "status": "400"}
        if nome == '':
            nome = usuario['nome']
        
        usuario_atualizado = Usuario(id, nome, email, senha)
        
        novos_usuarios = []
        for usuario_a_atualizar in list_usuarios:
            if usuario_a_atualizar['id'] == int(id):
                print(usuario_a_atualizar['id'])
                list_usuarios.remove(usuario_a_atualizar)
                break
       
        for i in list_usuarios:
            u = Usuario(i['id'], i['nome'], i['email'], i['senha'])
            novos_usuarios.append(u)
        novos_usuarios.append(usuario_atualizado)
        print(novos_usuarios)
        self.grava_arquivo(novos_usuarios, 'usuarios.json')
        return {"message": "Usuário atualizado com sucesso!", "status": "200"}

    def excluir(self, id):
        usuarios = self.listar()
        list_usuarios = list(usuarios.values())
        
        novos_usuarios = []
        for usuario_a_remover in list_usuarios:
            if usuario_a_remover['id'] == int(id):
                list_usuarios.remove(usuario_a_remover)
                break
        for i in list_usuarios:
            u = Usuario(i['id'], i['nome'], i['email'], i['senha'])
            novos_usuarios.append(u)

        
        self.grava_arquivo(novos_usuarios, 'usuarios.json')
        return {"message": "Usuário removido com sucesso!", "status": "200"}
    
    @staticmethod
    def grava_arquivo(usuarios: list, arquivo: str):
        diretorio_atual = os.path.dirname(os.path.realpath(__file__))
        arquivo_nome = diretorio_atual +  f'\\base_dados\\{arquivo}' 
        dict_usuarios = {}
        for usuario in usuarios:
            key = usuario.get_id()
            dict_usuarios[key] = {
                "id": usuario.get_id(),
                "nome": usuario.get_nome(),
                "email": usuario.get_email(),
                "senha": usuario.get_senha(),
                "is_admin": usuario.get_is_admin()
            }
        
        objeto = json.dumps(dict_usuarios, indent = 4)
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
                    usuarios = json.loads(lista)
                else:
                    usuarios = {}
            return usuarios
        except:
            return {}
