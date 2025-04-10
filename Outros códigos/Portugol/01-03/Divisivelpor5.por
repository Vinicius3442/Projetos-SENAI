//Atividade 5 Vinicius Arcanjo Lobato Montuani N°29 2°DEV B
programa {
  funcao inicio() {
    inteiro entrada

    escreva("Digite um número inteiro:\n")
    leia(entrada)

    se(entrada % 5 == 0){ //Nesse eu usei  a operação MODÚLO(%)
      limpa()
      escreva("O numero é divisível por 5")
    }
    senao{
      limpa()
      escreva("O número não é divísivel por 5")
    }
  }
}
