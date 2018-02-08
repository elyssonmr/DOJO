"""Cupom Fiscal"""

from datetime import date

# Exemplo "f string"
# f"alguma coisa {variaval_no_context}"
#           10        20        31
# 0123456789012345678901234567890
# ###############################

# 1  |Pão de Sal| R$ 1,00    #

class CLIController:
    def __init__(self):
        self._output = open("cupom_fiscal.txt", "w")
    
    def _writeln(self, text):
        self._output.write(text + '\n')



def writeln(text = 'DOJO', arq='arquivo'):
    arq.write(text + '\n')

def imprimir_linha_cerquilha():
    return '#'*35

def imprimir_separador_sessao():
    return '#=================================#'

def imprimir_cabecalho():
    writeln(imprimir_linha_cerquilha())
    writeln(f'# Sistema de Venda Sr. José       #')
    hoje = date.today()
    writeln(f'# Data Compra: {hoje.strftime("%d/%m/%Y"):<18.18} #')
    # print('# Data Compra: 18/01/2018         #')
    writeln(imprimir_separador_sessao())
    return True

def imprimir_produtos(produtos):
    writeln('# Produtos Comprados:             #')
    writeln('# Nº Item |   Nome   |   Valor    #')
    total = 0.0

    for indice, produto in enumerate(lista_produtos):
        total += produto['valor']
        imprimir_item(produto, indice + 1)

    writeln(imprimir_separador_sessao())
    writeln(f'# Total:               R$ {total:> 7.2f} #')
    writeln(imprimir_separador_sessao())

def imprimir_item(item_lista, indice):
    # indice_formatado = '%3d' % (indice,)
    # produto_formatado = '%10s' % (item_lista["descricao"],)
    # valor_formatado = ' R$ %5.2f' % (item_lista["valor"],)

    writeln(f'# {indice:<8}|{item_lista["descricao"]:^10.10}| R$ {item_lista["valor"]:>7.2f} #')
    # print("#", "|".join([indice_formatado, produto_formatado, valor_formatado]), "#")

def imprimir_rodape():
    writeln('# Obrigado Volte Sempre           #')
    writeln('# Venda Sr. José agradece         #')
    writeln(imprimir_separador_sessao()          )
    writeln('# DOJO Interprises SA             #')
    writeln(imprimir_linha_cerquilha()           )  

lista_produtos = []

pergunta = 'S'
#while pergunta == 'S':
    #produto = input("Produto: ")
    #valor = float(input("Valor: "))
    #lista_produtos.append({'descricao':produto, 'valor':valor})
    #pergunta = input("Deseja continuar cadastrando? ")
lista_produtos = [
    {"descricao": "Nutela", "valor": 15.00},
    {"descricao": "Trident", "valor": 3.50},
    {"descricao": "Pasta de dente", "valor": 10.00},
]


if __name__ == "__main__":
    arquivo = open('nota.txt', 'w')
    imprimir_cabecalho()
    imprimir_produtos(lista_produtos)
    imprimir_rodape()

    #writeln()
    arquivo.close()

"""
#teste de print em arquivo
arquivo2 = open('nota2.txt','w')
import sys
sys.stdout = arquivo2
print('teste')
arquivo2.close()
"""
