class ValidadorCPF():
    def __init__(self, cpf):
        self.cpf = cpf

    def validar_digitos(self):
        valido = False
        if len(self.cpf) == 11:
            valido = True

        return valido
