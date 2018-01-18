"""Cupom Fiscal"""

from datetime import date

# Exemplo "f string"
# f"alguma coisa {variaval_no_context}"
#           10        20        31
# 0123456789012345678901234567890
# ###############################

# 1  |Pão de Sal| R$ 1,00    #

def imprimir_linha_cerquilha():
    print('#'*35)

def imprimir_separador_sessao():
    print('#=================================#')

def imprimir_cabecalho():
    imprimir_linha_cerquilha()
    print(f'# Sistema de Venda Sr. José       #')
    hoje = date.today()
    print(f'# Data Compra: {hoje.strftime("%d/%m/%Y"):<18.18} #')
    # print('# Data Compra: 18/01/2018         #')
    imprimir_separador_sessao()

def imprimir_produtos(produtos):
    print('# Produtos Comprados:             #')
    print('# Nº Item |   Nome   |   Valor    #')
    total = 0.0

    for indice, produto in enumerate(lista_produtos):
        total += produto['valor']
        imprimir_item(produto, indice + 1)

    imprimir_separador_sessao()
    print(f'# Total:               R$ {total:> 7.2f} #')
    imprimir_separador_sessao()

def imprimir_item(item_lista,indice):
    # indice_formatado = '%3d' % (indice,)
    # produto_formatado = '%10s' % (item_lista["descricao"],)
    # valor_formatado = ' R$ %5.2f' % (item_lista["valor"],)

    print(f'# {indice:<8}|{item_lista["descricao"]:^10.10}| R$ {item_lista["valor"]:>7.2f} #')
    # print("#", "|".join([indice_formatado, produto_formatado, valor_formatado]), "#")

def imprimir_rodape():
    print('# Obrigado Volte Sempre           #')
    print('# Venda Sr. José agradece         #')
    imprimir_separador_sessao()
    print('# DOJO Interprises SA             #')
    imprimir_linha_cerquilha()

lista_produtos = []

pergunta = 'S'
#while pergunta == 'S':
    #produto = input("Produto: ")
    #valor = float(input("Valor: "))
    #lista_produtos.append({'descricao':produto, 'valor':valor})
    #pergunta = input("Deseja continuar cadastrando? ")
lista_produtos = [
    {"descricao": "Nutela", "valor": 8.00},
    {"descricao": "Trident", "valor": 3.50},
    {"descricao": "Pasta de dente", "valor": 10.00},
]

imprimir_cabecalho()
imprimir_produtos(lista_produtos)
imprimir_rodape()
