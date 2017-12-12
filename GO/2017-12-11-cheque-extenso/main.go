package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	especiais := map[int]string{
		10: "dez",
		11: "onze",
		12: "doze",
		13: "treze",
		14: "quatorze",
		15: "quinze",
		16: "dezesseis",
		17: "dezesete",
		18: "dezoito",
		19: "dezenove",
	}

	unidade := map[int]string{
		1: "um",
		2: "dois",
		3: "três",
		4: "quatro",
		5: "cinco",
		6: "seis",
		7: "sete",
		8: "oito",
		9: "nove",
	}

	dezena := map[int]string{
		2: "vinte",
		3: "trinta",
		4: "quarenta",
		5: "cinquenta",
		6: "sessenta",
		7: "setenta",
		8: "oitenta",
		9: "noventa",
	}

	centena := map[int]string{
		1: "cento",
		2: "duzentos",
		3: "trezentos",
		4: "quatrocentos",
		5: "quinhentos",
		6: "seiscentos",
		7: "setecentos",
		8: "oitocentos",
		9: "novecentos",
	}

	fmt.Print("Digite o valor da compra (1 a 999): ")
	var valor int
	_, error := fmt.Scanf("%d", &valor)
	if error != nil {
		fmt.Println(error)
		os.Exit(1)
	}
	ordemDivisao := []int{100, 10, 1}
	resultados := []map[int]string{centena, dezena, unidade}
	chequeExtenso := []string{}
	valorCalculo := valor
	for i := 0; i < len(ordemDivisao); i++ {
		ordem := ordemDivisao[i]
		parte := valorCalculo / ordem
		resto := valorCalculo % ordem
		especial, ok := especiais[valorCalculo]
		if !ok {
			extenso, _ := resultados[i][parte]
			if extenso != "" {
				chequeExtenso = append(chequeExtenso, extenso)
			}
		} else {
			if especial != "" {
				chequeExtenso = append(chequeExtenso, especial)
				resto = 0
			}
		}
		if resto == 0 {
			break
		}
		valorCalculo = resto
	}
	fmt.Print("Valor do Cheque por extenso: ")
	moeda := "real"
	if valor > 1 {
		moeda = "reais"
	}
	fmt.Println(strings.Join(chequeExtenso, " e "), moeda)
}
