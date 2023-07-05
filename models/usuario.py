class Usuario(object):
 
    def __init__(self,id, nome, email, senha, is_admin=False):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__is_admin = is_admin
 
    def get_id(self):
        return self.__id
 
    def get_nome(self):
        return self.__nome
    
    def get_email(self):
        return self.__email
 
    def get_senha(self):
        return self.__senha
 
    def get_is_admin(self):
        return self.__is_admin
 
    
    def set_id(self, id):
        if id > 0:
            self.__id = id
 
    def set_nome(self, nome):
        if nome!= '':
            self.__nome = nome
 
    def set_email(self, email):
        if email != '':
            self.__email = email
 
    def set_senha(self, senha):
        if senha != '':
            self.__senha = senha
    
    def set_is_admin(self, is_admin):
        self.__is_admin = is_admin
    
    id = property(fget=get_id, fset=set_id)
    nome = property(fget=get_nome, fset=set_nome)
    email = property(fget=get_email, fset=set_email)
    senha = property(fget=get_senha, fset=set_senha)
    is_admin = property(fget=get_is_admin, fset=set_is_admin)

usuario = Usuario(1, 'user', 'user@gmail.com', "12354")
 
print(usuario.id)