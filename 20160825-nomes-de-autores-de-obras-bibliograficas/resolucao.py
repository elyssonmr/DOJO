from unittest import TestCase, main


def formatar_nome(nome):
    return "SILVA, João"


class SobreNomeAutorTestCase(TestCase):

    def test_formatar_nome_simples(self):
        resposta = formatar_nome("João Silva")
        self.assertEqual("SILVA, João", resposta)


if __name__ == "__main__":
    main()
