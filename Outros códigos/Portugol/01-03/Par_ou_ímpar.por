//Atividade 6 Vinicius Montuani
programa {
  funcao inicio() {
    inteiro entrada

    escreva("Digite um número inteiro: ")
    leia(entrada)

    se(entrada % 2 == 0){
      limpa()
      escreva("O número ", entrada, " é um número PAR")
    }
    senao{
      limpa()
      escreva("O número ", entrada, " é um número ÍMPAR")
    }
  }
}
