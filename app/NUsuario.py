from usuario import Usuario

class NUsuario:
    def __init__(self):
        self._usuarios = []

    def listar(self):
        return self._usuarios 
    
    def ver_usuario(self, id):
        usuario = [user for user in self._usuarios if user.get_id() == id]
        return usuario
    
    def cadastrar(self, nome, email, senha):
        
        if '@' not in email: return {"message":"Formato de email inválido.", "status": "400"}
        
        email_ja_existe = [user for user in self._usuarios if user.get_email() == email]
        print(email_ja_existe)
        if email_ja_existe: return {"message":"Email já cadastrado.", "status": "400"}
        
        if len(nome) < 3  or len(senha) < 8: return {"message":"Mínimo de 3 caracteres para nome e 8 para senha", "status": "400"}
        
        id = 0
        for user in self._usuarios:
            id+=1
        usuario = Usuario(id, nome, email, senha)
        self._usuarios.append(usuario)
        return {"message": "Usuário cadastrado com sucesso!", "status": "201"}
    
    def atualizar(self):
        pass

    
    def excluir(self):
        # remover da lista
        pass

while True:
    nome = input("nome: ")
    email = input("email: ")
    senha = input("senha: ")
    usuario = NUsuario().cadastrar(nome, email, senha)
    print(usuario)