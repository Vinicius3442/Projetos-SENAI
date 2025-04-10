//Atividade 6 Vinicius Arcanjo Lobato Montuani N°29 2°DEV B
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
