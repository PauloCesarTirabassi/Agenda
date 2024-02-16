class Contato:

    def __init__(self, nome, idade, telefone, email, endereco, celular, ativo: bool, id):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.ativo = ativo
        self.celular = celular
        self.idade = idade
        self.id = id

    def ativar(self):
        self.ativo = True

    def desativar(self):
        self.ativo = False

    def console(self):
        if self.ativo:
            print(self.nome, "Este contato esta ativo!")
        else:
            print(self.nome, "Este contato esta inativo!")
