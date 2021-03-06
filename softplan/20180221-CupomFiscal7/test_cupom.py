import unittest
from unittest import TestCase
from unittest.mock import Mock
from io import StringIO

import cupom_fiscal as cupom


from cupom_fiscal import CLIController
from datetime import date

class ExampleUnitTestTestCase(TestCase):
    def test_sum(self):
        # Setup
        a = 1
        b = 1
        # Execution
        c = a + b
        # Verification
        self.assertEqual(2, c)

    def test_read_database(self):
        """Exploration test"""
        db_dao = Mock()
        db_dao.read_by_name.return_value = {
            "name": "Antedeguemon", "age": 28
        }
        expected = {"name": "Antedeguemon", "age": 28}

        resp = db_dao.read_by_name("Antedeguemon")

        self.assertEqual(expected, resp)
        db_dao.read_by_name.assert_called_once_with(
            "Antedeguemon")


class CupomFiscalTestCase(TestCase):
    def test_writeln_string_io(self):
        io = StringIO()

        cupom.writeln("Teste", io)

        self.assertEqual("Teste\n", io.getvalue())

    def test_writeln_mock(self):
        arquivo = Mock()

        cupom.writeln("Teste", arquivo)

        arquivo.write.assert_called_once_with("Teste\n")

    def test_imprimir_linha_cerquilha(self):
        result = cupom.imprimir_linha_cerquilha()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        esperado = '#' * 35
        self.assertEqual(result, esperado)

    def test_imprimir_separador_sessao(self):
        result = cupom.imprimir_separador_sessao()
        esperado = '#' + '=' *33 + '#'
        self.assertEqual(result, esperado)
    """
    def test_imprimir_cabecalho(self):
        result = cupom.imprimir_cabecalho()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, bool)
        self.assertTrue(result)
    """



class CLIControllerInstanceTestCase(TestCase):
    def test_instance(self):
        controller = CLIController()
        self.assertTrue(hasattr(controller._output, 'write'))

        controller._output.close()


class CLIControllerWritelnTestCase(TestCase):
    def setUp(self):
        self.io = StringIO()
        self.controller = CLIController()
        self.controller._output.close()
        self.controller._output = self.io

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
        self.assertIn(f'Data Compra: {data_compra.strftime("%d/%m/%Y"):<18.18}', self.io.getvalue())

    def test_imprimir_produtos(self):
        lista_produtos = [
        {"descricao": "Nutela", "valor": 15.00},
        {"descricao": "Trident", "valor": 3.50},
        {"descricao": "Pasta de dente", "valor": 10.00},
        ]
        self.controller.imprimir_produtos(lista_produtos)
        self.assertTrue(self.io.getvalue())        

    def tearDown(self):
        self.controller._output.close()


if __name__ == "__main__":
    unittest.main()
