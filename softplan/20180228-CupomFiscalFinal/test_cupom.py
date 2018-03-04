import unittest
from unittest import TestCase
from unittest.mock import patch, call
from io import StringIO

from cupom_fiscal import CLIController
from datetime import date


class CLIControllerInstanceTestCase(TestCase):
    def test_instance(self):
        controller = CLIController("Cupom")
        self.assertEqual("Cupom", controller._output)
        self.assertListEqual([], controller._produtos)


class CLIControllerWritelnTestCase(TestCase):
    def setUp(self):
        self.io = StringIO()
        self.controller = CLIController(self.io)

    @patch("builtins.input")
    def test_read_product(self, _input):
        _input.side_effect = ["Pasta de Dente", "10.00", "n"]
        expected = [{
            "descricao": "Pasta de Dente",
            "valor": 10.00
        }]
        expected_calls = [call("Produto: "), call("Valor: "),
                          call("Deseja continuar cadastrando? ")]

        self.controller.ler_produtos()

        self.assertListEqual(expected, self.controller._produtos)
        _input.assert_has_calls(expected_calls)


    @patch("builtins.input")
    def test_read_multiple_products(self, _input):
        _input.side_effect = ["Produto1", "1.00", "S", "Produto2", "2.00", "n"]
        expected = [{
            "descricao": "Produto1",
            "valor": 1.00
        }, {
            "descricao": "Produto2",
            "valor": 2.00
        }]
        expected_calls = [call("Produto: "), call("Valor: "),
                          call("Deseja continuar cadastrando? ")]
        # duplicamos por causa de cadastarmos 2 produtos
        expected_calls.extend(expected_calls)

        self.controller.ler_produtos()

        self.assertListEqual(expected, self.controller._produtos)
        _input.assert_has_calls(expected_calls)

    def test_writeln(self):
        self.controller.writeln("Teste")
        self.assertEqual("Teste\n", self.io.getvalue())

    def test_escrever_linha_cerquilha(self):
        self.controller.escrever_linha_cerquilha()
        self.assertEqual("#"*35+'\n', self.io.getvalue())

    def test_escrever_separador_sessao(self):
        self.controller.escrever_separador_sessao()
        self.assertEqual("#"+"="*33+"#\n", self.io.getvalue())
    
    def test_imprimir_cabecalho(self):
        self.controller.imprimir_cabecalho()
        self.assertTrue(self.io.getvalue())
        self.assertIn('# Sistema de Venda Sr. José', self.io.getvalue())
        
        data_compra = date.today()
        self.assertIn(f'Data Compra: {data_compra.strftime("%d/%m/%Y")}',
                      self.io.getvalue())

    def test_imprimir_produto(self):
        item = {
            "descricao": "Test Prod",
            "valor": 15.00
        }
        expected = "# 1       |Test Prod | R$   15.00 #\n"

        self.controller.imprimir_item(item, 1)

        self.assertEqual(expected, self.io.getvalue())

    def test_imprimir_produtos(self):
        self.controller._produtos = [
        {"descricao": "Nutela", "valor": 15.00},
        {"descricao": "Trident", "valor": 3.50},
        {"descricao": "Pasta de dente", "valor": 10.00},
        ]
        self.controller.imprimir_produtos()
        self.assertTrue(self.io.getvalue())

    def test_imprimir_rodape(self):
        self.controller.imprimir_rodape()

        impresso = self.io.getvalue()
        self.assertIn("Obrigado Volte Sempre", impresso)
        self.assertIn("DOJO Interprises SA", impresso)
        self.assertIn("Venda Sr. José agradece", impresso)

    @patch("cupom_fiscal.CLIController.imprimir_cabecalho")
    @patch("cupom_fiscal.CLIController.imprimir_produtos")
    @patch("cupom_fiscal.CLIController.imprimir_rodape")
    def test_imprimir_cupom(self, _rodape, _produtos, _cabecalho):
        self.controller.imprimir_cupom()
        
        _rodape.assert_called_once_with()
        _produtos.assert_called_once_with()
        _cabecalho.assert_called_once_with()

    def tearDown(self):
        self.controller._output.close()


if __name__ == "__main__":
    unittest.main()
