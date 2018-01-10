"""Cupom Fiscal"""

lista_produtos = []

pergunta = 'S'
while pergunta == 'S':
    produto = input("Produto: ")
    valor = int(input("Valor: "))
    lista_produtos.append({'descricao':produto, 'valor':valor})
    pergunta = input("Deseja continuar cadastrando? ")

total = 0
for produto in lista_produtos:
    total += produto['valor']
    print("Produto: %s | R$ %d" % (produto["descricao"], produto["valor"]))
    # print("Produto:", produto['descricao'],"|","R$",produto['valor'])

print('O total é: %d' % (total,))
#print(f'O total é: {total}')
