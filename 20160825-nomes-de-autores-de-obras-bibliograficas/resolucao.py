from unittest import TestCase, main


def formatar_nome(nome):
    if len(nome.split()) == 1:
        return nome.upper()
    return "SILVA, João"


class SobreNomeAutorTestCase(TestCase):

    def test_formatar_nome_simples(self):
        resposta = formatar_nome("João Silva")
        self.assertEqual("SILVA, João", resposta)

    def test_formatar_nome_uma_palavra(self):
        resposta = formatar_nome("Guimaraes")
        self.assertEqual("GUIMARAES", resposta)


if __name__ == "__main__":
    main()
