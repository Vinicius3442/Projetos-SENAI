//Atividade 11 Vinicius Montuani
programa {
  funcao inicio() {

    inteiro lado1, lado2, lado3
    cadeia triangulo

    escreva("Digite o valor do primeiro lado:\n")
    leia(lado1)

    escreva("Digite o valor do segundo lado:\n")
    leia(lado2)

    escreva("Digite o valor do terceiro lado:\n")
    leia(lado3)

    se(lado1 == lado2 e lado2 == lado3 e lado1 == lado3){
      limpa()
      triangulo = "Equilatero"
      escreva("O triângulo é:\n", triangulo)
    }

    senao se(lado1 == lado2 e lado2 != lado3 e lado1 != lado3 ou lado2 == lado3 e lado1 != lado3 e lado2 != lado1 ou lado1 == lado3 e lado1 != lado2 e lado2 != lado3){
      limpa()
      triangulo = "Isósceles"
      escreva("O triângulo é:\n", triangulo)
    }

    senao se(lado1 != lado2 e lado2 != lado3 e lado1 != lado3){
      limpa()
      triangulo = "Escaleno"
      escreva("O triângulo é:\n", triangulo)
    }
  }
}
