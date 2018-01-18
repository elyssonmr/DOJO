"""Cupom Fiscal"""

# Exemplo "f string"
# f"alguma coisa {variaval_no_context}"
#           10        20        31
# 0123456789012345678901234567890
# ###############################

# 1  |Pão de Sal| R$ 1,00    #

def imprimir_linha_cerquilha():
    print('#'*31)

def imprimir_item(item_lista,indice):
    indice_formatado = '%3d' % (indice,)
    produto_formatado = '%10s' % (item_lista["descricao"],)
    valor_formatado = ' R$ %5.2f' % (item_lista["valor"],)

    print("#", "|".join([indice_formatado, produto_formatado, valor_formatado]), "#")

def cabecalho():
    
    imprimir_linha_cerquilha()
    print('# Sistema de Venda Sr. José   #')
    print('# Data Compra: 18/01/2018     #')
    print('#')

def rodape():
    print('#=============================#')
    print('# Obrigado Volte Sempre       #')
    print('# Venda Sr. José agradece     #')
    print('#=============================#')
    print('# DOJO Interprises SA         #')
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
    {"descricao": "Pasta de dente", "valor": 10}
]
total = 0

cabecalho()

for indice, produto in enumerate(lista_produtos):
    total += produto['valor']
    # print("Produto: %s | R$ %d" % (produto["descricao"], produto["valor"]))
    # print("Produto:", produto['descricao'],"|","R$",produto['valor'])
    
    imprimir_item(produto, indice+1)

print('O total é: %d' % (total,))
#print(f'O total é: {total}')

rodape()
