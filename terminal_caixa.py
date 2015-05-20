import unittest

class Terminal(object):
    
    def sacar(self, valor_saque):
        notas = []
        
        notas_cem = valor_saque / 100
        
        if notas_cem > 0:
            notas.append('%d nota de 100R$' % notas_cem)
            valor_saque = valor_saque % 100
        
        notas_cinq = valor_saque / 50
        
        if notas_cinq > 0:
            notas.append('%d nota de 50R$' % notas_cinq)
            valor_saque = valor_saque % 50
        
        notas_vin = valor_saque / 20
        
        if notas_vin > 0:
            notas.append('%d nota de 20R$' % notas_vin)
            valor_saque = valor_saque % 20
            
        notas_dez = valor_saque / 10
        
        if notas_dez > 0:
            notas.append('%d nota de 10R$' % notas_dez)
            valor_saque = valor_saque % 10
        
        if valor_saque == 0:
            return ' '.join(notas)
        else:
            raise Exception('Nao Ha notas para representar este valor')
    

class TerminalTest(unittest.TestCase):
    def setUp(self):
        self.caixa = Terminal()
        
    def test_saque_10_reais(self):
        esperado = '1 nota de 10R$'
        resposta = self.caixa.sacar(10)
        
        self.assertEqual(esperado, resposta)
    
    def test_saque_20_reais(self):
        esperado = '1 nota de 20R$'
        resposta = self.caixa.sacar(20)
        self.assertEqual(esperado, resposta)
    
    def test_saque_50_reais(self):
        esperado = '1 nota de 50R$'
        resposta = self.caixa.sacar(50)
        self.assertEqual(esperado, resposta)
        
    def test_saque_100_reais(self):
        esperado = '1 nota de 100R$'
        resposta = self.caixa.sacar(100)
        self.assertEqual(esperado, resposta)
    
    def test_saque_80_reais(self):
        esperado = '1 nota de 50R$ 1 nota de 20R$ 1 nota de 10R$'
        resposta = self.caixa.sacar(80)
        self.assertEqual(resposta, esperado)
    
    def test_saque_de_70_com_saldo_atualizado(self):
        esperado = '1 nota de 50R$ 1 nota de 20R$'
        resposta = self.caixa.sacar(70)
        self.assertEqual(resposta, esperado)

    def test_saque_17_reais(self):
        with self.assertRaisesRegexp(Exception, 'Nao Ha notas para representar este valor'):
            self.caixa.sacar(17)
            
    def test_saque_200_reais(self):
        esperado = '2 nota de 100R$'
        resposta = self.caixa.sacar(200)
        self.assertEqual(resposta, esperado)


unittest.main()