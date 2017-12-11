from unittest import TestCase, main


def formatar_nome(nome):
    palavras = nome.split()
    if len(palavras) == 1:
        return palavras[0].upper()
    if palavras[-1].upper() in ["FILHO", "FILHA", "NETO", "NETA", "SOBRINHO", "SOBRINHA", "JUNIOR"]:
        restante = " ".join(palavras[:-2])
        maiusculo = " ".join([palavras[-2].upper(), palavras[-1].upper()])
        return "{}, {}".format(maiusculo, restante)
    restante = " ".join(palavras[:-1])
    return "{}, {}".format(palavras[-1].upper(), restante)


class SobreNomeAutorTestCase(TestCase):

    def test_formatar_nome_simples(self):
        resposta = formatar_nome("João Silva")
        self.assertEqual("SILVA, João", resposta)

    def test_formatar_nome_simples_rezende(self):
        resposta = formatar_nome("Élysson Mendes Rezende")
        self.assertEqual("REZENDE, Élysson Mendes", resposta)

    def test_formatar_nome_uma_palavra(self):
        resposta = formatar_nome("Guimaraes")
        self.assertEqual("GUIMARAES", resposta)

    def test_formatar_nome_sobrenome_filho(self):
        resposta = formatar_nome("Élysson Mendes Rezende Filho")
        self.assertEqual("REZENDE FILHO, Élysson Mendes", resposta)


if __name__ == "__main__":
    main()
