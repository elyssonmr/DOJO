import unittest
from unittest import TestCase
from unittest.mock import Mock
from io import StringIO

import cupom_fiscal as cupom


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





if __name__ == "__main__":
    unittest.main()
